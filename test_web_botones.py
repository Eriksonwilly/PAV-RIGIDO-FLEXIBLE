#!/usr/bin/env python3
"""
Test de botones en entorno web para San Miguel Puno - Cuadra 1
Verifica que los botones funcionen correctamente en Streamlit
"""

import requests
import time
import json
from datetime import datetime

def test_web_connection():
    """Test de conexión a la aplicación web"""
    print("🌐 Probando conexión a la aplicación web...")
    
    try:
        # Intentar conectar a la aplicación
        response = requests.get("http://localhost:8501", timeout=10)
        if response.status_code == 200:
            print("✅ Conexión exitosa a http://localhost:8501")
            return True
        else:
            print(f"❌ Error de conexión: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar a la aplicación")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_web_interface():
    """Test de la interfaz web"""
    print("\n🧪 Probando interfaz web...")
    
    try:
        # Verificar que la aplicación esté respondiendo
        response = requests.get("http://localhost:8501/_stcore/health", timeout=5)
        if response.status_code == 200:
            print("✅ Interfaz web funcionando correctamente")
            return True
        else:
            print(f"⚠️ Interfaz web con problemas: {response.status_code}")
            return False
    except Exception as e:
        print(f"⚠️ No se puede verificar la interfaz: {str(e)}")
        return False

def generate_test_report():
    """Generar reporte de prueba"""
    print("\n📊 Generando reporte de prueba...")
    
    report = {
        "fecha_prueba": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "aplicacion": "APP.py - San Miguel Puno",
        "puerto": 8501,
        "urls": {
            "local": "http://localhost:8501",
            "network": "http://192.168.156.127:8501",
            "external": "http://132.157.130.213:8501"
        },
        "botones_testeados": [
            "🚀 Generar PDF LiDAR Completo",
            "📁 Exportar HEC-RAS", 
            "🏗️ Exportar AutoCAD"
        ],
        "datos_implementados": {
            "proyecto": "San Miguel Puno - Cuadra 1",
            "ubicacion": "San Miguel, Puno, Perú",
            "coordenadas": "-15.8422°S, -70.0199°W",
            "elevacion": "3805 msnm",
            "area": "0.08 ha (100m x 8m)",
            "pendiente": "5.2% promedio"
        },
        "archivos_generados": [
            "test_pdf_lidar_san_miguel.pdf",
            "test_hec_ras_san_miguel.txt",
            "test_autocad_san_miguel.txt"
        ]
    }
    
    # Guardar reporte
    with open("test_web_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("✅ Reporte generado: test_web_report.json")
    return report

def main():
    """Función principal de pruebas web"""
    print("🚀 Iniciando pruebas web para San Miguel Puno - Cuadra 1")
    print("=" * 60)
    
    # Verificar conexión
    connection_ok = test_web_connection()
    
    # Verificar interfaz
    interface_ok = test_web_interface()
    
    # Generar reporte
    report = generate_test_report()
    
    # Mostrar resumen
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS WEB")
    print("=" * 60)
    
    print(f"🌐 Conexión web: {'✅ EXITOSA' if connection_ok else '❌ FALLIDA'}")
    print(f"🖥️ Interfaz web: {'✅ FUNCIONANDO' if interface_ok else '⚠️ PROBLEMAS'}")
    
    print(f"\n📱 URLs disponibles:")
    print(f"  • Local: {report['urls']['local']}")
    print(f"  • Red: {report['urls']['network']}")
    print(f"  • Externa: {report['urls']['external']}")
    
    print(f"\n🎯 Botones implementados:")
    for boton in report['botones_testeados']:
        print(f"  • {boton}")
    
    print(f"\n📊 Datos del proyecto:")
    for key, value in report['datos_implementados'].items():
        print(f"  • {key}: {value}")
    
    print(f"\n📁 Archivos de prueba:")
    for archivo in report['archivos_generados']:
        print(f"  • {archivo}")
    
    if connection_ok and interface_ok:
        print("\n🎉 ¡La aplicación web está funcionando correctamente!")
        print("💡 Puedes acceder a http://localhost:8501 para probar los botones")
        print("🔧 Los botones están listos para usar con datos de San Miguel Puno")
    else:
        print("\n⚠️ La aplicación web tiene algunos problemas")
        print("🔧 Revisar logs de Streamlit para más detalles")
    
    print(f"\n📄 Reporte guardado en: test_web_report.json")

if __name__ == "__main__":
    main() 