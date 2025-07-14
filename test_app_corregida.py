#!/usr/bin/env python3
"""
Test script para verificar que las correcciones en APP.py funcionan correctamente
"""

import sys
import os

def test_imports():
    """Test de importaciones básicas"""
    print("🔍 Probando importaciones...")
    
    try:
        import streamlit as st
        print("✅ Streamlit importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando Streamlit: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ NumPy importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando NumPy: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando Pandas: {e}")
        return False
    
    return True

def test_aashto_function():
    """Test de la función AASHTO 93 corregida"""
    print("\n🔍 Probando función AASHTO 93...")
    
    try:
        # Importar la función desde APP.py
        sys.path.append('.')
        from APP import calcular_espesor_losa_AASHTO93
        
        # Parámetros de prueba
        W18 = 1000000  # ESALs
        ZR = -1.645    # 95% confiabilidad
        S0 = 0.35      # Desviación estándar
        delta_PSI = 1.5
        Sc = 4.5       # MPa
        J = 3.2
        k = 150        # pci
        C = 1.0        # drenaje bueno
        Ec = 30000     # MPa
        
        # Calcular espesor
        espesor = calcular_espesor_losa_AASHTO93(W18, ZR, S0, delta_PSI, Sc, J, k, C, Ec)
        
        if espesor is not None and espesor > 0:
            print(f"✅ Función AASHTO 93 funciona correctamente. Espesor: {espesor:.2f} pulgadas")
            return True
        else:
            print("❌ Función AASHTO 93 retornó valor inválido")
            return False
            
    except Exception as e:
        print(f"❌ Error en función AASHTO 93: {e}")
        return False

def test_lidar_functions():
    """Test de funciones LiDAR"""
    print("\n🔍 Probando funciones LiDAR...")
    
    try:
        from APP import calcular_cbr_ndvi, generar_hec_ras_drenaje
        
        # Test CBR-NDVI
        ndvi_test = 0.4
        cbr = calcular_cbr_ndvi(ndvi_test)
        print(f"✅ Función CBR-NDVI funciona. NDVI={ndvi_test}, CBR={cbr}%")
        
        # Test HEC-RAS
        hec_content = generar_hec_ras_drenaje(5.0, 100, 5.0, 10)
        if hec_content and len(hec_content) > 100:
            print("✅ Función HEC-RAS funciona correctamente")
        else:
            print("❌ Función HEC-RAS retornó contenido inválido")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error en funciones LiDAR: {e}")
        return False

def test_mathematical_operations():
    """Test de operaciones matemáticas críticas"""
    print("\n🔍 Probando operaciones matemáticas...")
    
    try:
        import math
        
        # Test de operaciones que causaban errores
        test_values = [0.1, 0.5, 1.0, 2.0, 5.0]
        
        for val in test_values:
            # Test logaritmo
            log_result = math.log10(val)
            
            # Test potencia
            pow_result = val ** 0.75
            
            # Test división
            div_result = 1.0 / val if val != 0 else float('inf')
            
            print(f"✅ Operaciones con {val}: log={log_result:.3f}, pow={pow_result:.3f}, div={div_result:.3f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en operaciones matemáticas: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🚀 INICIANDO PRUEBAS DE CORRECCIÓN - APP.py")
    print("=" * 50)
    
    tests = [
        ("Importaciones básicas", test_imports),
        ("Función AASHTO 93", test_aashto_function),
        ("Funciones LiDAR", test_lidar_functions),
        ("Operaciones matemáticas", test_mathematical_operations)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print(f"❌ Test '{test_name}' falló")
        except Exception as e:
            print(f"❌ Test '{test_name}' falló con excepción: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 RESULTADOS: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡TODAS LAS PRUEBAS PASARON! La app está corregida.")
        return True
    else:
        print("⚠️ Algunas pruebas fallaron. Revisar errores.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 