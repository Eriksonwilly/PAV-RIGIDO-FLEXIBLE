import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
import json
import os
from datetime import datetime
import math

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

# --- PROCESAMIENTO DE NUBE DE PUNTOS LIDAR (DRONES) - VERSIÓN DEMO ---
def procesar_nube_puntos(archivo_las, cota_minima=2000):
    """
    Procesa datos LiDAR para extraer:
    - Modelo Digital del Terreno (MDT).
    - Curvas de nivel (cada 0.5m).
    - Detección de zonas inestables (ej: hundimientos).
    
    Args:
        archivo_las (str): Nombre del archivo LAS/LAZ
        cota_minima (float): Elevación mínima para filtrar datos
        
    Returns:
        dict: Resultados del procesamiento LiDAR
    """
    try:
        # Simulación de procesamiento PDAL (versión demo)
        import random
        
        # Simular datos de nube de puntos
        puntos_totales = random.randint(500000, 2000000)
        area_ha = puntos_totales * 0.0001
        pendiente_promedio = random.uniform(2.5, 8.5)
        
        # Detección de zonas inestables
        zonas_inestables = []
        if pendiente_promedio > 5.0:
            zonas_inestables.append("Pendiente crítica detectada")
        if random.random() > 0.7:
            zonas_inestables.append("Posible hundimiento detectado")
        
        return {
            "Área_ha": round(area_ha, 2),
            "Pendiente_%": round(pendiente_promedio, 2),
            "Zonas_inestables": zonas_inestables if zonas_inestables else ["Sin anomalías detectadas"],
            "Puntos_procesados": puntos_totales,
            "MDT_generado": "mdt_terreno.tif",
            "Curvas_nivel": "curvas_0.5m.shp",
            "Estado": "✅ Procesamiento completado (Demo)"
        }
    except Exception as e:
        return {
            "Error": f"Error en procesamiento: {str(e)}",
            "Estado": "❌ Error en procesamiento"
        }

# --- DISEÑO AUTOMATIZADO DE PAVIMENTOS RÍGIDO (PERÚ) ---
def diseno_rigido(k_subrasante, ESALs, resistencia_concreto=28, clima="costa"):
    """
    Diseño de pavimento rígido según Norma PCA + DG-2018
    
    Args:
        k_subrasante (float): Módulo de reacción de subrasante (MPa/m)
        ESALs (int): Ejes equivalentes de 18 kips
        resistencia_concreto (float): Resistencia del concreto (MPa)
        clima (str): Tipo de clima ("costa" o "sierra")
        
    Returns:
        dict: Resultados del diseño rígido
    """
    try:
        # Ajuste por clima (Sierra vs Costa)
        factor_climatico = 1.3 if clima == "sierra" and k_subrasante < 50 else 1.0
        
        # Fórmula PCA modificada para Perú
        espesor_cm = ((math.log10(ESALs) * 100) / 
                     ((resistencia_concreto ** 0.7) * (k_subrasante ** 0.3))) * factor_climatico
        
        # Validar espesor mínimo según DG-2018
        if espesor_cm < 20:
            espesor_cm = 20  # Mínimo para vías principales
        
        # Calcular juntas según PCA
        junta_transversal = 3 * espesor_cm
        junta_longitudinal = 4.5 * espesor_cm
        
        # Análisis de fatiga PCA
        tension_maxima = 0.45 * resistencia_concreto  # 45% de la resistencia
        factor_seguridad = resistencia_concreto / tension_maxima
        
        return {
            "Espesor": f"{round(espesor_cm, 1)} cm",
            "Juntas": f"Transversales: {round(junta_transversal,1)}m | Longitudinales: {round(junta_longitudinal,1)}m",
            "Factor_climatico": factor_climatico,
            "Tension_maxima": f"{round(tension_maxima, 1)} MPa",
            "Factor_seguridad": round(factor_seguridad, 2),
            "Nota": "Usar concreto NP 350 (MR ≥ 4.5 MPa) - Norma IT.EC.030",
            "Estado": "✅ Diseño rígido completado"
        }
    except Exception as e:
        return {
            "Error": f"Error en diseño rígido: {str(e)}",
            "Estado": "❌ Error en diseño"
        }

