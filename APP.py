import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64

# --- Autenticación simple ---
def check_credentials(username, password):
    valid_users = {
        "admin": "admin123",
        "demo": "demo"
    }
    return username in valid_users and password == valid_users[username]

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user' not in st.session_state:
    st.session_state['user'] = None

# --- PORTADA DE LOGIN ---
def show_login_page():
    st.set_page_config(
        page_title="CONSORCIO DEJ - Pavimento Rígido/Flexible",
        page_icon="🛣️",
        layout="wide"
    )
    st.markdown("""
    <div style="text-align: center; padding: 30px; background-color: #FFD700; color: #2F2F2F; border-radius: 10px; margin-bottom: 20px; border: 2px solid #FFA500;">
        <h1>🛣️ CONSORCIO DEJ</h1>
        <p style="font-size: 18px; font-weight: bold;">Sistema de Diseño de Pavimentos</p>
        <p style="font-size: 14px;">Ingrese sus credenciales para acceder</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("Ingrese usuario y contraseña para acceder al sistema.\n\n**admin / admin123** o **demo / demo**")
    with st.form("login_form"):
        username = st.text_input("Usuario", key="login_user")
        password = st.text_input("Contraseña", type="password", key="login_pass")
        submitted = st.form_submit_button("Entrar")
        if submitted:
            if check_credentials(username, password):
                st.session_state['logged_in'] = True
                st.session_state['user'] = username
                st.experimental_rerun()
                st.stop()  # <-- Esto es clave para cortar el flujo tras el rerun
            else:
                st.error("Usuario o contraseña incorrectos.")
    st.stop()

if not st.session_state['logged_in']:
    show_login_page()

# --- App principal (solo si autenticado) ---
st.set_page_config(
    page_title="CONSORCIO DEJ - Pavimento Rígido/Flexible",
    page_icon="🛣️",
    layout="wide"
)

# --- Barra superior con botón de cerrar sesión ---
with st.container():
    col_logo, col_title, col_user, col_logout = st.columns([0.12, 0.55, 0.18, 0.15])
    with col_logo:
        st.markdown("<div style='text-align:center;'><span style='font-size:38px;'>🛣️</span></div>", unsafe_allow_html=True)
    with col_title:
        st.markdown("<div style='text-align:center;'><h2 style='color:#2F2F2F;margin-bottom:0;'>CONSORCIO DEJ</h2><span style='font-size:16px;color:#555;'>Diseño de Pavimentos Rígido y Flexible</span></div>", unsafe_allow_html=True)
    with col_user:
        st.markdown(f"<div style='text-align:right;'><b>Usuario:</b> <span style='color:#1976D2'>{st.session_state['user']}</span></div>", unsafe_allow_html=True)
    with col_logout:
        if st.button("Cerrar Sesión", key="logout_btn"):
            st.session_state['logged_in'] = False
            st.session_state['user'] = None
            st.experimental_rerun()

st.info("""
Bienvenido al sistema profesional de diseño de pavimentos. Complete los datos del proyecto y presione **Calcular** para obtener resultados y recomendaciones según normativa peruana. 

> **Tip:** Puede editar la tabla de tránsito y cambiar unidades en la parte inferior derecha.
""")

# Panel principal con 3 columnas
col_izq, col_centro, col_der = st.columns([1.2, 1.1, 1.2])

# -------- PANEL IZQUIERDO: DATOS GENERALES --------
with col_izq:
    st.markdown("#### <span style='color:#1976D2'>Datos generales</span>", unsafe_allow_html=True)
    with st.container():
        proyecto = st.text_input("Proyecto", "")
        descripcion = st.text_input("Descripción", "")
        periodo = st.number_input("Período de diseño", 5, 50, 20, help="años")
        espesor_losa = st.number_input("Espesor de la losa", 10, 40, 20, help="mm/in", format="%d")
        modulo_rotura = st.number_input("Módulo de rotura", 100, 1000, 450, help="psi/MPa")
        dovelas = st.radio("Dovelas", ["Sí", "No"], horizontal=True, index=0)
        bermas = st.radio("Bermas", ["Sí", "No"], horizontal=True, index=1)
    st.divider()
    st.markdown("#### <span style='color:#1976D2'>Módulo de reacción de la subrasante (K)</span>", unsafe_allow_html=True)
    subrasante_tipo = st.radio("Subrasante", ["Ingreso directo", "Correlación con CBR"], index=1)
    if subrasante_tipo == "Ingreso directo":
        k_val = st.number_input("K =", 10, 500, 99, help="pci/MPa/m")
    else:
        cbr = st.number_input("CBR =", 1, 20, 3)
        st.info("K se calculará por correlación con CBR")
    st.divider()
    subbase = st.checkbox("Subbase", value=True)
    if subbase:
        espesor_subbase = st.number_input("Espesor", 1, 50, 10, help="mm/in")
        tipo_subbase = st.radio("Tipo de subbase", ["Sin tratar", "Tratada con cemento"], horizontal=True)
    st.divider()
    st.markdown("#### <span style='color:#1976D2'>Barras de anclaje</span>", unsafe_allow_html=True)
    diam_barras = st.selectbox("Diámetro de barra", ["3/8\"", "1/2\"", "5/8\"", "3/4\""])
    acero_fy = st.number_input("Acero (fy)", 200, 600, 280, help="MPa")
    ancho_carril = st.number_input("Ancho de carril", 2.5, 4.0, 3.05, step=0.01, help="m")

# -------- PANEL CENTRAL: TRÁNSITO --------
with col_centro:
    st.markdown("#### <span style='color:#388E3C'>Tránsito</span>", unsafe_allow_html=True)
    with st.container():
        factor_seg = st.selectbox("Factor de seguridad", [1.0, 1.1, 1.2, 1.3, 1.4], index=2)
        tipo_ejes = st.selectbox("Tipo de Ejes", ["Ejes Simples", "Ejes Tándem"])
    st.markdown("##### <span style='color:#388E3C'>Tabla de Tránsito</span>", unsafe_allow_html=True)
    st.caption("Carga (kN/kips) y repeticiones")
    tabla_default = {
        "Carga": [52, 48, 44, 36, 32, 28, 24, 20, 16],
        "Repeticiones": [21320, 42810, 124900, 372900, 885800, 930700, 1656000, 984900, 1356000]
    }
    tabla = st.data_editor(tabla_default, num_rows="dynamic", use_container_width=True)
    st.divider()

# --- FUNCIONES DE CÁLCULO ---
def calcular_espesor_losa_rigido(W18, k, R, C, Sc, J, Ec):
    # D = sqrt( (W18 * k * (1-R)) / (C * (Sc * J * (Ec/k)**0.25)) )
    try:
        numerador = W18 * k * (1 - R)
        denominador = C * (Sc * J * (Ec / k) ** 0.25)
        D = (numerador / denominador) ** 0.5
        return D
    except Exception:
        return 0

def calcular_junta_L(sigma_t, gamma_c, f, mu, w):
    # L <= (f * mu * w) / (2 * sigma_t * gamma_c)
    try:
        L = (f * mu * w) / (2 * sigma_t * gamma_c)
        return L
    except Exception:
        return 0

def calcular_As_temp(gamma_c, L, h, fa, fs):
    # As = (gamma_c * L * h * fa) / (2 * fs)
    try:
        As = (gamma_c * L * h * fa) / (2 * fs)
        return As
    except Exception:
        return 0

def calcular_SN_flexible(a1, D1, a2, D2, m2, a3, D3, m3):
    # SN = a1*D1 + a2*D2*m2 + a3*D3*m3
    try:
        SN = a1 * D1 + a2 * D2 * m2 + a3 * D3 * m3
        return SN
    except Exception:
        return 0

# --- Panel derecho: lógica de cálculo y visualización ---
with col_der:
    st.markdown("#### <span style='color:#D32F2F'>Análisis</span>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    calcular = st.button("🚀 Calcular", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.divider()

    # --- CÁLCULO PAVIMENTO RÍGIDO ---
    if calcular:
        # Parámetros de entrada (puedes ajustar nombres según tus campos)
        # Ejemplo: W18, k, R, C, Sc, J, Ec
        W18 = sum(tabla['Repeticiones']) if 'Repeticiones' in tabla else 100000
        k = k_val if subrasante_tipo == "Ingreso directo" else 99
        R = 0.95  # Confiabilidad (puedes agregar campo)
        C = 1.0   # Coef. drenaje (puedes agregar campo)
        Sc = modulo_rotura  # Resistencia a flexión
        J = 3.2   # Coef. transferencia (puedes agregar campo)
        Ec = 300000  # Módulo elasticidad (puedes agregar campo)
        D = calcular_espesor_losa_rigido(W18, k, R, C, Sc, J, Ec)

        # Juntas (ejemplo)
        sigma_t = 45  # esfuerzo admisible (puedes agregar campo)
        gamma_c = 2400  # peso unitario (puedes agregar campo)
        f = 1.5  # coef. fricción
        mu = 1.0  # coef. fricción
        w = D * 1.0  # peso de losa (simplificado)
        L_junta = calcular_junta_L(sigma_t, gamma_c, f, mu, w)

        # Refuerzo por temperatura (si aplica)
        fa = 1.5
        fs = acero_fy
        As_temp = calcular_As_temp(gamma_c, L_junta, D, fa, fs)

        # Mostrar resultados
        st.markdown(f"**Espesor de losa calculado (D):** <span style='color:#1976D2;font-size:20px'><b>{D:.2f} cm</b></span>", unsafe_allow_html=True)
        st.markdown(f"**Junta máxima (L):** <span style='color:#1976D2'>{L_junta:.2f} m</span>", unsafe_allow_html=True)
        st.markdown(f"**Área de acero por temperatura (As):** <span style='color:#1976D2'>{As_temp:.2f} cm²</span>", unsafe_allow_html=True)
        st.markdown(f"**Número de ejes equivalentes (W18):** {W18}")
        st.markdown(f"**Módulo de reacción (k):** {k}")
        st.markdown(f"**Resistencia a flexión (Sc):** {Sc}")
        st.markdown(f"**Módulo elasticidad (Ec):** {Ec}")
        st.markdown(f"**Coef. transferencia (J):** {J}")
        st.markdown(f"**Coef. drenaje (C):** {C}")
        st.markdown(f"**Confiabilidad (R):** {R}")
        st.divider()

        # --- CÁLCULO PAVIMENTO FLEXIBLE (opcional, si tienes panel) ---
        # Ejemplo de campos para flexible:
        # a1, D1, a2, D2, m2, a3, D3, m3 = ...
        # SN = calcular_SN_flexible(a1, D1, a2, D2, m2, a3, D3, m3)
        # st.markdown(f"**Número estructural (SN):** <span style='color:#388E3C'>{SN:.2f}</span>", unsafe_allow_html=True)

    # --- ANÁLISIS DE SENSIBILIDAD Y GRÁFICOS ---
    sensibilidad = st.button("📊 Análisis de sensibilidad", use_container_width=True, key="btn_sensibilidad")
    if sensibilidad:
        # Parámetros base
        W18 = sum(tabla['Repeticiones']) if 'Repeticiones' in tabla else 100000
        k = k_val if subrasante_tipo == "Ingreso directo" else 99
        R = 0.95
        C = 1.0
        Sc = modulo_rotura
        J = 3.2
        Ec = 300000
        
        # Rangos más amplios y realistas
        k_range = np.linspace(30, 500, 50)  # pci
        Sc_range = np.linspace(200, 800, 50)  # psi
        Ec_range = np.linspace(200000, 500000, 50)  # psi
        W18_range = np.linspace(50000, 500000, 50)
        R_range = np.linspace(0.80, 0.99, 50)
        
        # Cálculos de sensibilidad
        D_k = [calcular_espesor_losa_rigido(W18, kx, R, C, Sc, J, Ec) for kx in k_range]
        D_Sc = [calcular_espesor_losa_rigido(W18, k, R, C, scx, J, Ec) for scx in Sc_range]
        D_Ec = [calcular_espesor_losa_rigido(W18, k, R, C, Sc, J, ecx) for ecx in Ec_range]
        D_W18 = [calcular_espesor_losa_rigido(w18x, k, R, C, Sc, J, Ec) for w18x in W18_range]
        D_R = [calcular_espesor_losa_rigido(W18, k, rx, C, Sc, J, Ec) for rx in R_range]
        
        # Gráfico combinado
        fig_combined, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # D vs k
        ax1.plot(k_range, D_k, color='blue', linewidth=2)
        ax1.axvline(x=k, color='red', linestyle='--', alpha=0.7, label=f'Valor actual: {k}')
        ax1.set_title('Espesor de losa vs Módulo de reacción (k)', fontsize=12, fontweight='bold')
        ax1.set_xlabel('Módulo de reacción k (pci)')
        ax1.set_ylabel('Espesor de losa D (pulg)')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # D vs Sc
        ax2.plot(Sc_range, D_Sc, color='green', linewidth=2)
        ax2.axvline(x=Sc, color='red', linestyle='--', alpha=0.7, label=f'Valor actual: {Sc}')
        ax2.set_title('Espesor de losa vs Módulo de rotura (Sc)', fontsize=12, fontweight='bold')
        ax2.set_xlabel('Módulo de rotura Sc (psi)')
        ax2.set_ylabel('Espesor de losa D (pulg)')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        # D vs W18
        ax3.plot(W18_range, D_W18, color='orange', linewidth=2)
        ax3.axvline(x=W18, color='red', linestyle='--', alpha=0.7, label=f'Valor actual: {W18:,.0f}')
        ax3.set_title('Espesor de losa vs Tránsito (W18)', fontsize=12, fontweight='bold')
        ax3.set_xlabel('Número de ejes equivalentes W18')
        ax3.set_ylabel('Espesor de losa D (pulg)')
        ax3.grid(True, alpha=0.3)
        ax3.legend()
        
        # D vs R
        ax4.plot(R_range, D_R, color='purple', linewidth=2)
        ax4.axvline(x=R, color='red', linestyle='--', alpha=0.7, label=f'Valor actual: {R}')
        ax4.set_title('Espesor de losa vs Confiabilidad (R)', fontsize=12, fontweight='bold')
        ax4.set_xlabel('Confiabilidad R')
        ax4.set_ylabel('Espesor de losa D (pulg)')
        ax4.grid(True, alpha=0.3)
        ax4.legend()
        
        plt.tight_layout()
        st.pyplot(fig_combined)
        
        # Tabla de resultados y recomendaciones
        st.markdown("### 📋 Resultados del Análisis de Sensibilidad")
        
        # Análisis de fatiga y erosión (simplificado)
        D_actual = calcular_espesor_losa_rigido(W18, k, R, C, Sc, J, Ec)
        fatiga_actual = (W18 / (10**7)) * (D_actual / Sc) ** 3.42  # Simplificado
        erosion_actual = (W18 / (10**6)) * (D_actual / k) ** 7.35  # Simplificado
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Espesor Actual", f"{D_actual:.2f} pulg")
        with col2:
            st.metric("Fatiga (%)", f"{fatiga_actual*100:.2f}%")
        with col3:
            st.metric("Erosión (%)", f"{erosion_actual*100:.2f}%")
        
        # Recomendaciones automáticas
        st.markdown("### 💡 Recomendaciones Automáticas")
        
        if fatiga_actual > 1.0:
            st.warning("⚠️ **Fatiga crítica detectada.** Considere aumentar el espesor de losa o mejorar la resistencia del concreto.")
        elif fatiga_actual > 0.5:
            st.info("ℹ️ **Fatiga moderada.** El diseño está en el límite aceptable.")
        else:
            st.success("✅ **Fatiga dentro de límites seguros.**")
            
        if erosion_actual > 1.0:
            st.warning("⚠️ **Erosión crítica detectada.** Considere mejorar la subrasante o aumentar el espesor de subbase.")
        elif erosion_actual > 0.5:
            st.info("ℹ️ **Erosión moderada.** Verificar drenaje y calidad de subrasante.")
        else:
            st.success("✅ **Erosión dentro de límites seguros.**")
        
        # Análisis de sensibilidad numérico
        st.markdown("### 📊 Análisis de Sensibilidad Numérico")
        
        # Calcular sensibilidad (% cambio en D por % cambio en parámetro)
        sens_k = abs((D_k[25] - D_k[24]) / D_k[24]) / abs((k_range[25] - k_range[24]) / k_range[24])
        sens_Sc = abs((D_Sc[25] - D_Sc[24]) / D_Sc[24]) / abs((Sc_range[25] - Sc_range[24]) / Sc_range[24])
        sens_W18 = abs((D_W18[25] - D_W18[24]) / D_W18[24]) / abs((W18_range[25] - W18_range[24]) / W18_range[24])
        
        sensibilidad_df = pd.DataFrame({
            'Parámetro': ['Módulo de reacción (k)', 'Módulo de rotura (Sc)', 'Tránsito (W18)'],
            'Sensibilidad': [sens_k, sens_Sc, sens_W18],
            'Impacto': ['Alto' if s > 0.5 else 'Medio' if s > 0.2 else 'Bajo' for s in [sens_k, sens_Sc, sens_W18]]
        })
        
        st.dataframe(sensibilidad_df, use_container_width=True)
        
        # Exportación PDF mejorada
        st.markdown("### 📤 Exportar Resultados Completos")
        
        # Crear PDF con todos los resultados
        if st.button("📄 Generar Reporte PDF Completo", key="btn_export_pdf"):
            try:
                # Crear figura con todos los resultados
                fig_report = plt.figure(figsize=(16, 20))
                
                # Subplot 1: Gráficos de sensibilidad
                plt.subplot(4, 2, 1)
                plt.plot(k_range, D_k, color='blue', linewidth=2)
                plt.axvline(x=k, color='red', linestyle='--', alpha=0.7, label=f'Valor actual: {k}')
                plt.title('Espesor vs Módulo de reacción (k)', fontsize=10, fontweight='bold')
                plt.xlabel('k (pci)')
                plt.ylabel('D (pulg)')
                plt.grid(True, alpha=0.3)
                plt.legend()
                
                plt.subplot(4, 2, 2)
                plt.plot(Sc_range, D_Sc, color='green', linewidth=2)
                plt.axvline(x=Sc, color='red', linestyle='--', alpha=0.7, label=f'Valor actual: {Sc}')
                plt.title('Espesor vs Módulo de rotura (Sc)', fontsize=10, fontweight='bold')
                plt.xlabel('Sc (psi)')
                plt.ylabel('D (pulg)')
                plt.grid(True, alpha=0.3)
                plt.legend()
                
                plt.subplot(4, 2, 3)
                plt.plot(W18_range, D_W18, color='orange', linewidth=2)
                plt.axvline(x=W18, color='red', linestyle='--', alpha=0.7, label=f'Valor actual: {W18:,.0f}')
                plt.title('Espesor vs Tránsito (W18)', fontsize=10, fontweight='bold')
                plt.xlabel('W18')
                plt.ylabel('D (pulg)')
                plt.grid(True, alpha=0.3)
                plt.legend()
                
                plt.subplot(4, 2, 4)
                plt.plot(R_range, D_R, color='purple', linewidth=2)
                plt.axvline(x=R, color='red', linestyle='--', alpha=0.7, label=f'Valor actual: {R}')
                plt.title('Espesor vs Confiabilidad (R)', fontsize=10, fontweight='bold')
                plt.xlabel('R')
                plt.ylabel('D (pulg)')
                plt.grid(True, alpha=0.3)
                plt.legend()
                
                # Subplot 5: Tabla de resultados
                plt.subplot(4, 2, (5, 6))
                plt.axis('off')
                table_data = [
                    ['Parámetro', 'Valor Actual', 'Resultado'],
                    ['Espesor de losa (D)', f'{D_actual:.2f} pulg', 'Calculado'],
                    ['Fatiga (%)', f'{fatiga_actual*100:.2f}%', 'Analizado'],
                    ['Erosión (%)', f'{erosion_actual*100:.2f}%', 'Analizado'],
                    ['Módulo de reacción (k)', f'{k} pci', 'Entrada'],
                    ['Módulo de rotura (Sc)', f'{Sc} psi', 'Entrada'],
                    ['Tránsito (W18)', f'{W18:,.0f}', 'Calculado'],
                    ['Confiabilidad (R)', f'{R}', 'Entrada']
                ]
                table = plt.table(cellText=table_data[1:], colLabels=table_data[0], 
                                cellLoc='center', loc='center', colWidths=[0.3, 0.3, 0.2])
                table.auto_set_font_size(False)
                table.set_fontsize(9)
                table.scale(1, 2)
                plt.title('Resultados del Análisis', fontsize=12, fontweight='bold', pad=20)
                
                # Subplot 6: Tabla de sensibilidad
                plt.subplot(4, 2, (7, 8))
                plt.axis('off')
                sens_table_data = [
                    ['Parámetro', 'Sensibilidad', 'Impacto'],
                    ['Módulo de reacción (k)', f'{sens_k:.3f}', 'Alto' if sens_k > 0.5 else 'Medio' if sens_k > 0.2 else 'Bajo'],
                    ['Módulo de rotura (Sc)', f'{sens_Sc:.3f}', 'Alto' if sens_Sc > 0.5 else 'Medio' if sens_Sc > 0.2 else 'Bajo'],
                    ['Tránsito (W18)', f'{sens_W18:.3f}', 'Alto' if sens_W18 > 0.5 else 'Medio' if sens_W18 > 0.2 else 'Bajo']
                ]
                sens_table = plt.table(cellText=sens_table_data[1:], colLabels=sens_table_data[0], 
                                     cellLoc='center', loc='center', colWidths=[0.4, 0.3, 0.2])
                sens_table.auto_set_font_size(False)
                sens_table.set_fontsize(9)
                sens_table.scale(1, 2)
                plt.title('Análisis de Sensibilidad', fontsize=12, fontweight='bold', pad=20)
                
                plt.tight_layout()
                
                # Guardar PDF
                pdf_buffer = BytesIO()
                fig_report.savefig(pdf_buffer, format='pdf', bbox_inches='tight', dpi=300)
                pdf_buffer.seek(0)
                
                # Botón de descarga
                st.download_button(
                    label="📥 Descargar Reporte PDF Completo",
                    data=pdf_buffer.getvalue(),
                    file_name=f"reporte_pavimento_{proyecto}.pdf",
                    mime="application/pdf",
                    key="btn_download_pdf"
                )
                
                st.success("✅ Reporte PDF generado exitosamente con todos los resultados y gráficos.")
                
            except Exception as e:
                st.error(f"❌ Error al generar PDF: {str(e)}")
        
        st.success("✅ Análisis de sensibilidad completado con gráficos, recomendaciones y opción de exportación.")

    else:
        st.markdown("**Espesor de losa :**  ", help="mm/in")
        st.markdown("**Módulo de rotura :**  ", help="psi/MPa")
        st.markdown("**K del conjunto :**  ", help="pci/MPa/m")
        st.markdown("**Período de diseño :**  ", help="años")
        st.markdown("<span style='color:red'><b>Porcentaje de fatiga</b></span>: 0.00", unsafe_allow_html=True)
        st.markdown("<span style='color:red'><b>Porcentaje de erosión</b></span>: 0.00", unsafe_allow_html=True)
        st.divider()
        st.markdown("**Recomendación para barras de anclaje:**")
        st.markdown("Longitud:  ")
        st.markdown("Separación entre barras:  ")
        st.markdown("**Recomendación para pasadores (fy=60 ksi):**")
        st.markdown("Longitud:  ")
        st.markdown("Separación entre barras:  ")
        st.markdown("Diámetro de barras:  ")
        st.divider()
        st.markdown("Sistema de unidades :   ", help="SI / Inglés")
        st.radio("", ["SI", "Inglés"], horizontal=True, index=0, key="radio_unidades")
        st.divider()
        st.success("Resultados y gráficos aparecerán aquí tras el cálculo.")
