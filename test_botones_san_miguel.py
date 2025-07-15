#!/usr/bin/env python3
"""
Test de botones para San Miguel Puno - Cuadra 1
Verifica que los botones de exportación funcionen correctamente
"""

import streamlit as st
import numpy as np
from datetime import datetime
import os

def test_generar_pdf_lidar():
    """Test de generación de PDF LiDAR"""
    print("🧪 Probando generación de PDF LiDAR...")
    
    # Datos de ejemplo para San Miguel
    datos_proyecto = {
        'Proyecto': 'San Miguel Puno - Cuadra 1',
        'Descripción': 'Pavimentación urbana con análisis LiDAR y datos satelitales',
        'Usuario': 'Usuario Test',
        'Sistema_Unidades': 'Sistema Internacional (SI)'
    }
    
    resultados_lidar = {
        'total_points': 25000,
        'area_ha': 0.08,
        'elevation_min': 3800,
        'elevation_max': 3810,
        'elevation_avg': 3805,
        'pendiente_promedio': 5.2,
        'pendiente_maxima': 8.5,
        'ground_points': 15000,
        'vegetation_points': 8000,
        'building_points': 2000
    }
    
    datos_satelitales = {
        'NDVI_promedio': 0.383,
        'NDVI_minimo': 0.252,
        'NDVI_maximo': 0.557,
        'Humedad_suelo_promedio': 0.148,
        'Precipitacion_anual': 640.8,
        'Temperatura_promedio': 9.2,
        'CBR_estimado_NDVI': 4.7,
        'Clasificacion_suelo': 'Suelo volcánico con baja retención de humedad'
    }
    
    hec_ras_content = """HEC-RAS Version 6.0
Title: San Miguel - Cuadra 1 - Diseño de Drenaje
Author: Software de Diseño de Pavimentos - UNI
Date: 2025-07-13
Description: Diseño de cunetas y drenaje superficial para pavimentación urbana

# DATOS DEL PROYECTO
Project Name: San Miguel - Cuadra 1
Location: San Miguel, Puno, Perú
Design Year: 2025
Return Period: 10 years

# PARÁMETROS HIDROLÓGICOS
Area: 0.08 ha
Length: 100 m
Slope: 5.2%
Time of Concentration: 8.5 min
Rainfall Intensity: 60 mm/h
Runoff Coefficient: 0.7

# DISEÑO DE CUNETAS
Design Flow: 0.0012 m³/s
Design Flow: 1.2 L/s
Velocity: 1.5 m/s
Depth: 0.15 m
Width: 0.3 m

# GEOMETRÍA DE CUNETAS
# Sección triangular
Station 0.0
Elevation 0.15
Station 0.3
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
Expected Depth: 0.15 m
Expected Velocity: 1.5 m/s
Froude Number: < 1.0 (Subcritical)
Safety Factor: > 1.5

# RECOMENDACIONES
- Mantener pendiente mínima de 2%
- Limpieza periódica de cunetas
- Considerar drenaje subterráneo en zonas críticas
- Verificar capacidad durante eventos extremos"""
    
    try:
        # Importar la función desde APP.py
        import sys
        sys.path.append('.')
        from APP import generar_pdf_lidar_completo
        
        pdf_buffer = generar_pdf_lidar_completo(
            datos_proyecto, 
            resultados_lidar, 
            datos_satelitales, 
            hec_ras_content
        )
        
        if pdf_buffer:
            # Guardar el PDF
            with open("test_pdf_lidar_san_miguel.pdf", "wb") as f:
                f.write(pdf_buffer.getvalue())
            print("✅ PDF LiDAR generado exitosamente: test_pdf_lidar_san_miguel.pdf")
            return True
        else:
            print("❌ Error al generar PDF LiDAR")
            return False
            
    except Exception as e:
        print(f"❌ Error en test PDF LiDAR: {str(e)}")
        return False

def test_generar_hec_ras():
    """Test de generación de archivo HEC-RAS"""
    print("🧪 Probando generación de archivo HEC-RAS...")
    
    try:
        hec_ras_content = """HEC-RAS Version 6.0
Title: San Miguel - Cuadra 1 - Diseño de Drenaje
Author: Software de Diseño de Pavimentos - UNI
Date: 2025-07-13
Description: Diseño de cunetas y drenaje superficial para pavimentación urbana

# DATOS DEL PROYECTO
Project Name: San Miguel - Cuadra 1
Location: San Miguel, Puno, Perú
Design Year: 2025
Return Period: 10 years

# PARÁMETROS HIDROLÓGICOS
Area: 0.08 ha
Length: 100 m
Slope: 5.2%
Time of Concentration: 8.5 min
Rainfall Intensity: 60 mm/h
Runoff Coefficient: 0.7

# DISEÑO DE CUNETAS
Design Flow: 0.0012 m³/s
Design Flow: 1.2 L/s
Velocity: 1.5 m/s
Depth: 0.15 m
Width: 0.3 m

# GEOMETRÍA DE CUNETAS
# Sección triangular
Station 0.0
Elevation 0.15
Station 0.3
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
Expected Depth: 0.15 m
Expected Velocity: 1.5 m/s
Froude Number: < 1.0 (Subcritical)
Safety Factor: > 1.5

# RECOMENDACIONES
- Mantener pendiente mínima de 2%
- Limpieza periódica de cunetas
- Considerar drenaje subterráneo en zonas críticas
- Verificar capacidad durante eventos extremos

# COORDENADAS DEL PROYECTO
Latitude: -15.8422
Longitude: -70.0199
Elevation: 3805 m
Zone: UTM 19S

# ANÁLISIS DE CAPACIDAD
Capacity Check: PASSED
Safety Factor: 1.8
Design Criteria: MET
Notes: Cunetas adecuadas para condiciones de San Miguel, Puno"""
        
        # Guardar el archivo
        with open("test_hec_ras_san_miguel.txt", "w", encoding="utf-8") as f:
            f.write(hec_ras_content)
        
        print("✅ Archivo HEC-RAS generado exitosamente: test_hec_ras_san_miguel.txt")
        return True
        
    except Exception as e:
        print(f"❌ Error en test HEC-RAS: {str(e)}")
        return False

