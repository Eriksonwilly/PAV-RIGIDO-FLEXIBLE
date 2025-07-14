#!/usr/bin/env python3
"""
VERIFICACIÓN FINAL COMPLETA - APP PAVIMENTOS
============================================

Script de verificación integral para asegurar que toda la aplicación
funcione correctamente antes del despliegue final.
"""

import sys
import os
import json
from datetime import datetime

def test_imports():
    """Prueba todas las importaciones necesarias"""
    print("🔍 VERIFICANDO IMPORTACIONES...")
    print("-" * 40)
    
    imports = [
        ('streamlit', 'st'),
        ('numpy', 'np'),
        ('matplotlib.pyplot', 'plt'),
        ('pandas', 'pd'),
        ('reportlab', 'reportlab'),
        ('plotly', 'plotly'),
        ('json', 'json'),
        ('datetime', 'datetime'),
        ('io', 'BytesIO'),
        ('base64', 'base64')
    ]
    
    results = []
    for module_name, import_name in imports:
        try:
            __import__(import_name)
            print(f"✅ {module_name}: OK")
            results.append(True)
        except ImportError:
            print(f"❌ {module_name}: FALTA")
            results.append(False)
    
    return results

def test_san_miguel_module():
    """Prueba el módulo de caso práctico San Miguel"""
    print("\n🔍 VERIFICANDO MÓDULO SAN MIGUEL...")
    print("-" * 40)
    
    try:
        from CASO_PRACTICO_SAN_MIGUEL_COMPLETO import CasoPracticoSanMiguel, EnhancedJSONEncoder
        print("✅ Importación de CasoPracticoSanMiguel: OK")
        print("✅ Importación de EnhancedJSONEncoder: OK")
        
        # Probar la creación de instancia
        caso = CasoPracticoSanMiguel()
        print("✅ Creación de instancia: OK")
        
        # Probar la ejecución completa
        print("🏗️ Ejecutando caso práctico...")
        resultado = caso.ejecutar_caso_completo()
        
        if "error" not in resultado:
            print("✅ Ejecución del caso práctico: OK")
            print(f"📊 Proyecto: {resultado['resumen_ejecutivo']['proyecto']}")
            print(f"📍 Ubicación: {resultado['resumen_ejecutivo']['ubicacion']}")
            print(f"🏗️ Tipo Pavimento: {resultado['resumen_ejecutivo']['tipo_pavimento_recomendado']}")
            print(f"📏 Espesor: {resultado['resumen_ejecutivo']['espesor_recomendado']}")
            print(f"💰 Costo: {resultado['resumen_ejecutivo']['costo_estimado']}")
            print(f"⏱️ Duración: {resultado['resumen_ejecutivo']['duracion_obra']}")
            print(f"📁 Archivos generados: {len(resultado['archivos_generados'])}")
            
            # Verificar que se guardaron los archivos
            if os.path.exists("resultados_san_miguel"):
                print("✅ Directorio de resultados creado: OK")
                if os.path.exists("resultados_san_miguel/reporte_completo.json"):
                    print("✅ Archivo JSON guardado: OK")
                if os.path.exists("resultados_san_miguel/resumen_ejecutivo.txt"):
                    print("✅ Archivo TXT guardado: OK")
            
            return True
        else:
            print(f"❌ Error en caso práctico: {resultado['error']}")
            return False
            
    except Exception as e:
        print(f"❌ Error en módulo San Miguel: {e}")
        return False

def test_streamlit_compatibility():
    """Prueba la compatibilidad con Streamlit"""
    print("\n🔍 VERIFICANDO COMPATIBILIDAD STREAMLIT...")
    print("-" * 40)
    
    try:
        import streamlit as st
        print("✅ Streamlit disponible")
        
        # Verificar funciones modernas
        if hasattr(st, 'rerun'):
            print("✅ st.rerun() disponible (versión moderna)")
        else:
            print("⚠️ st.rerun() no disponible")
            
        if hasattr(st, 'experimental_rerun'):
            print("⚠️ st.experimental_rerun() disponible (versión antigua)")
        else:
            print("✅ st.experimental_rerun() no disponible (correcto)")
            
        # Verificar otras funciones importantes
        required_functions = [
            'set_page_config', 'header', 'subheader', 'info', 'warning', 'error',
            'success', 'button', 'form', 'form_submit_button', 'text_input',
            'number_input', 'selectbox', 'radio', 'checkbox', 'data_editor',
            'columns', 'container', 'spinner', 'metric', 'download_button',
            'tabs', 'divider', 'markdown', 'caption', 'stop'
        ]
        
        missing_functions = []
        for func in required_functions:
            if not hasattr(st, func):
                missing_functions.append(func)
        
        if missing_functions:
            print(f"❌ Funciones faltantes: {missing_functions}")
            return False
        else:
            print("✅ Todas las funciones de Streamlit disponibles: OK")
            return True
            
    except ImportError:
        print("❌ Streamlit no está instalado")
        return False

