import streamlit as st
import numpy as np

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
        st.button("📊 Análisis de sensibilidad", use_container_width=True)
        st.divider()
        col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4)
        with col_btn1:
            st.button("💾 Guardar")
        with col_btn2:
            st.button("📂 Abrir")
        with col_btn3:
            st.button("📝 TXT")
        with col_btn4:
            st.button("❌ Salir")
        st.divider()
        st.markdown("Sistema de unidades :   ", help="SI / Inglés")
        st.radio("", ["SI", "Inglés"], horizontal=True, index=0)
        st.divider()
        st.success("Resultados y gráficos aparecerán aquí tras el cálculo.")
