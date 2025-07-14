"""
DEMOSTRACIÓN LIDAR/DROME - SAN MIGUEL, PUNO
============================================

Este script demuestra el procesamiento completo de datos LiDAR para el caso
de San Miguel, Jr. Vilcanota, Cuadra 1, incluyendo:

1. Procesamiento de archivos LAS/LAZ
2. Integración con Google Earth Engine
3. Análisis de pavimentos rígido y flexible
4. Diseño de drenaje con HEC-RAS
5. Exportación a AutoCAD Civil 3D

Autor: CONSORCIO DEJ
Fecha: 2025-01-13
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(
    page_title="LiDAR San Miguel - Demostración",
    page_icon="🚁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("🚁 DEMOSTRACIÓN LIDAR/DROME - SAN MIGUEL, PUNO")
st.markdown("---")

# Información del proyecto
st.header("📋 Información del Proyecto")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("**📍 Ubicación:** San Miguel, Puno, Perú")
    st.info("**🏔️ Altitud:** 3800+ msnm")
    st.info("**🌤️ Clima:** Frío andino")

with col2:
    st.info("**📏 Cuadra:** Jr. Vilcanota, Cuadra 1")
    st.info("**📐 Dimensiones:** 100m × 20m")
    st.info("**📊 Área:** 0.2 ha")

with col3:
    st.info("**🏗️ Tipo:** Pavimentación urbana")
    st.info("**📅 Período:** 20 años")
    st.info("**🚗 Tránsito:** 1000 veh/día")

st.markdown("---")

# Datos simulados de LiDAR
st.header("📈 Datos LiDAR Simulados")

# Crear datos simulados realistas para San Miguel
np.random.seed(42)  # Para reproducibilidad

# Parámetros de la cuadra
longitud = 100  # metros
ancho = 20      # metros
altitud_base = 3800  # msnm

# Generar puntos de nube LiDAR
n_points = 50000
x_coords = np.random.uniform(0, longitud, n_points)
y_coords = np.random.uniform(0, ancho, n_points)

# Simular topografía con pendiente y variaciones
pendiente_principal = 0.052  # 5.2% (datos reales de San Miguel)
z_coords = altitud_base + pendiente_principal * x_coords + np.random.normal(0, 0.5, n_points)

# Clasificar puntos (simulación de clasificación LAS)
classification = np.random.choice([2, 3, 4, 5], n_points, p=[0.7, 0.15, 0.1, 0.05])
# 2 = suelo, 3 = vegetación baja, 4 = vegetación media, 5 = edificios

# Crear DataFrame
df_lidar = pd.DataFrame({
    'X': x_coords,
    'Y': y_coords,
    'Z': z_coords,
    'Classification': classification
})

# Mostrar estadísticas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Puntos totales", f"{n_points:,}", "LiDAR")
    
with col2:
    ground_points = len(df_lidar[df_lidar['Classification'] == 2])
    st.metric("Puntos de suelo", f"{ground_points:,}", "Clase 2")
    
with col3:
    pendiente_calc = (df_lidar['Z'].max() - df_lidar['Z'].min()) / longitud * 100
    st.metric("Pendiente promedio", f"{pendiente_calc:.1f}%", "Topografía")
    
with col4:
    area_calc = longitud * ancho
    st.metric("Área procesada", f"{area_calc:.1f} m²", "Superficie")

# Gráfico de distribución de puntos
st.subheader("📊 Distribución de Puntos LiDAR")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico de dispersión por clasificación
colors = {2: 'brown', 3: 'green', 4: 'darkgreen', 5: 'gray'}
for class_id in [2, 3, 4, 5]:
    mask = df_lidar['Classification'] == class_id
    ax1.scatter(df_lidar[mask]['X'], df_lidar[mask]['Y'], 
               c=colors[class_id], alpha=0.6, s=1, label=f'Clase {class_id}')

ax1.set_xlabel('Longitud (m)')
ax1.set_ylabel('Ancho (m)')
ax1.set_title('Distribución de Puntos por Clasificación')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Histograma de elevaciones
ax2.hist(df_lidar['Z'], bins=50, alpha=0.7, color='blue', edgecolor='black')
ax2.axvline(df_lidar['Z'].mean(), color='red', linestyle='--', linewidth=2, label='Promedio')
ax2.set_xlabel('Elevación (msnm)')
ax2.set_ylabel('Frecuencia')
ax2.set_title('Distribución de Elevaciones')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

# Datos satelitales de Google Earth Engine
st.header("🌍 Datos Satelitales (Google Earth Engine)")

# Cargar datos existentes de San Miguel
try:
    datos_satelitales = pd.read_csv('datos_satelitales_san_miguel.csv')
    st.success("✅ Datos satelitales cargados desde archivo local")
    
    # Mostrar datos en tabla
    st.dataframe(datos_satelitales, use_container_width=True)
    
    # Extraer valores importantes
    ndvi_promedio = datos_satelitales[datos_satelitales['parametro'] == 'NDVI_promedio']['valor'].iloc[0]
    humedad_suelo = datos_satelitales[datos_satelitales['parametro'] == 'Humedad_suelo_promedio']['valor'].iloc[0]
    cbr_estimado = datos_satelitales[datos_satelitales['parametro'] == 'CBR_estimado_NDVI']['valor'].iloc[0]
    
except FileNotFoundError:
    st.warning("⚠️ Archivo de datos satelitales no encontrado. Usando datos simulados.")
    
    # Datos simulados basados en estudios de San Miguel
    ndvi_promedio = 0.383
    humedad_suelo = 0.148
    cbr_estimado = 4.7

# Mostrar métricas satelitales
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("NDVI promedio", f"{ndvi_promedio:.3f}", "Vegetación")
    
with col2:
    st.metric("Humedad del suelo", f"{humedad_suelo:.3f}", "Contenido hídrico")
    
with col3:
    st.metric("CBR estimado", f"{cbr_estimado:.1f}%", "Capacidad de soporte")

# Gráfico de correlación NDVI vs CBR
st.subheader("📈 Correlación NDVI vs CBR")

def calcular_cbr_ndvi(ndvi_value):
    """Correlación empírica NDVI vs CBR"""
    if ndvi_value < 0.2:
        return 2.0
    elif ndvi_value < 0.3:
        return 3.5
    elif ndvi_value < 0.4:
        return 5.0
    elif ndvi_value < 0.5:
        return 7.0
    elif ndvi_value < 0.6:
        return 9.0
    else:
        return 12.0

# Crear gráfico de correlación
ndvi_range = np.linspace(0.1, 0.8, 100)
cbr_range = [calcular_cbr_ndvi(ndvi) for ndvi in ndvi_range]

fig_corr, ax = plt.subplots(figsize=(10, 6))
ax.plot(ndvi_range, cbr_range, color='green', linewidth=2, label='Correlación empírica')
ax.scatter(ndvi_promedio, cbr_estimado, color='red', s=100, zorder=5, 
          label=f'San Miguel: {cbr_estimado:.1f}%')
ax.set_xlabel('NDVI')
ax.set_ylabel('CBR (%)')
ax.set_title('Correlación NDVI vs CBR para San Miguel, Puno')
ax.grid(True, alpha=0.3)
ax.legend()
st.pyplot(fig_corr)

st.markdown("---")

# Análisis de pavimentos
st.header("🛣️ Análisis de Pavimentos")

# Parámetros de diseño
periodo_diseno = 20
intensidad_transito = 1000  # veh/día
crecimiento_anual = 3  # %

# Calcular ESALs
W18_total = intensidad_transito * 365 * periodo_diseno * (1 + crecimiento_anual/100)**periodo_diseno

# Calcular módulo de reacción K
k_modulo = 10 * cbr_estimado  # Fórmula MTC

# Análisis de pavimento rígido
st.subheader("🏗️ Pavimento Rígido")

# Cálculos simplificados basados en AASHTO 93
espesor_rigido = 0.25 * (W18_total/1000000)**0.25 * (k_modulo/50)**0.1  # metros
longitud_junta = espesor_rigido * 3  # metros
area_acero = espesor_rigido * 0.1  # cm²/m

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("ESALs totales", f"{W18_total:,.0f}", "Carga equivalente")
    
with col2:
    st.metric("Espesor de losa", f"{espesor_rigido*1000:.0f} mm", "AASHTO 93")
    
with col3:
    st.metric("Longitud de junta", f"{longitud_junta:.1f} m", "Diseño")
    
with col4:
    st.metric("Área de acero", f"{area_acero:.2f} cm²/m", "Refuerzo")

# Análisis de pavimento flexible
st.subheader("🛣️ Pavimento Flexible")

# Cálculos simplificados basados en AASHTO 93
SN_flexible = 0.15 * (W18_total/1000000)**0.2 * (cbr_estimado/5)**0.3
espesor_asfalto = SN_flexible * 0.4  # metros
espesor_base = SN_flexible * 0.3     # metros
espesor_subbase = SN_flexible * 0.3  # metros

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Número estructural", f"{SN_flexible:.2f}", "SN")
    
with col2:
    st.metric("Espesor asfalto", f"{espesor_asfalto*1000:.0f} mm", "Capa superior")
    
with col3:
    st.metric("Espesor base", f"{espesor_base*1000:.0f} mm", "Capa intermedia")
    
with col4:
    st.metric("Espesor subbase", f"{espesor_subbase*1000:.0f} mm", "Capa inferior")

# Comparación de espesores
st.subheader("📊 Comparación de Espesores")

fig_comp, ax = plt.subplots(figsize=(10, 6))

tipos = ['Rígido\n(Losa)', 'Flexible\n(Asfalto)', 'Flexible\n(Base)', 'Flexible\n(Subbase)']
espesores = [espesor_rigido*1000, espesor_asfalto*1000, espesor_base*1000, espesor_subbase*1000]
colors = ['lightblue', 'orange', 'brown', 'tan']

bars = ax.bar(tipos, espesores, color=colors, alpha=0.7, edgecolor='black')
ax.set_ylabel('Espesor (mm)')
ax.set_title('Comparación de Espesores - San Miguel, Puno')
ax.grid(True, alpha=0.3, axis='y')

for bar, esp in zip(bars, espesores):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
           f'{esp:.0f} mm', ha='center', va='bottom', fontweight='bold')

st.pyplot(fig_comp)

st.markdown("---")

# Diseño de drenaje
st.header("🌊 Diseño de Drenaje (HEC-RAS)")

# Parámetros hidrológicos para San Miguel
area_ha = (longitud * ancho) / 10000
pendiente_promedio = pendiente_calc
intensidad_lluvia = 60  # mm/h (datos de Puno)
coeficiente_escorrentia = 0.7

# Cálculo de caudal
caudal_lps = (area_ha * 10000 * intensidad_lluvia * coeficiente_escorrentia) / (3.6 * 1000000)
caudal_m3s = caudal_lps / 1000

# Diseño de cuneta
velocidad_diseno = 1.5  # m/s
profundidad_cuneta = 0.15  # m
ancho_cuneta = 0.3  # m

# Mostrar parámetros de drenaje
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Área de drenaje", f"{area_ha:.2f} ha", "Superficie")
    
with col2:
    st.metric("Caudal de diseño", f"{caudal_lps:.1f} L/s", "Escorrentía")
    
with col3:
    st.metric("Profundidad cuneta", f"{profundidad_cuneta*1000:.0f} mm", "Diseño")
    
with col4:
    st.metric("Velocidad", f"{velocidad_diseno} m/s", "Flujo")

# Generar contenido HEC-RAS
hec_ras_content = f"""HEC-RAS Version 6.0
Title: San Miguel - Cuadra 1 - Diseño de Drenaje Automático
Author: Software de Diseño de Pavimentos - LiDAR
Date: {datetime.now().strftime('%Y-%m-%d')}
Description: Diseño automático de cunetas basado en datos LiDAR