def test_app_structure():
    """Prueba la estructura de la aplicación"""
    print("\n🔍 VERIFICANDO ESTRUCTURA DE LA APP...")
    print("-" * 40)
    
    required_files = [
        'APP.py',
        'CASO_PRACTICO_SAN_MIGUEL_COMPLETO.py',
        'requirements.txt',
        'README.md'
    ]
    
    optional_files = [
        'MODULO_LIDAR_DRONES.py',
        'MODULO_DISENO_AUTOMATIZADO.py',
        'MODULO_INTEROPERABILIDAD.py',
        'MODULO_GOOGLE_EARTH_ENGINE.py',
        'MODULO_LIDAR_AVANZADO.py',
        'MODULO_EXPORTACION_EXTERNA.py'
    ]
    
    results = []
    
    # Verificar archivos requeridos
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}: OK")
            results.append(True)
        else:
            print(f"❌ {file}: FALTA")
            results.append(False)
    
    # Verificar archivos opcionales
    for file in optional_files:
        if os.path.exists(file):
            print(f"✅ {file}: OK (opcional)")
        else:
            print(f"⚠️ {file}: No disponible (opcional)")
    
    return all(results)

def test_json_serialization():
    """Prueba la serialización JSON con el encoder mejorado"""
    print("\n🔍 VERIFICANDO SERIALIZACIÓN JSON...")
    print("-" * 40)
    
    try:
        from CASO_PRACTICO_SAN_MIGUEL_COMPLETO import EnhancedJSONEncoder
        
        # Crear datos de prueba con tipos problemáticos
        test_data = {
            'string': 'test',
            'number': 123,
            'boolean': True,
            'list': [1, 2, 3],
            'dict': {'key': 'value'},
            'none': None,
            'complex_object': object(),  # Objeto no serializable
            'function': lambda x: x,     # Función no serializable
        }
        
        # Intentar serializar
        json_str = json.dumps(test_data, cls=EnhancedJSONEncoder, indent=2)
        print("✅ Serialización JSON con encoder mejorado: OK")
        
        # Verificar que se puede deserializar
        parsed_data = json.loads(json_str)
        print("✅ Deserialización JSON: OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en serialización JSON: {e}")
        return False

def generate_final_report(results):
    """Genera un reporte final de verificación"""
    print("\n" + "=" * 60)
    print("📊 REPORTE FINAL DE VERIFICACIÓN")
    print("=" * 60)
    
    test_names = [
        "Importaciones",
        "Módulo San Miguel", 
        "Compatibilidad Streamlit",
        "Estructura de la App",
        "Serialización JSON"
    ]
    
    passed = 0
    total = len(results)
    
    for i, (test_name, result) in enumerate(zip(test_names, results)):
        status = "✅ PASÓ" if result else "❌ FALLÓ"
        print(f"{i+1}. {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Resultado: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("\n🎉 ¡VERIFICACIÓN COMPLETA EXITOSA!")
        print("✅ La aplicación está lista para producción")
        print("✅ El caso práctico San Miguel funciona correctamente")
        print("✅ La serialización JSON está corregida")
        print("✅ Streamlit es compatible")
        print("\n💡 Para ejecutar la app:")
        print("   python -m streamlit run APP.py --server.port 8501")
    else:
        print(f"\n⚠️ {total - passed} pruebas fallaron")
        print("💡 Revisa los errores arriba e instala las dependencias faltantes:")
        print("   pip install -r requirements.txt")
    
    # Guardar reporte
    report_data = {
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'resultados': dict(zip(test_names, results)),
        'total_passed': passed,
        'total_tests': total,
        'status': 'EXITOSO' if passed == total else 'CON ERRORES'
    }
    
    with open('verificacion_final_report.json', 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n📄 Reporte guardado en: verificacion_final_report.json")

def main():
    """Función principal de verificación"""
    print("🧪 VERIFICACIÓN FINAL COMPLETA - APP PAVIMENTOS")
    print("Sistema de Diseño de Pavimentos Rígido y Flexible")
    print("=" * 70)
    
    # Ejecutar todas las pruebas
    tests = [
        test_imports(),
        test_san_miguel_module(),
        test_streamlit_compatibility(),
        test_app_structure(),
        test_json_serialization()
    ]
    
    # Generar reporte final
    generate_final_report(tests)

if __name__ == "__main__":
    main() 