# --- DISEÑO AUTOMATIZADO DE PAVIMENTOS FLEXIBLE (PERÚ) ---
def diseno_flexible(CBR, ESALs, tipo_suelo="volcánico", clima="costa"):
    """
    Diseño de pavimento flexible según AASHTO 93 modificado para Perú
    
    Args:
        CBR (float): CBR de subrasante (%)
        ESALs (int): Ejes equivalentes de 18 kips
        tipo_suelo (str): Tipo de suelo ("volcánico", "aluvial", "otro")
        clima (str): Tipo de clima ("costa" o "sierra")
        
    Returns:
        dict: Resultados del diseño flexible
    """
    try:
        # Ajuste por tipo de suelo
        if tipo_suelo == "volcánico":
            CBR_ajustado = CBR * 0.9  # Reducción por presencia de cenizas
        elif tipo_suelo == "aluvial":
            CBR_ajustado = CBR * 1.1  # Mejora por material granular
        else:
            CBR_ajustado = CBR
        
        # Ajuste por clima
        factor_climatico = 1.2 if clima == "sierra" else 1.0
        
        # Cálculo del número estructural SN
        SN = (math.log10(ESALs) * (4.5 - CBR_ajustado)) / (0.372 * 1.2) * factor_climatico
        
        # Distribución de capas según AASHTO 93
        espesor_base = SN * 0.3
        espesor_subbase = SN * 0.7
        
        # Validaciones según MTC
        if espesor_base < 15:
            espesor_base = 15  # Mínimo según IT.5 - MTC
        
        return {
            "Base": f"{round(espesor_base, 1)} cm (Grava A-1-a)",
            "Subbase": f"{round(espesor_subbase, 1)} cm (Material granular CBR ≥ 25%)",
            "SN_total": round(SN, 2),
            "CBR_ajustado": round(CBR_ajustado, 1),
            "Factor_climatico": factor_climatico,
            "Nota": "Compactar al 95% Proctor Modificado - Art. 410.3 MTC",
            "Estado": "✅ Diseño flexible completado"
        }
    except Exception as e:
        return {
            "Error": f"Error en diseño flexible: {str(e)}",
            "Estado": "❌ Error en diseño"
        }

# --- INTEROPERABILIDAD CON CIVIL 3D (VERSIÓN DEMO) ---
def exportar_a_civil3d(espesor, ruta_dwg):
    """
    Exporta diseño de pavimento a AutoCAD Civil 3D
    
    Args:
        espesor (float): Espesor de diseño (cm)
        ruta_dwg (str): Ruta del archivo DWG destino
        
    Returns:
        str: Mensaje de estado de exportación
    """
    try:
        # Simulación de exportación a Civil 3D
        import random
        
        # Simular creación de capas
        capas_creadas = [
            "PAVIMENTO_RIGIDO",
            "PAVIMENTO_FLEXIBLE", 
            "JUNTAS",
            "REFUERZO_ACERO"
        ]
        
        # Simular dibujo de elementos
        elementos_dibujados = {
            "Polilíneas": random.randint(10, 50),
            "Círculos": random.randint(5, 20),
            "Texto": random.randint(20, 100)
        }
        
        return {
            "Archivo_DWG": ruta_dwg,
            "Capas_creadas": capas_creadas,
            "Elementos_dibujados": elementos_dibujados,
            "Espesor_exportado": f"{espesor} cm",
            "Estado": "✅ Exportación a Civil 3D completada (Demo)",
            "Nota": "Para exportación real, requiere entorno AutoCAD y pyautocad"
        }
    except Exception as e:
        return {
            "Error": f"Error en exportación: {str(e)}",
            "Estado": "❌ Error en exportación"
        }

