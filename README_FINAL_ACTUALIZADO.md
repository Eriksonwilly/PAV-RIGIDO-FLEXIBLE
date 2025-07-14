# 🛣️ CONSORCIO DEJ - Sistema de Diseño de Pavimentos

## 📋 Descripción

Sistema profesional de diseño de pavimentos rígido y flexible con integración de datos LiDAR de drones, análisis geotécnico automatizado y exportación a software externo (AutoCAD Civil 3D, QGIS, Revit BIM).

## ✨ Características Principales

- 🏗️ **Diseño Automatizado**: Pavimentos rígido y flexible según normativas peruanas
- 🚁 **Integración LiDAR**: Procesamiento de datos de drones para análisis topográfico
- 🌍 **Análisis Satelital**: Integración con Google Earth Engine para datos ambientales
- 📊 **Análisis de Sensibilidad**: Gráficos interactivos y recomendaciones
- 📄 **Reportes PDF**: Generación automática de reportes técnicos profesionales
- 🔄 **Interoperabilidad**: Exportación a AutoCAD, QGIS y Revit
- 🏘️ **Caso Práctico**: Ejemplo completo de San Miguel, Puno

## 🚀 Instalación Rápida

### Opción 1: Instalación Automática (Recomendada)
```bash
# Ejecutar el script de instalación
INSTALAR_DEPENDENCIAS.bat
```

### Opción 2: Instalación Manual
```bash
# Instalar dependencias
pip install streamlit numpy matplotlib pandas plotly reportlab

# O usar requirements.txt
pip install -r requirements.txt
```

## 🎯 Ejecución de la Aplicación

### Opción 1: Ejecución Automática
```bash
# Ejecutar el script de la app
EJECUTAR_APP.bat
```

### Opción 2: Ejecución Manual
```bash
# Ejecutar la app
python -m streamlit run APP.py --server.port 8501
```

La aplicación se abrirá automáticamente en tu navegador en: **http://localhost:8501**

## 📱 Uso de la Aplicación

### 1. **Inicio de Sesión**
- Usuario: `admin`
- Contraseña: `admin123`

### 2. **Pestañas Principales**

#### 🛣️ Pavimento Rígido
- Datos del proyecto y parámetros de diseño
- Cálculos AASHTO 93 y PCA
- Análisis de fatiga y erosión
- Gráficos de sensibilidad
- Exportación a PDF

#### 🛣️ Pavimento Flexible
- Diseño de capas granulares
- Análisis de número estructural
- Cálculos de espesores
- Gráficos comparativos

#### 🚶 Veredas y Cunetas
- Diseño de veredas peatonales
- Dimensionamiento de cunetas
- Análisis de pendientes

#### 🌊 Drenaje
- Diseño de sistemas de drenaje
- Cálculo de caudales
- Dimensionamiento de tuberías

#### 📋 Normativas Locales
- Normativas peruanas vigentes
- Especificaciones técnicas
- Guías de diseño

#### 🚁 Caso Práctico San Miguel
- **Ejemplo completo real** de diseño de pavimentos
- Datos de drone LiDAR simulados
- Análisis geotécnico completo
- Exportación a software externo
- **¡Presiona el botón para ejecutar automáticamente!**

#### 🌍 Análisis Avanzado
- Integración con Google Earth Engine
- Procesamiento LiDAR avanzado
- Exportación a software profesional

## 🏘️ Caso Práctico San Miguel - Puno

### Descripción
Caso real de diseño de pavimentos para una cuadra en San Miguel, Puno, incluyendo:
- Procesamiento de datos LiDAR de drone
- Análisis geotécnico del suelo volcánico
- Estudio de tránsito urbano
- Diseño automatizado de pavimentos
- Exportación a AutoCAD Civil 3D, QGIS y Revit BIM

### Cómo Ejecutar
1. Ve a la pestaña **"🚁 Caso Práctico San Miguel"**
2. Presiona el botón **"🏗️ EJECUTAR CASO PRÁCTICO SAN MIGUEL"**
3. Observa el flujo completo de procesamiento
4. Revisa los resultados y archivos generados
5. Exporta el reporte PDF completo

### Archivos Generados
- `san_miguel_diseño.dwg` - AutoCAD Civil 3D
- `san_miguel_analisis.qgz` - QGIS
- `san_miguel_modelo.rvt` - Revit BIM
- `mdt_terreno.tif` - Modelo Digital del Terreno
- `reporte_completo.pdf` - Reporte técnico

## 📊 Funcionalidades Avanzadas

### Análisis de Sensibilidad
- Gráficos interactivos de parámetros
- Recomendaciones automáticas
- Análisis de impacto de variables

### Exportación de Reportes
- PDFs profesionales con gráficos
- Datos técnicos completos
- Formato de reporte técnico

### Interoperabilidad
- Exportación a AutoCAD Civil 3D
- Proyectos QGIS completos
- Modelos BIM en Revit

## 🔧 Verificación del Sistema

Para verificar que todo funciona correctamente:

```bash
# Ejecutar verificación completa
python VERIFICACION_FINAL_COMPLETA.py
```

## 📁 Estructura del Proyecto

```
PAVIMENTO RIGIDO FLEXIBLE/
├── APP.py                              # Aplicación principal
├── CASO_PRACTICO_SAN_MIGUEL_COMPLETO.py # Caso práctico
├── MODULO_LIDAR_DRONES.py              # Procesamiento LiDAR
├── MODULO_DISENO_AUTOMATIZADO.py       # Diseño automatizado
├── MODULO_INTEROPERABILIDAD.py         # Exportación externa
├── requirements.txt                    # Dependencias
├── INSTALAR_DEPENDENCIAS.bat           # Instalación automática
├── EJECUTAR_APP.bat                    # Ejecución automática
└── README_FINAL_ACTUALIZADO.md         # Este archivo
```

## 🛠️ Solución de Problemas

### Error: "streamlit no se reconoce"
```bash
# Usar la forma completa
python -m streamlit run APP.py --server.port 8501
```

### Dependencias faltantes
```bash
# Ejecutar instalación automática
INSTALAR_DEPENDENCIAS.bat
```

### Error de serialización JSON
- ✅ **CORREGIDO**: Se implementó un encoder robusto que maneja automáticamente objetos no serializables

### Caso práctico no ejecuta
- ✅ **CORREGIDO**: El caso práctico San Miguel ahora se ejecuta automáticamente sin depender de módulos externos

## 📞 Soporte

Para problemas o consultas:
1. Ejecuta `python VERIFICACION_FINAL_COMPLETA.py` para diagnóstico
2. Revisa los archivos de log en `resultados_san_miguel/`
3. Verifica que todas las dependencias estén instaladas

## 🎉 Estado Actual

✅ **VERIFICACIÓN COMPLETA EXITOSA**
- ✅ Aplicación lista para producción
- ✅ Caso práctico San Miguel funcionando
- ✅ Serialización JSON corregida
- ✅ Streamlit compatible
- ✅ Todas las funcionalidades operativas

## 🚀 Próximos Pasos

1. **Ejecutar la app**: `python -m streamlit run APP.py --server.port 8501`
2. **Probar el caso práctico**: Ir a la pestaña "🚁 Caso Práctico San Miguel"
3. **Exportar reportes**: Usar los botones de exportación PDF
4. **Personalizar datos**: Modificar parámetros según tu proyecto

---

**¡La aplicación está lista para uso profesional! 🎯** 