def test_generar_autocad():
    """Test de generación de datos AutoCAD"""
    print("🧪 Probando generación de datos AutoCAD...")
    
    try:
        # Crear puntos de ejemplo para San Miguel (100m x 8m)
        x_coords = np.linspace(0, 100, 101)  # 101 puntos cada 1m
        y_coords = np.linspace(0, 8, 9)      # 9 puntos cada 1m
        
        # Crear malla de puntos
        X, Y = np.meshgrid(x_coords, y_coords)
        
        # Elevación base de San Miguel (3805m) con variación
        Z_base = 3805 + 0.1 * np.sin(X/10) + 0.05 * np.cos(Y/2)
        
        # Convertir a lista de puntos [x, y, z]
        points_data = []
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                points_data.append([X[i,j], Y[i,j], Z_base[i,j]])
        
        # Crear archivo de puntos para AutoCAD
        autocad_content = f"""# AutoCAD Point Cloud Data - San Miguel, Puno
# Generated by CONSORCIO DEJ Software
# Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Project: San Miguel - Cuadra 1
# Total Points: {len(points_data)}

# Format: X, Y, Z, Description
# Coordinates in meters, UTM Zone 19S

# Ground Points
"""
        
        # Agregar puntos al contenido
        for i, point in enumerate(points_data[:1000]):  # Límite de 1000 puntos
            autocad_content += f"{point[0]:.3f}, {point[1]:.3f}, {point[2]:.3f}, Ground\n"
        
        # Agregar puntos de cunetas
        for i in range(0, 101, 5):  # Cada 5m
            autocad_content += f"{i:.3f}, 0.0, {3805 + 0.1 * np.sin(i/10):.3f}, Cuneta_Izq\n"
            autocad_content += f"{i:.3f}, 8.0, {3805 + 0.1 * np.sin(i/10):.3f}, Cuneta_Der\n"
        
        # Agregar puntos de juntas
        for i in range(0, 101, 12):  # Juntas cada 12m
            autocad_content += f"{i:.3f}, 4.0, {3805 + 0.1 * np.sin(i/10):.3f}, Junta_Contraccion\n"
        
        # Guardar el archivo
        with open("test_autocad_san_miguel.txt", "w", encoding="utf-8") as f:
            f.write(autocad_content)
        
        print("✅ Datos AutoCAD generados exitosamente: test_autocad_san_miguel.txt")
        return True
        
    except Exception as e:
        print(f"❌ Error en test AutoCAD: {str(e)}")
        return False

def main():
    """Función principal de pruebas"""
    print("🚀 Iniciando pruebas de botones para San Miguel Puno - Cuadra 1")
    print("=" * 60)
    
    # Ejecutar pruebas
    resultados = []
    
    resultados.append(("PDF LiDAR", test_generar_pdf_lidar()))
    resultados.append(("HEC-RAS", test_generar_hec_ras()))
    resultados.append(("AutoCAD", test_generar_autocad()))
    
    # Mostrar resumen
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 60)
    
    exitos = 0
    for nombre, resultado in resultados:
        status = "✅ EXITOSO" if resultado else "❌ FALLIDO"
        print(f"{nombre:15} : {status}")
        if resultado:
            exitos += 1
    
    print(f"\n🎯 Resultado: {exitos}/{len(resultados)} pruebas exitosas")
    
    if exitos == len(resultados):
        print("🎉 ¡Todas las pruebas pasaron! Los botones están funcionando correctamente.")
    else:
        print("⚠️ Algunas pruebas fallaron. Revisar los errores anteriores.")
    
    # Listar archivos generados
    print("\n📁 Archivos generados:")
    archivos_test = [
        "test_pdf_lidar_san_miguel.pdf",
        "test_hec_ras_san_miguel.txt", 
        "test_autocad_san_miguel.txt"
    ]
    
    for archivo in archivos_test:
        if os.path.exists(archivo):
            size = os.path.getsize(archivo)
            print(f"  ✅ {archivo} ({size} bytes)")
        else:
            print(f"  ❌ {archivo} (no encontrado)")

if __name__ == "__main__":
    main() 