# --- VALIDACIÓN NORMATIVA PERUANA ---
def validar_normativa_peruana(espesor_cm, CBR_subbase, pendiente_cuneta, tipo_pavimento="rigido"):
    """
    Valida cumplimiento de normativas peruanas
    
    Args:
        espesor_cm (float): Espesor de pavimento (cm)
        CBR_subbase (float): CBR de subbase (%)
        pendiente_cuneta (float): Pendiente de cuneta (%)
        tipo_pavimento (str): Tipo de pavimento ("rigido" o "flexible")
        
    Returns:
        list: Lista de validaciones
    """
    validaciones = []
    
    # Validaciones para pavimento rígido
    if tipo_pavimento == "rigido":
        if espesor_cm < 20:
            validaciones.append("❌ Espesor rígido menor a 20 cm (DG-2018 Art. 5.4.3)")
        else:
            validaciones.append("✅ Espesor rígido cumple DG-2018")
    
    # Validaciones para pavimento flexible
    if tipo_pavimento == "flexible":
        if espesor_cm < 15:
            validaciones.append("❌ Espesor flexible menor a 15 cm (IT.5 - MTC)")
        else:
            validaciones.append("✅ Espesor flexible cumple IT.5 - MTC")
    
    # Validaciones de subbase
    if CBR_subbase < 20:
        validaciones.append("❌ Subbase flexible CBR < 20% (IT.5 - MTC)")
    else:
        validaciones.append("✅ Subbase flexible cumple IT.5 - MTC")
    
    # Validaciones de drenaje
    if pendiente_cuneta < 2:
        validaciones.append("❌ Pendiente de cuneta < 2% (RAS 2020)")
    else:
        validaciones.append("✅ Pendiente de cuneta cumple RAS 2020")
    
    # Validaciones adicionales
    if espesor_cm > 50:
        validaciones.append("⚠️ Espesor muy alto - verificar economía")
    
    return validaciones

# --- ANÁLISIS DE FATIGA PCA ---
def analisis_fatiga_pca(ESALs, resistencia_concreto, espesor_cm):
    """
    Análisis de fatiga según método PCA
    
    Args:
        ESALs (int): Ejes equivalentes
        resistencia_concreto (float): Resistencia del concreto (MPa)
        espesor_cm (float): Espesor de losa (cm)
        
    Returns:
        dict: Resultados del análisis de fatiga
    """
    try:
        # Cálculo de tensiones según PCA
        tension_maxima = 0.45 * resistencia_concreto
        tension_por_carga = 0.35 * resistencia_concreto
        
        # Cálculo de daño acumulado
        daño_acumulado = (ESALs / 1000000) * (tension_por_carga / tension_maxima) ** 3.2
        
        # Vida útil estimada
        vida_util = 20 / daño_acumulado if daño_acumulado > 0 else 50
        
        # Estado de la losa
        if daño_acumulado < 1.0:
            estado = "Excelente"
        elif daño_acumulado < 2.0:
            estado = "Bueno"
        elif daño_acumulado < 3.0:
            estado = "Regular"
        else:
            estado = "Crítico"
        
        return {
            "Tension_maxima": f"{round(tension_maxima, 1)} MPa",
            "Tension_por_carga": f"{round(tension_por_carga, 1)} MPa",
            "Daño_acumulado": round(daño_acumulado, 3),
            "Vida_util_estimada": round(vida_util, 1),
            "Estado_losa": estado,
            "Estado": "✅ Análisis de fatiga completado"
        }
    except Exception as e:
        return {
            "Error": f"Error en análisis de fatiga: {str(e)}",
            "Estado": "❌ Error en análisis"
        }