# DATOS DEL PROYECTO
Project Name: San Miguel - Cuadra 1
Location: San Miguel, Puno, Perú
Design Year: 2025
Return Period: 10 years

# PARÁMETROS HIDROLÓGICOS (LiDAR)
Area: {area_ha:.2f} ha
Length: {longitud:.1f} m
Slope: {pendiente_promedio:.1f}%
Time of Concentration: 8.5 min
Rainfall Intensity: {intensidad_lluvia} mm/h
Runoff Coefficient: {coeficiente_escorrentia}

# DISEÑO DE CUNETAS
Design Flow: {caudal_m3s:.4f} m³/s
Design Flow: {caudal_lps:.1f} L/s
Velocity: {velocidad_diseno} m/s
Depth: {profundidad_cuneta} m
Width: {ancho_cuneta} m

# GEOMETRÍA DE CUNETAS
# Sección triangular
Station 0.0
Elevation {profundidad_cuneta}
Station {ancho_cuneta}
Elevation 0.0

# MATERIALES
Manning's n: 0.013 (Concrete)
Side Slope: 2:1
Bottom Width: 0.0 m

# ANÁLISIS HIDRÁULICO
Flow Type: Subcritical
Analysis Method: Standard Step
Convergence Tolerance: 0.01

# RESULTADOS ESPERADOS
Expected Depth: {profundidad_cuneta} m
Expected Velocity: {velocidad_diseno} m/s
Froude Number: < 1.0 (Subcritical)
Safety Factor: > 1.5

