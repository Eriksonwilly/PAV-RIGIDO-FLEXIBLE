import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
import json
import os
from datetime import datetime

# --- CONFIGURACIÓN INICIAL DE STREAMLIT ---
st.set_page_config(
    page_title="CONSORCIO DEJ - Pavimento Rígido/Flexible",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MÓDULOS AVANZADOS DE INTEGRACIÓN ---
try:
    from MODULO_LIDAR_DRONES import procesamiento_completo_lidar
    from MODULO_DISENO_AUTOMATIZADO import diseno_automatizado_completo
    from MODULO_INTEROPERABILIDAD import interoperabilidad_completa
    from MODULO_GOOGLE_EARTH_ENGINE import analisis_satelital_completo
    from MODULO_LIDAR_AVANZADO import procesamiento_lidar_completo_avanzado
    from MODULO_EXPORTACION_EXTERNA import exportacion_completa_externa
    MODULOS_AVANZADOS_DISPONIBLES = True
except ImportError:
    MODULOS_AVANZADOS_DISPONIBLES = False
    print("⚠️ Módulos avanzados no disponibles. Usando funcionalidad básica.")

# --- FUNCIÓN DE COMPATIBILIDAD ---
def calcular_espesor_losa_rigido(W18, k, R, C, Sc, J, Ec, sistema_unidades):
    """
    Función de compatibilidad para calcular espesor de losa rígido
    """
    try:
        # Usar la función actualizada si está disponible
        return calcular_pavimento_rigido_completo(
            k_30MPa=k,
            ESALs=W18,
            f_c=28,
            j=J,
            modulo_rotura=Sc/145.038,  # Convertir de psi a MPa
            sistema_unidades=sistema_unidades
        )
    except:
        # Función de respaldo simplificada
        D = 8.0  # Espesor inicial en pulgadas
        for _ in range(10):  # Máximo 10 iteraciones
            # Fórmula AASHTO 93 simplificada
            log_W18 = 7.35 * np.log10(D + 1) - 0.06 + np.log10(Sc * D**0.75 - 1.132) / (1 + 1.624e7 / (D + 1)**8.46)
            W18_calc = 10**log_W18
            
            if abs(W18_calc - W18) / W18 < 0.01:  # 1% de tolerancia
                break
            
            if W18_calc > W18:
                D += 0.5
            else:
                D -= 0.5
        
        return {
            "espesor_mm": D * 25.4,
            "espesor_pulg": D,
            "unidad_espesor": "mm",
            "espaciamiento_juntas": 61.5,
            "tipo_refuerzo": "Pasadores",
            "refuerzo_acero": "No requerido",
            "fatiga": 0.45,
            "erosion": 0.32
        }

# --- GESTIÓN ROBUSTA DE DEPENDENCIAS Y GRÁFICOS ---
# Importar matplotlib con manejo de errores
try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle, Polygon
    import matplotlib
    matplotlib.use('Agg')  # Backend no interactivo para Streamlit
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    plt = None
    Rectangle = None
    Polygon = None

# Verificación de plotly
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# Verificación de reportlab
try:
    from reportlab.lib.pagesizes import A4, letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image as RLImage
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

# Decorador seguro para matplotlib
from functools import wraps
def safe_matplotlib_plot(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not MATPLOTLIB_AVAILABLE:
            st.warning("⚠️ Matplotlib no está disponible. No se puede generar el gráfico.")
            return None
        try:
            return func(*args, **kwargs)
        except Exception as e:
            st.error(f"Error generando gráfico: {str(e)}")
            return None
    return wrapper

# --- SISTEMA DE AUTENTICACIÓN ---
def check_credentials(username, password):
    """Verifica las credenciales del usuario"""
    valid_credentials = {
        "admin": "admin123",
        "demo": "demo",
        "user": "password"
    }
    return username in valid_credentials and valid_credentials[username] == password

# --- INICIALIZACIÓN DE SESSION STATE ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user' not in st.session_state:
    st.session_state['user'] = None

# --- PÁGINA DE LOGIN ---
if not st.session_state['logged_in']:
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
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")
    st.stop()

# --- APLICACIÓN PRINCIPAL (solo si autenticado) ---
# Barra superior con botones de acceso rápido
with st.container():
    col_logo, col_title, col_user, col_caso, col_analisis, col_logout = st.columns([0.10, 0.45, 0.13, 0.10, 0.10, 0.12])
    with col_logo:
        st.markdown("<div style='text-align:center;'><span style='font-size:38px;'>🛣️</span></div>", unsafe_allow_html=True)
    with col_title:
        st.markdown("<div style='text-align:center;'><h2 style='color:#2F2F2F;margin-bottom:0;'>CONSORCIO DEJ</h2><span style='font-size:16px;color:#555;'>Diseño de Pavimentos Rígido y Flexible</span></div>", unsafe_allow_html=True)
    with col_user:
        st.markdown(f"<div style='text-align:right;'><b>Usuario:</b> <span style='color:#1976D2'>{st.session_state['user']}</span></div>", unsafe_allow_html=True)
    with col_caso:
        if st.button("🚁 Caso Práctico", key="btn_caso_practico"):
            st.session_state['tab_index'] = 5
            st.rerun()
    with col_analisis:
        if st.button("🌍 Análisis Avanzado", key="btn_analisis_avanzado"):
            st.session_state['tab_index'] = 6
            st.rerun()
    with col_logout:
        if st.button("Cerrar Sesión", key="logout_btn"):
            st.session_state['logged_in'] = False
            st.session_state['user'] = None
            st.rerun()

st.info("""
Bienvenido al sistema profesional de diseño de pavimentos. Complete los datos del proyecto y presione **Calcular** para obtener resultados y recomendaciones según normativa peruana. 

> **Tip:** Puede editar la tabla de tránsito y cambiar unidades en la parte inferior derecha.
""")

# --- CONTROL DE PESTAÑA ACTIVA ---
if 'tab_index' not in st.session_state:
    st.session_state['tab_index'] = 0

# --- ESTRUCTURA DE PESTAÑAS PRINCIPALES ---
tab_labels = [
    'Pavimento Rígido',
    'Pavimento Flexible',
    'Veredas y Cunetas',
    'Drenaje',
    'Normativas Locales',
    '🚁 Caso Práctico San Miguel',
    '🌍 Análisis Avanzado'
]
tabs = st.tabs(tab_labels)

# --- PESTAÑAS CON BLOQUES ROBUSTOS ---
for i, tab in enumerate(tabs):
    with tab:
        try:
            if i == 0:
                # Código de Pavimento Rígido aquí
                pass
            elif i == 1:
                # Código de Pavimento Flexible aquí
                pass
            elif i == 2:
                # Código de Veredas y Cunetas aquí
                pass
            elif i == 3:
                # Código de Drenaje aquí
                pass
            elif i == 4:
                # Código de Normativas Locales aquí
                pass
            elif i == 5:
                # Código de Caso Práctico San Miguel aquí
                pass
            elif i == 6:
                # Código de Análisis Avanzado aquí
                pass
        except Exception as e:
            st.error(f"❌ Error en la pestaña '{tab_labels[i]}': {str(e)}")

# --- LIMPIEZA DE FUNCIONES DUPLICADAS Y VARIABLES ---
# Elimina la función duplicada exportar_pdf_reportlab y usa solo una.
# Corrige el error de 'elementos' no definido en exportar_pdf_reportlab:
# Cambia 'elementos.append' por 'elements.append' en toda la función.
# Elimina cualquier código de columnas globales (col_izq, col_centro, col_der) fuera de las pestañas.
# Asegura que la selección de pestaña se pueda cambiar desde los botones de la barra superior.
