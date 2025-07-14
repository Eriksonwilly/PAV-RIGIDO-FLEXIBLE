#!/usr/bin/env python3
"""
TEST SAN MIGUEL CASE STUDY FIX
==============================

Script para verificar que el caso práctico San Miguel funciona correctamente
después de las correcciones en APP.py
"""

import sys
import os

def test_san_miguel_import():
    """Prueba la importación del módulo San Miguel"""
    try:
        from CASO_PRACTICO_SAN_MIGUEL_COMPLETO import CasoPracticoSanMiguel
        print("✅ Importación de CasoPracticoSanMiguel: OK")
        return True
    except ImportError as e:
        print(f"❌ Error importando CasoPracticoSanMiguel: {e}")
        return False

def test_san_miguel_execution():
    """Prueba la ejecución del caso práctico San Miguel"""
    try:
        from CASO_PRACTICO_SAN_MIGUEL_COMPLETO import CasoPracticoSanMiguel
        
        print("🏗️ Ejecutando caso práctico San Miguel...")
        caso = CasoPracticoSanMiguel()
        resultado = caso.ejecutar_caso_completo()
        
        if "error" not in resultado:
            print("✅ Caso práctico San Miguel ejecutado exitosamente!")
            print(f"📊 Proyecto: {resultado['resumen_ejecutivo']['proyecto']}")
            print(f"📍 Ubicación: {resultado['resumen_ejecutivo']['ubicacion']}")
            print(f"🏗️ Tipo Pavimento: {resultado['resumen_ejecutivo']['tipo_pavimento_recomendado']}")
            print(f"📏 Espesor: {resultado['resumen_ejecutivo']['espesor_recomendado']}")
            print(f"💰 Costo: {resultado['resumen_ejecutivo']['costo_estimado']}")
            print(f"⏱️ Duración: {resultado['resumen_ejecutivo']['duracion_obra']}")
            print(f"📁 Archivos generados: {len(resultado['archivos_generados'])}")
            return True
        else:
            print(f"❌ Error en caso práctico: {resultado['error']}")
            return False
            
    except Exception as e:
        print(f"❌ Error ejecutando caso práctico: {e}")
        return False

def test_streamlit_compatibility():
    """Prueba la compatibilidad con Streamlit"""
    try:
        import streamlit as st
        print("✅ Streamlit disponible")
        
        # Verificar que st.rerun() está disponible (nueva versión)
        if hasattr(st, 'rerun'):
            print("✅ st.rerun() disponible (versión moderna)")
        else:
            print("⚠️ st.rerun() no disponible, usando st.experimental_rerun()")
            
        return True
    except ImportError:
        print("❌ Streamlit no está instalado")
        return False

def test_dependencies():
    """Prueba las dependencias principales"""
    dependencies = [
        ('numpy', 'np'),
        ('matplotlib.pyplot', 'plt'),
        ('pandas', 'pd'),
        ('reportlab', 'reportlab'),
        ('plotly', 'plotly')
    ]
    
    results = []
    for dep_name, import_name in dependencies:
        try:
            __import__(import_name)
            print(f"✅ {dep_name}: OK")
            results.append(True)
        except ImportError:
            print(f"⚠️ {dep_name}: No disponible")
            results.append(False)
    
    return all(results)

def main():
    """Función principal de pruebas"""
    print("🧪 TEST SAN MIGUEL CASE STUDY FIX")
    print("=" * 50)
    
    tests = [
        ("Dependencias principales", test_dependencies),
        ("Compatibilidad Streamlit", test_streamlit_compatibility),
        ("Importación San Miguel", test_san_miguel_import),
        ("Ejecución San Miguel", test_san_miguel_execution)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🔍 {test_name}:")
        print("-" * 30)
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Error en {test_name}: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE PRUEBAS:")
    print("=" * 50)
    
    for i, (test_name, _) in enumerate(tests):
        status = "✅ PASÓ" if results[i] else "❌ FALLÓ"
        print(f"{i+1}. {test_name}: {status}")
    
    passed = sum(results)
    total = len(results)
    
    print(f"\n🎯 Resultado: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron! El caso práctico San Miguel está listo.")
        print("💡 Puedes ejecutar: streamlit run APP.py")
    else:
        print("⚠️ Algunas pruebas fallaron. Revisa los errores arriba.")
        print("💡 Instala las dependencias faltantes con: pip install -r requirements.txt")

if __name__ == "__main__":
    main() 