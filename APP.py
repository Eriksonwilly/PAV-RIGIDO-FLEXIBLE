import streamlit as st
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="CONSORCIO DEJ - Pavimento Rígido/Flexible",
    page_icon="🛣️",
    layout="wide"
)

# Banner superior con fondo y estilo profesional
st.markdown("""
<div style="text-align: center; padding: 20px; background-color: #FFD700; color: #2F2F2F; border-radius: 10px; margin-bottom: 20px; border: 2px solid #FFA500;">
    <h1>🛣️ CONSORCIO DEJ</h1>
    <p style="font-size: 18px; font-weight: bold;">Diseño de Pavimentos Rígido y Flexible</p>
    <p style="font-size: 14px;">Normativa Peruana MTC 2020 / 2018 | Inspirado en PCAcalculo</p>
</div>
""", unsafe_allow_html=True)

# Mensaje de bienvenida y ayuda
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

# -------- PANEL DERECHO: ANÁLISIS Y RESULTADOS --------
with col_der:
    st.markdown("#### <span style='color:#D32F2F'>Análisis</span>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.button("🚀 Calcular", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.divider()
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