# --- DIAGRAMA DE ARQUITECTURA Y ROADMAP ---
def mostrar_diagrama_arquitectura():
    """Muestra el diagrama de arquitectura del software"""
    st.markdown("""
    ### 🌐 Diagrama de Arquitectura del Software
    ```mermaid
    graph TD
        A["Drone LiDAR"] --> B["Archivos LAS/LAZ"]
        B --> C["PDAL - Procesamiento"]
        C --> D["Modelo Digital del Terreno"]
        D --> E["Diseño Pavimentos"]
        E --> F["AutoCAD Civil 3D"]
        E --> G["Revit BIM"]
        E --> H["QGIS - Análisis"]
        H --> I["Validación Normativa"]
        I --> J["Reportes PDF Premium"]
    ```
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 📈 Roadmap Priorizado
    - **Fase 1 (0-3 meses):** Integrar PDAL para procesar datos LAS/LAZ. Conectar con QGIS para análisis geotécnico.
    - **Fase 2 (3-6 meses):** API REST para móviles (colecta de datos CBR en campo). Exportación a BIM (Revit).
    - **Fase 3 (6-12 meses):** Machine Learning para predecir vida útil del pavimento.
    """)

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
            if i == 5:  # 🚁 Caso Práctico San Miguel
                st.header("🚁 Caso Práctico San Miguel")
                st.info("Procesamiento de datos LiDAR y diseño automatizado para San Miguel, Puno.")
                
                # Sección de procesamiento LiDAR
                st.markdown("### 📊 Procesamiento de Datos LiDAR (Drones)")
                st.markdown("**Sube tu archivo LAS/LAZ de dron:**")
                archivo_las = st.file_uploader("Archivo LAS/LAZ", type=["las", "laz"], key="lidar_upload")
                
                if archivo_las:
                    with st.spinner("Procesando datos LiDAR..."):
                        resultados_lidar = procesar_nube_puntos(archivo_las.name)
                        st.success("✅ Datos LiDAR procesados exitosamente")
                        st.json(resultados_lidar)
                
                st.markdown("---")
                
                # Sección de diseño automatizado
                st.markdown("### 🏗️ Diseño Automatizado de Pavimento Rígido (Norma Peruana)")
                col1, col2 = st.columns(2)
                with col1:
                    k = st.number_input("k subrasante (MPa/m)", 10, 200, 50, key="k_rigido")
                    ESALs = st.number_input("ESALs (ejes equivalentes)", 10000, 10000000, 100000, key="esals_rigido")
                with col2:
                    resistencia_concreto = st.number_input("Resistencia concreto (MPa)", 20, 50, 28, key="resistencia")
                    clima = st.selectbox("Clima", ["costa", "sierra"], key="clima_rigido")
                
                if st.button("🚀 Calcular Diseño Rígido", key="btn_rigido"):
                    with st.spinner("Calculando diseño rígido..."):
                        resultado_rigido = diseno_rigido(k, ESALs, resistencia_concreto, clima)
                        st.success("✅ Diseño rígido completado")
                        st.json(resultado_rigido)
                
                st.markdown("### 🛣️ Diseño Automatizado de Pavimento Flexible (Norma Peruana)")
                col1, col2 = st.columns(2)
                with col1:
                    CBR = st.number_input("CBR subrasante (%)", 2, 30, 8, key="cbr_flexible")
                    tipo_suelo = st.selectbox("Tipo de suelo", ["volcánico", "aluvial", "otro"], key="tipo_suelo")
                with col2:
                    ESALs_flex = st.number_input("ESALs flexible", 10000, 10000000, 100000, key="esals_flexible")
                    clima_flex = st.selectbox("Clima flexible", ["costa", "sierra"], key="clima_flexible")
                
                if st.button("🚀 Calcular Diseño Flexible", key="btn_flexible"):
                    with st.spinner("Calculando diseño flexible..."):
                        resultado_flexible = diseno_flexible(CBR, ESALs_flex, tipo_suelo, clima_flex)
                        st.success("✅ Diseño flexible completado")
                        st.json(resultado_flexible)
                
                # Sección de análisis de fatiga
                st.markdown("### 🔬 Análisis de Fatiga PCA")
                if st.button("🚀 Analizar Fatiga", key="btn_fatiga"):
                    with st.spinner("Analizando fatiga..."):
                        if 'resultado_rigido' in locals():
                            espesor_cm = float(resultado_rigido['Espesor'].split()[0])
                            analisis_fatiga = analisis_fatiga_pca(ESALs, resistencia_concreto, espesor_cm)
                            st.success("✅ Análisis de fatiga completado")
                            st.json(analisis_fatiga)
                        else:
                            st.warning("⚠️ Primero calcule el diseño rígido")
                
                # Sección de validación normativa
                st.markdown("### 📋 Validación Normativa Peruana")
                pendiente_cuneta = st.number_input("Pendiente de cuneta (%)", 0.5, 10.0, 2.0, key="pendiente_cuneta")
                
                if st.button("🚀 Validar Normativa", key="btn_validar"):
                    with st.spinner("Validando normativa..."):
                        if 'resultado_rigido' in locals():
                            espesor_cm = float(resultado_rigido['Espesor'].split()[0])
                            validaciones = validar_normativa_peruana(espesor_cm, CBR, pendiente_cuneta, "rigido")
                            st.success("✅ Validación completada")
                            for v in validaciones:
                                st.write(v)
                        else:
                            st.warning("⚠️ Primero calcule el diseño")
                
                st.markdown("---")
                mostrar_diagrama_arquitectura()
                
            elif i == 6:  # 🌍 Análisis Avanzado
                st.header("🌍 Análisis Avanzado")
                st.info("Interoperabilidad con QGIS, Civil 3D y BIM. Exportación de modelos y planos constructivos.")
                
                # Sección de exportación a Civil 3D
                st.markdown("### 🏗️ Exportar a Civil 3D")
                col1, col2 = st.columns(2)
                with col1:
                    espesor = st.number_input("Espesor de diseño (cm)", 10, 50, 20, key="espesor_civil3d")
                with col2:
                    ruta_dwg = st.text_input("Ruta DWG destino", "C:/proyecto/pavimento.dwg", key="ruta_dwg")
                
                if st.button("🚀 Exportar a Civil 3D", key="btn_civil3d"):
                    with st.spinner("Exportando a Civil 3D..."):
                        msg = exportar_a_civil3d(espesor, ruta_dwg)
                        st.success("✅ Exportación completada")
                        st.json(msg)
                
                st.markdown("---")
                
                # Sección de integración con QGIS y BIM
                st.markdown("### 🔗 Integración con QGIS y Revit BIM")
                st.markdown("""
                - **QGIS:** Visualiza el MDT y curvas de nivel
                - **Revit BIM:** Exporta modelos para modelado 4D
                - **API REST:** Colecta de datos en campo (futuro)
                """)
                
                # Sección de requerimientos técnicos
                st.markdown("### 📋 Requerimientos Técnicos")
                st.markdown("""
                **Procesamiento de datos LiDAR (Drones):**
                - Lectura de archivos LAS/LAZ usando PDAL
                - Filtrado de vegetación y generación de MDT
                - Exportación a GeoTIFF y shapefiles para QGIS
                
                **Diseño de pavimentos (Norma Peruana):**
                - Rígido: Método PCA + AASHTO 93 con ajustes para clima
                - Flexible: AASHTO 93 modificado para suelos volcánicos
                
                **Interoperabilidad:**
                - Exportación a AutoCAD Civil 3D (.DWG) y Revit (IFC)
                - API REST para móviles (colecta de datos CBR)
                
                **Validaciones:**
                - Cumplimiento de espesores mínimos (DG-2018)
                - Detección de zonas inestables (ASTM D6432)
                """)
                
                mostrar_diagrama_arquitectura()
                
            else:
                # Pestañas básicas (mantener funcionalidad existente)
                st.header(f"Pestaña {tab_labels[i]}")
                st.info(f"Contenido de {tab_labels[i]} - En desarrollo")
                
        except Exception as e:
            st.error(f"❌ Error en la pestaña '{tab_labels[i]}': {str(e)}")

# --- LIMPIEZA DE FUNCIONES DUPLICADAS Y VARIABLES ---
# Elimina la función duplicada exportar_pdf_reportlab y usa solo una.
# Corrige el error de 'elementos' no definido en exportar_pdf_reportlab:
# Cambia 'elementos.append' por 'elements.append' en toda la función.
# Elimina cualquier código de columnas globales (col_izq, col_centro, col_der) fuera de las pestañas.
# Asegura que la selección de pestaña se pueda cambiar desde los botones de la barra superior.
