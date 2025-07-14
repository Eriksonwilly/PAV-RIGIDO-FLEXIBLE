#!/usr/bin/env python3
"""
Script de verificación de dependencias para CONSORCIO DEJ
Software de Diseño de Pavimentos
"""

import sys
import importlib

def verificar_dependencia(nombre, import_name=None):
    """Verifica si una dependencia está instalada"""
    if import_name is None:
        import_name = nombre
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {nombre} - INSTALADO")
        return True
    except ImportError:
        print(f"❌ {nombre} - NO INSTALADO")
        return False

def main():
    print("=" * 60)
    print("    VERIFICACION DE DEPENDENCIAS")
    print("    CONSORCIO DEJ - Software de Pavimentos")
    print("=" * 60)
    print()
    
    # Dependencias principales (requeridas)
    print("📦 DEPENDENCIAS PRINCIPALES:")
    print("-" * 40)
    
    dependencias_principales = [
        ("Streamlit", "streamlit"),
        ("Pandas", "pandas"),
        ("NumPy", "numpy"),
        ("Matplotlib", "matplotlib"),
        ("Plotly", "plotly"),
        ("ReportLab", "reportlab"),
        ("OpenPyXL", "openpyxl"),
        ("SciPy", "scipy"),
    ]
    
    todas_principales = True
    for nombre, import_name in dependencias_principales:
        if not verificar_dependencia(nombre, import_name):
            todas_principales = False
    
    print()
    
    # Dependencias opcionales (LiDAR)
    print("🚁 DEPENDENCIAS OPCIONALES (LiDAR):")
    print("-" * 40)
    
    dependencias_opcionales = [
        ("LasPy", "laspy"),
        ("Open3D", "open3d"),
        ("Rasterio", "rasterio"),
        ("Google Earth Engine", "ee"),
        ("GeoMap", "geemap"),
        ("PyAutoCAD", "pyautocad"),
        ("Scikit-learn", "sklearn"),
    ]
    
    todas_opcionales = True
    for nombre, import_name in dependencias_opcionales:
        if not verificar_dependencia(nombre, import_name):
            todas_opcionales = False
    
    print()
    print("=" * 60)
    
    # Resumen
    if todas_principales:
        print("✅ TODAS LAS DEPENDENCIAS PRINCIPALES ESTÁN INSTALADAS")
        print("   La aplicación básica funcionará correctamente")
    else:
        print("❌ FALTAN DEPENDENCIAS PRINCIPALES")
        print("   Ejecuta: INSTALAR_DEPENDENCIAS.bat")
        print("   O instala manualmente las dependencias faltantes")
    
    if todas_opcionales:
        print("✅ TODAS LAS DEPENDENCIAS LIDAR ESTÁN INSTALADAS")
        print("   La funcionalidad LiDAR estará disponible")
    else:
        print("⚠️  FALTAN DEPENDENCIAS LIDAR (OPCIONALES)")
        print("   Para funcionalidad LiDAR completa, instala:")
        print("   pip install laspy open3d rasterio earthengine-api geemap pyautocad scikit-learn")
    
    print()
    print("🚀 PARA EJECUTAR LA APLICACIÓN:")
    print("   streamlit run APP.py")
    print()
    print("=" * 60)

if __name__ == "__main__":
    main() 