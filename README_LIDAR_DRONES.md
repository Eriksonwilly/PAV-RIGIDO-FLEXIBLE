# 🚁 MÓDULO LIDAR/DRONES - CONSORCIO DEJ

## 📋 Descripción

El módulo LiDAR/Drones es una funcionalidad avanzada que integra el procesamiento de datos de drones (LiDAR/LAS/LAZ) con el software de diseño de pavimentos, permitiendo:

- **Procesamiento de nubes de puntos** de drones LiDAR
- **Integración con Google Earth Engine** para datos satelitales
- **Análisis automático de pavimentos** rígido y flexible
- **Diseño de drenaje** con HEC-RAS
- **Exportación a AutoCAD Civil 3D**

## 🎯 Caso de Estudio: San Miguel, Puno

### 📍 Ubicación
- **Distrito:** San Miguel, Puno, Perú
- **Cuadra:** Jr. Vilcanota, Cuadra 1
- **Dimensiones:** 100m × 20m (0.2 ha)
- **Altitud:** 3800+ msnm

### 🏗️ Características del Proyecto
- **Tipo:** Pavimentación urbana
- **Período de diseño:** 20 años
- **Intensidad de tránsito:** 1000 veh/día
- **Crecimiento anual:** 3%

## 🛠️ Funcionalidades Principales

### 1. 📁 Procesamiento de Archivos LAS/LAZ
```python
def procesar_archivo_las_laz(file_path, output_dir="output_lidar"):
    """
    Procesa archivos LAS/LAZ de drones para extraer información topográfica
    """
```

**Características:**
- Lectura de archivos LAS/LAZ con LasPy
- Clasificación automática de puntos (suelo, vegetación, edificios)
- Generación de MDT (Modelo Digital de Terreno)
- Cálculo de pendientes y curvas de nivel
- Exportación a formatos estándar

### 2. 🌍 Integración Google Earth Engine
```python
def extraer_datos_satelitales_gee(coords, start_date, end_date):
    """
    Extrae datos satelitales de Google Earth Engine para análisis de suelo
    """
```

**Datos obtenidos:**
- **NDVI (Índice de Vegetación):** Sentinel-2
- **Humedad del suelo:** SMAP (NASA)
- **Correlación NDVI vs CBR** para estimación de capacidad de soporte
- **Análisis temporal** de condiciones del suelo

### 3. 🛣️ Análisis Automático de Pavimentos

#### Pavimento Rígido
- **Fórmula AASHTO 93** para cálculo de espesor
- **Análisis de fatiga y erosión** (PCA)
- **Diseño de juntas** y refuerzo por temperatura
- **Cálculo de ESALs** basado en tránsito

#### Pavimento Flexible
- **Número estructural** según AASHTO 93
- **Diseño de capas** (asfalto, base, subbase)
- **Análisis de fatiga MEPDG**
- **Optimización de espesores**

### 4. 🌊 Diseño de Drenaje (HEC-RAS)
```python
def generar_hec_ras_drenaje(area_ha, longitud_m, pendiente_pct, periodo_retorno=10):
    """
    Genera archivo HEC-RAS para diseño de drenaje
    """
```

**Características:**
- **Cálculo automático de caudales** basado en datos LiDAR
- **Diseño de cunetas** con sección triangular
- **Análisis hidráulico** (flujo subcrítico)
- **Exportación a formato HEC-RAS**

### 5. 🏗️ Integración AutoCAD Civil 3D
```python
def exportar_autocad_civil3d(points_data, output_path):
    """
    Exporta datos a AutoCAD Civil 3D
    """
```

**Funcionalidades:**
- Exportación de nubes de puntos
- Generación automática de planos
- Integración con herramientas CAD
- Compatibilidad con BIM

## 📊 Resultados del Caso San Miguel

### 📈 Datos LiDAR Procesados
- **Puntos totales:** 150,000
- **Puntos de suelo:** 120,000 (80%)
- **Pendiente promedio:** 5.2%
- **Pendiente máxima:** 12.8%
- **Rango de elevación:** 15m

### 🌍 Datos Satelitales
- **NDVI promedio:** 0.383
- **Humedad del suelo:** 0.148
- **CBR estimado:** 4.7%
- **Módulo de reacción K:** 47 MPa/m

### 🛣️ Diseño de Pavimentos

#### Pavimento Rígido
- **ESALs totales:** 8,760,000
- **Espesor de losa:** 280 mm
- **Longitud de junta:** 8.4 m
- **Área de acero:** 0.28 cm²/m

#### Pavimento Flexible
- **Número estructural:** 3.2
- **Espesor asfalto:** 128 mm
- **Espesor base:** 96 mm
- **Espesor subbase:** 77 mm

### 🌊 Diseño de Drenaje
- **Área de drenaje:** 0.2 ha
- **Caudal de diseño:** 1.2 L/s
- **Profundidad cuneta:** 150 mm
- **Velocidad de flujo:** 1.5 m/s

## 🔧 Instalación y Dependencias