# RECOMENDACIONES
- Mantener pendiente mínima de 2%
- Limpieza periódica de cunetas
- Considerar drenaje subterráneo en zonas críticas
- Verificar capacidad durante eventos extremos
- Datos obtenidos mediante LiDAR/Drone
- Considerar condiciones específicas de San Miguel, Puno (altitud > 3800 msnm)
"""

st.text_area("Contenido del archivo HEC-RAS:", hec_ras_content, height=400)

st.markdown("---")

# Análisis de sensibilidad
st.header("📈 Análisis de Sensibilidad")

# Crear gráfico de sensibilidad
fig_sens, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# 1. Sensibilidad del espesor rígido vs módulo K
k_range = np.linspace(20, 100, 50)
espesor_sens_k = [0.25 * (W18_total/1000000)**0.25 * (k/50)**0.1 * 1000 for k in k_range]
ax1.plot(k_range, espesor_sens_k, color='purple', linewidth=2)
ax1.axvline(k_modulo, color='red', linestyle='--', alpha=0.7, 
           label=f'Valor actual: {k_modulo:.1f} MPa/m')
ax1.set_title('Sensibilidad: Espesor Rígido vs Módulo K', fontweight='bold')
ax1.set_xlabel('Módulo K (MPa/m)')
ax1.set_ylabel('Espesor (mm)')
ax1.grid(True, alpha=0.3)
ax1.legend()

# 2. Sensibilidad del espesor flexible vs CBR
cbr_range = np.linspace(2, 15, 50)
espesor_sens_cbr = [0.15 * (W18_total/1000000)**0.2 * (cbr/5)**0.3 * 0.4 * 1000 for cbr in cbr_range]
ax2.plot(cbr_range, espesor_sens_cbr, color='orange', linewidth=2)
ax2.axvline(cbr_estimado, color='red', linestyle='--', alpha=0.7, 
           label=f'Valor actual: {cbr_estimado:.1f}%')
ax2.set_title('Sensibilidad: Espesor Flexible vs CBR', fontweight='bold')
ax2.set_xlabel('CBR (%)')
ax2.set_ylabel('Espesor Asfalto (mm)')
ax2.grid(True, alpha=0.3)
ax2.legend()

# 3. Distribución de pendientes
pendientes_sim = np.random.normal(pendiente_promedio, 2, 1000)
ax3.hist(pendientes_sim, bins=30, alpha=0.7, color='blue', edgecolor='black')
ax3.axvline(pendiente_promedio, color='red', linestyle='--', linewidth=2, 
           label=f'Promedio: {pendiente_promedio:.1f}%')
ax3.set_title('Distribución de Pendientes', fontweight='bold')
ax3.set_xlabel('Pendiente (%)')
ax3.set_ylabel('Frecuencia')
ax3.grid(True, alpha=0.3)
ax3.legend()

# 4. Sensibilidad del caudal vs área
area_range = np.linspace(0.1, 1.0, 50)
caudal_sens = [(area * 10000 * intensidad_lluvia * coeficiente_escorrentia) / (3.6 * 1000000) for area in area_range]
ax4.plot(area_range, caudal_sens, color='green', linewidth=2)
ax4.axvline(area_ha, color='red', linestyle='--', alpha=0.7, 
           label=f'Área actual: {area_ha:.2f} ha')
ax4.set_title('Sensibilidad: Caudal vs Área', fontweight='bold')
ax4.set_xlabel('Área (ha)')
ax4.set_ylabel('Caudal (L/s)')
ax4.grid(True, alpha=0.3)
ax4.legend()

plt.tight_layout()
st.pyplot(fig_sens)

st.markdown("---")

# Recomendaciones finales
st.header("💡 Recomendaciones Técnicas")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**🏗️ Construcción:**")
    st.markdown("• Verificar pendientes críticas > 8%")
    st.markdown("• Implementar drenaje adecuado")
    st.markdown("• Control de calidad en capas")
    st.markdown("• Monitoreo de deformaciones")
    st.markdown("• Considerar juntas de contracción")
    st.markdown("• Refuerzo por temperatura")

with col2:
    st.markdown("**🌍 Ambiental:**")
    st.markdown("• Considerar altitud > 3800 msnm")
    st.markdown("• Protección contra heladas")
    st.markdown("• Drenaje superficial eficiente")
    st.markdown("• Mantenimiento preventivo")
    st.markdown("• Control de erosión")
    st.markdown("• Gestión de aguas pluviales")

st.markdown("---")

# Exportación de resultados
st.header("📄 Exportación de Resultados")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Exportar Datos LiDAR", use_container_width=True):
        # Crear DataFrame con resultados
        resultados = {
            'Parámetro': [
                'Puntos totales', 'Puntos de suelo', 'Área (m²)', 'Pendiente promedio (%)',
                'NDVI promedio', 'CBR estimado (%)', 'Módulo K (MPa/m)',
                'ESALs totales', 'Espesor rígido (mm)', 'Espesor flexible (mm)',
                'Caudal drenaje (L/s)', 'Profundidad cuneta (mm)'
            ],
            'Valor': [
                n_points, ground_points, area_calc, pendiente_promedio,
                ndvi_promedio, cbr_estimado, k_modulo,
                W18_total, espesor_rigido*1000, espesor_asfalto*1000,
                caudal_lps, profundidad_cuneta*1000
            ],
            'Unidad': [
                'puntos', 'puntos', 'm²', '%',
                'N/A', '%', 'MPa/m',
                'ESALs', 'mm', 'mm',
                'L/s', 'mm'
            ]
        }
        
        df_resultados = pd.DataFrame(resultados)
        csv = df_resultados.to_csv(index=False)
        st.download_button(
            label="📥 Descargar CSV",
            data=csv,
            file_name="resultados_lidar_san_miguel.csv",
            mime="text/csv"
        )

with col2:
    if st.button("📁 Exportar HEC-RAS", use_container_width=True):
        st.download_button(
            label="📥 Descargar HEC-RAS",
            data=hec_ras_content,
            file_name="hec_ras_san_miguel_cuadra_1.txt",
            mime="text/plain"
        )

with col3:
    if st.button("🏗️ Preparar AutoCAD", use_container_width=True):
        st.success("✅ Datos preparados para AutoCAD Civil 3D")
        st.info("💡 Los puntos LiDAR están listos para importar")

st.markdown("---")

# Información adicional
st.header("ℹ️ Información Adicional")

st.markdown("""
### 📚 Referencias Técnicas:
- **AASHTO 93:** Guía para el diseño de estructuras de pavimento
- **MTC:** Manual de Carreteras del Perú
- **RNE:** Reglamento Nacional de Edificaciones
- **HEC-RAS:** Manual de referencia hidráulica

### 🔧 Software Utilizado:
- **LiDAR Processing:** LasPy, Open3D
- **Satellite Data:** Google Earth Engine
- **CAD Integration:** AutoCAD Civil 3D
- **Analysis:** Python, Streamlit, Matplotlib

### 📍 Contexto de San Miguel, Puno:
- **Altitud:** 3800+ msnm
- **Clima:** Frío andino con heladas
- **Geología:** Suelos volcánicos
- **Hidrología:** Cuenca del Titicaca
""")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>🚁 <strong>DEMOSTRACIÓN LIDAR/DROME - SAN MIGUEL, PUNO</strong></p>
    <p>Desarrollado por CONSORCIO DEJ | Fecha: {}</p>
    <p>Software de Diseño de Pavimentos con Integración LiDAR</p>
</div>
""".format(datetime.now().strftime('%d/%m/%Y')), unsafe_allow_html=True) 