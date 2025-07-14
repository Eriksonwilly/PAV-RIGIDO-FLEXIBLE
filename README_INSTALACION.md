# 🚀 GUÍA DE INSTALACIÓN - CONSORCIO DEJ

## 📋 Descripción

Software de Diseño de Pavimentos con integración LiDAR/Drones para análisis avanzado de pavimentos rígidos, flexibles y drenaje.

## 🔧 Requisitos del Sistema

- **Python:** 3.8 o superior
- **Sistema Operativo:** Windows 10/11, macOS, Linux
- **Memoria RAM:** Mínimo 4GB (recomendado 8GB+)
- **Espacio en disco:** 2GB libres

## 📦 Instalación Rápida

### Opción 1: Instalación Automática (Recomendada)

1. **Descargar el proyecto**
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd PAVIMENTO-RIGIDO-FLEXIBLE
   ```

2. **Ejecutar instalador automático**
   ```bash
   # Windows
   INSTALAR_DEPENDENCIAS.bat
   
   # Linux/macOS
   chmod +x INSTALAR_DEPENDENCIAS.sh
   ./INSTALAR_DEPENDENCIAS.sh
   ```

3. **Verificar instalación**
   ```bash
   python verificar_instalacion.py
   ```

4. **Ejecutar aplicación**
   ```bash
   streamlit run APP.py
   ```

### Opción 2: Instalación Manual

1. **Instalar dependencias principales**
   ```bash
   pip install streamlit>=1.28.0
   pip install pandas>=1.5.0
   pip install numpy>=1.21.0
   pip install matplotlib>=3.5.0
   pip install plotly>=5.0.0
   pip install reportlab>=3.6.0
   pip install openpyxl>=3.0.0
   pip install scipy>=1.9.0
   ```

2. **Instalar dependencias LiDAR (opcional)**
   ```bash
   pip install laspy>=2.0.0
   pip install open3d>=0.17.0
   pip install rasterio>=1.3.0
   pip install earthengine-api>=0.1.0
   pip install geemap>=0.20.0
   pip install pyautocad>=0.2.0
   pip install scikit-learn>=1.1.0
   ```

## 🚀 Ejecución

### Aplicación Principal
```bash
streamlit run APP.py
```

### Demostración LiDAR
```bash
streamlit run DEMOSTRACION_LIDAR_SAN_MIGUEL.py
```

### Verificación de Dependencias
```bash
python verificar_instalacion.py
```

## 📁 Estructura del Proyecto

```
PAVIMENTO-RIGIDO-FLEXIBLE/
├── APP.py                          # Aplicación principal
├── DEMOSTRACION_LIDAR_SAN_MIGUEL.py # Demostración LiDAR
├── requirements.txt                # Dependencias
├── INSTALAR_DEPENDENCIAS.bat       # Instalador Windows
├── verificar_instalacion.py        # Verificador
├── README_INSTALACION.md           # Este archivo
├── README_LIDAR_DRONES.md          # Documentación LiDAR
└── datos_satelitales_san_miguel.csv # Datos de ejemplo
```

## 🔍 Solución de Problemas

### Error: "Import could not be resolved"
- **Causa:** Dependencias no instaladas
- **Solución:** Ejecutar `INSTALAR_DEPENDENCIAS.bat`

### Error: "Streamlit not found"
- **Causa:** Streamlit no instalado
- **Solución:** `pip install streamlit>=1.28.0`

### Error: "Matplotlib backend"
- **Causa:** Configuración de backend
- **Solución:** El código maneja automáticamente este problema

### Error: "LiDAR dependencies"
- **Causa:** Dependencias LiDAR no instaladas
- **Solución:** Instalar opcionalmente con pip

## 📊 Funcionalidades

### ✅ Funcionalidades Básicas (Siempre Disponibles)
- Diseño de pavimento rígido (AASHTO 93)
- Diseño de pavimento flexible (AASHTO 93)
- Análisis de veredas y cunetas
- Diseño de drenaje
- Normativas locales (MTC)
- Generación de PDFs
- Gráficos de análisis

### 🚁 Funcionalidades LiDAR (Opcionales)
- Procesamiento de archivos LAS/LAZ
- Integración Google Earth Engine
- Análisis automático de pavimentos
- Diseño de drenaje HEC-RAS
- Exportación AutoCAD Civil 3D

## 🎯 Caso de Estudio

El software incluye un caso de estudio completo:
- **Ubicación:** San Miguel, Jr. Vilcanota, Cuadra 1, Puno
- **Dimensiones:** 100m × 20m
- **Altitud:** 3800+ msnm
- **Tipo:** Pavimentación urbana

## 📞 Soporte

### Contacto
- **Desarrollador:** CONSORCIO DEJ
- **Email:** soporte@consorciodej.com

### Comandos Útiles
```bash
# Verificar Python
python --version

# Verificar pip
pip --version

# Listar paquetes instalados
pip list

# Actualizar pip
python -m pip install --upgrade pip

# Instalar desde requirements
pip install -r requirements.txt
```

## 🔄 Actualizaciones

Para actualizar el software:
1. Descargar la nueva versión
2. Ejecutar `INSTALAR_DEPENDENCIAS.bat`
3. Verificar con `python verificar_instalacion.py`

## 📝 Notas Importantes

- **Primera ejecución:** Puede tardar más tiempo en cargar
- **Dependencias LiDAR:** Son opcionales, la aplicación funciona sin ellas
- **Archivos grandes:** Los archivos LAS/LAZ pueden ser pesados
- **Memoria:** Procesamiento LiDAR requiere más RAM

---

**🚀 CONSORCIO DEJ - Software de Diseño de Pavimentos**  
*Versión: 2.0 | Fecha: Enero 2025* 