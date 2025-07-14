#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT DE PRUEBA - APP MEJORADA
================================

Prueba las nuevas funcionalidades avanzadas de la aplicación:
1. Procesamiento LiDAR (demo)
2. Diseño automatizado de pavimentos
3. Validación normativa peruana
4. Análisis de fatiga PCA
5. Exportación a Civil 3D (demo)
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_procesamiento_lidar():
    """Prueba la función de procesamiento LiDAR"""
    print("🧪 Probando procesamiento LiDAR...")
    
    try:
        # Importar la función desde APP.py
        from APP import procesar_nube_puntos
        
        # Probar con archivo simulado
        resultado = procesar_nube_puntos("test_data.las")
        
        # Verificar que el resultado tiene la estructura esperada
        campos_requeridos = ["Área_ha", "Pendiente_%", "Zonas_inestables", "Estado"]
        for campo in campos_requeridos:
            if campo not in resultado:
                print(f"❌ Campo '{campo}' no encontrado en resultado")
                return False
        
        print(f"✅ Procesamiento LiDAR exitoso: {resultado['Estado']}")
        return True
        
    except Exception as e:
        print(f"❌ Error en procesamiento LiDAR: {e}")
        return False

def test_diseno_rigido():
    """Prueba la función de diseño rígido"""
    print("🧪 Probando diseño rígido...")
    
    try:
        from APP import diseno_rigido
        
        # Parámetros de prueba
        k = 50  # MPa/m
        ESALs = 100000
        resistencia = 28  # MPa
        clima = "sierra"
        
        resultado = diseno_rigido(k, ESALs, resistencia, clima)
        
        # Verificar estructura del resultado
        campos_requeridos = ["Espesor", "Juntas", "Factor_climatico", "Estado"]
        for campo in campos_requeridos:
            if campo not in resultado:
                print(f"❌ Campo '{campo}' no encontrado en resultado")
                return False
        
        print(f"✅ Diseño rígido exitoso: {resultado['Estado']}")
        print(f"   Espesor: {resultado['Espesor']}")
        print(f"   Factor climático: {resultado['Factor_climatico']}")
        return True
        
    except Exception as e:
        print(f"❌ Error en diseño rígido: {e}")
        return False

def test_diseno_flexible():
    """Prueba la función de diseño flexible"""
    print("🧪 Probando diseño flexible...")
    
    try:
        from APP import diseno_flexible
        
        # Parámetros de prueba
        CBR = 8  # %
        ESALs = 100000
        tipo_suelo = "volcánico"
        clima = "sierra"
        
        resultado = diseno_flexible(CBR, ESALs, tipo_suelo, clima)
        
        # Verificar estructura del resultado
        campos_requeridos = ["Base", "Subbase", "SN_total", "Estado"]
        for campo in campos_requeridos:
            if campo not in resultado:
                print(f"❌ Campo '{campo}' no encontrado en resultado")
                return False
        
        print(f"✅ Diseño flexible exitoso: {resultado['Estado']}")
        print(f"   Base: {resultado['Base']}")
        print(f"   SN total: {resultado['SN_total']}")
        return True
        
    except Exception as e:
        print(f"❌ Error en diseño flexible: {e}")
        return False

def test_validacion_normativa():
    """Prueba la función de validación normativa"""
    print("🧪 Probando validación normativa...")
    
    try:
        from APP import validar_normativa_peruana
        
        # Parámetros de prueba
        espesor_cm = 25
        CBR_subbase = 25
        pendiente_cuneta = 2.5
        tipo_pavimento = "rigido"
        
        validaciones = validar_normativa_peruana(espesor_cm, CBR_subbase, pendiente_cuneta, tipo_pavimento)
        
        # Verificar que hay validaciones
        if len(validaciones) == 0:
            print("❌ No se generaron validaciones")
            return False
        
        print(f"✅ Validación normativa exitosa: {len(validaciones)} validaciones")
        for v in validaciones:
            print(f"   {v}")
        return True
        
    except Exception as e:
        print(f"❌ Error en validación normativa: {e}")
        return False

def test_analisis_fatiga():
    """Prueba la función de análisis de fatiga"""
    print("🧪 Probando análisis de fatiga PCA...")
    
    try:
        from APP import analisis_fatiga_pca
        
        # Parámetros de prueba
        ESALs = 100000
        resistencia_concreto = 28
        espesor_cm = 25
        
        resultado = analisis_fatiga_pca(ESALs, resistencia_concreto, espesor_cm)
        
        # Verificar estructura del resultado
        campos_requeridos = ["Tension_maxima", "Daño_acumulado", "Estado_losa", "Estado"]
        for campo in campos_requeridos:
            if campo not in resultado:
                print(f"❌ Campo '{campo}' no encontrado en resultado")
                return False
        
        print(f"✅ Análisis de fatiga exitoso: {resultado['Estado']}")
        print(f"   Estado de losa: {resultado['Estado_losa']}")
        print(f"   Daño acumulado: {resultado['Daño_acumulado']}")
        return True
        
    except Exception as e:
        print(f"❌ Error en análisis de fatiga: {e}")
        return False

def test_exportacion_civil3d():
    """Prueba la función de exportación a Civil 3D"""
    print("🧪 Probando exportación a Civil 3D...")
    
    try:
        from APP import exportar_a_civil3d
        
        # Parámetros de prueba
        espesor = 25
        ruta_dwg = "C:/test/pavimento.dwg"
        
        resultado = exportar_a_civil3d(espesor, ruta_dwg)
        
        # Verificar estructura del resultado
        campos_requeridos = ["Archivo_DWG", "Capas_creadas", "Estado"]
        for campo in campos_requeridos:
            if campo not in resultado:
                print(f"❌ Campo '{campo}' no encontrado en resultado")
                return False
        
        print(f"✅ Exportación a Civil 3D exitosa: {resultado['Estado']}")
        print(f"   Archivo: {resultado['Archivo_DWG']}")
        print(f"   Capas creadas: {len(resultado['Capas_creadas'])}")
        return True
        
    except Exception as e:
        print(f"❌ Error en exportación Civil 3D: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🚀 INICIANDO PRUEBAS DE LA APP MEJORADA")
    print("=" * 50)
    
    # Lista de pruebas
    pruebas = [
        test_procesamiento_lidar,
        test_diseno_rigido,
        test_diseno_flexible,
        test_validacion_normativa,
        test_analisis_fatiga,
        test_exportacion_civil3d
    ]
    
    # Ejecutar pruebas
    resultados = []
    for prueba in pruebas:
        try:
            resultado = prueba()
            resultados.append(resultado)
        except Exception as e:
            print(f"❌ Error ejecutando prueba: {e}")
            resultados.append(False)
        print()
    
    # Resumen de resultados
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 50)
    exitos = sum(resultados)
    total = len(resultados)
    
    print(f"✅ Pruebas exitosas: {exitos}/{total}")
    print(f"❌ Pruebas fallidas: {total - exitos}/{total}")
    
    if exitos == total:
        print("🎉 ¡TODAS LAS PRUEBAS PASARON! La app está funcionando correctamente.")
        return True
    else:
        print("⚠️ Algunas pruebas fallaron. Revisar errores arriba.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 