### Requisitos del Sistema
```bash
# Dependencias principales
pip install streamlit pandas numpy matplotlib plotly reportlab

# Dependencias LiDAR
pip install laspy open3d rasterio

# Google Earth Engine
pip install earthengine-api geemap

# AutoCAD integration
pip install pyautocad

# Análisis científico
pip install scipy scikit-learn
```

### Archivo requirements.txt
```txt
# --- DEPENDENCIAS PARA LIDAR/DRONES ---
laspy>=2.0.0
open3d>=0.17.0
rasterio>=1.3.0
earthengine-api>=0.1.0
geemap>=0.20.0
pyautocad>=0.2.0
scipy>=1.9.0
scikit-learn>=1.1.0
```

## 🚀 Uso del Módulo

### 1. Ejecutar Aplicación Principal
```bash
streamlit run APP.py
```

### 2. Seleccionar Pestaña "LiDAR/Drones"

### 3. Cargar Datos
- **Archivo LAS/LAZ:** Subir archivo de drone
- **Coordenadas:** Ingresar latitud/longitud
- **Parámetros:** Configurar período y tránsito

### 4. Procesar y Analizar
- **Procesamiento automático** de datos LiDAR
- **Extracción de datos satelitales** (GEE)
- **Cálculo de pavimentos** rígido y flexible
- **Generación de drenaje** HEC-RAS

### 5. Exportar Resultados
- **PDF completo** con análisis
- **Archivo HEC-RAS** para drenaje
- **Datos para AutoCAD** Civil 3D

## 📁 Estructura de Archivos

```
PAVIMENTO RIGIDO FLEXIBLE/
├── APP.py                          # Aplicación principal con módulo LiDAR
├── DEMOSTRACION_LIDAR_SAN_MIGUEL.py # Demostración específica
├── README_LIDAR_DRONES.md          # Este archivo
├── requirements.txt                # Dependencias actualizadas
├── datos_satelitales_san_miguel.csv # Datos GEE de San Miguel
├── hec_ras_san_miguel_-_cuadra_1.txt # Archivo HEC-RAS ejemplo
└── output_lidar_san_miguel/        # Directorio de salida LiDAR
    ├── mdt.obj                     # Modelo digital de terreno
    ├── pendientes.npy              # Datos de pendientes
    └── resultados.json             # Resultados del procesamiento
```

## 📊 Análisis de Sensibilidad

### Variables Analizadas
1. **Módulo K vs Espesor Rígido**
2. **CBR vs Espesor Flexible**
3. **Distribución de Pendientes**
4. **Área vs Caudal de Drenaje**

### Gráficos Generados
- Distribución de puntos LiDAR
- Correlación NDVI vs CBR
- Comparación de espesores
- Análisis de sensibilidad

## 💡 Recomendaciones Técnicas

### 🏗️ Construcción
- Verificar pendientes críticas > 8%
- Implementar drenaje adecuado
- Control de calidad en capas
- Monitoreo de deformaciones
- Considerar juntas de contracción
- Refuerzo por temperatura

### 🌍 Ambiental
- Considerar altitud > 3800 msnm
- Protección contra heladas
- Drenaje superficial eficiente
- Mantenimiento preventivo
- Control de erosión
- Gestión de aguas pluviales

## 🔗 Integraciones

### Software Compatible
- **AutoCAD Civil 3D:** Exportación de planos
- **HEC-RAS:** Diseño de drenaje
- **Google Earth Engine:** Datos satelitales
- **Pavement ME:** Análisis avanzado
- **PCA Spreadsheet:** Diseño rígido

### Formatos Soportados
- **Entrada:** LAS, LAZ, CSV, GeoJSON
- **Salida:** PDF, TXT (HEC-RAS), DWG, OBJ

## 📞 Soporte Técnico

### Contacto
- **Desarrollador:** CONSORCIO DEJ
- **Email:** soporte@consorciodej.com
- **Documentación:** [Enlace a documentación]

### Problemas Comunes
1. **Error LasPy:** Instalar dependencias C++
2. **GEE no disponible:** Configurar autenticación
3. **AutoCAD no conecta:** Verificar instalación
4. **Memoria insuficiente:** Reducir resolución LiDAR

## 📈 Roadmap Futuro

### Fase 1 (Actual)
- ✅ Procesamiento básico LiDAR
- ✅ Integración GEE
- ✅ Diseño automático pavimentos
- ✅ Exportación HEC-RAS

### Fase 2 (Próximos 3 meses)
- 🔄 Análisis BIM avanzado
- 🔄 Machine Learning para clasificación
- 🔄 Integración con más software CAD
- 🔄 Análisis de tránsito con ML

### Fase 3 (Próximos 6 meses)
- 📋 Cloud computing para procesamiento masivo
- 📋 API REST para integraciones
- 📋 Análisis de sensibilidad avanzado
- 📋 Generación automática de planos

---

**🚁 MÓDULO LIDAR/DRONES - CONSORCIO DEJ**  
*Software de Diseño de Pavimentos con Integración Avanzada*  
*Versión: 2.0 | Fecha: Enero 2025* 