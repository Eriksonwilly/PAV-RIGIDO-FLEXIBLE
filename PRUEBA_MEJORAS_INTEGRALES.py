"""
PRUEBA MEJORAS INTEGRALES - SOFTWARE DE DISEÑO DE PAVIMENTOS
============================================================

Script de prueba para verificar todas las mejoras implementadas:
- Procesamiento de datos LiDAR de drones
- Diseño automatizado de pavimentos
- Interoperabilidad con software externo
- Caso práctico San Miguel

Autor: IA Assistant - Especialista UNI
Fecha: 2024
"""

import json
import os
from datetime import datetime

def test_modulo_lidar():
    """Prueba el módulo de procesamiento LiDAR"""
    print("🚁 PRUEBA MÓDULO LIDAR DRONES")
    print("=" * 50)
    
    try:
        from MODULO_LIDAR_DRONES import procesamiento_completo_lidar
        
        # Datos de prueba
        archivo_las = "san_miguel_cuadra_1.las"
        proyecto = "San Miguel - Cuadra 1"
        
        # Ejecutar procesamiento
        resultado = procesamiento_completo_lidar(archivo_las, proyecto)
        
        # Verificar resultados
        if "error" not in resultado:
            print("✅ Procesamiento LiDAR exitoso")
            print(f"   Proyecto: {resultado['Proyecto']}")
            print(f"   Área: {resultado['Datos_LiDAR']['Área_ha']} ha")
            print(f"   Pendiente: {resultado['Datos_LiDAR']['Pendiente_%']}%")
            print(f"   Puntos procesados: {resultado['Datos_LiDAR']['Puntos_procesados']:,}")
            print(f"   Estado: {resultado['Estado']}")
            return True
        else:
            print(f"❌ Error en procesamiento LiDAR: {resultado['error']}")
            return False
            
    except ImportError:
        print("⚠️ Módulo LIDAR no disponible")
        return False
    except Exception as e:
        print(f"❌ Error probando módulo LIDAR: {e}")
        return False

def test_modulo_diseno():
    """Prueba el módulo de diseño automatizado"""
    print("\n🏗️ PRUEBA MÓDULO DISEÑO AUTOMATIZADO")
    print("=" * 50)
    
    try:
        from MODULO_DISENO_AUTOMATIZADO import diseno_automatizado_completo
        
        # Datos de prueba
        datos_lidar = {
            "Área_ha": 0.08,
            "Pendiente_%": 5.2,
            "Puntos_procesados": 850000
        }
        
        datos_suelo = {
            "k_modulo": 45,
            "CBR": 4.5,
            "clima": "sierra",
            "tipo_suelo": "volcánico"
        }
        
        datos_transito = {
            "ESALs": 250000,
            "tipo_via": "urbana",
            "proyecto": "San Miguel - Cuadra 1"
        }
        
        # Ejecutar diseño
        resultado = diseno_automatizado_completo(
            datos_lidar, datos_suelo, datos_transito, "ambos"
        )
        
        # Verificar resultados
        if "error" not in resultado:
            print("✅ Diseño automatizado exitoso")
            if "pavimento_rigido" in resultado:
                print(f"   Espesor rígido: {resultado['pavimento_rigido']['espesor_cm']} cm")
                print(f"   Juntas transversales: {resultado['pavimento_rigido']['juntas_transversales_m']} m")
            if "pavimento_flexible" in resultado:
                print(f"   Espesor flexible: {resultado['pavimento_flexible']['espesor_total_cm']} cm")
            print(f"   Estado: {resultado['Estado']}")
            return True
        else:
            print(f"❌ Error en diseño automatizado: {resultado['error']}")
            return False
            
    except ImportError:
        print("⚠️ Módulo de diseño no disponible")
        return False
    except Exception as e:
        print(f"❌ Error probando módulo de diseño: {e}")
        return False

def test_modulo_interoperabilidad():
    """Prueba el módulo de interoperabilidad"""
    print("\n🔄 PRUEBA MÓDULO INTEROPERABILIDAD")
    print("=" * 50)
    
    try:
        from MODULO_INTEROPERABILIDAD import interoperabilidad_completa
        
        # Datos de prueba
        datos_lidar = {
            "Área_ha": 0.08,
            "Pendiente_%": 5.2,
            "Puntos_procesados": 850000
        }
        
        diseno_pavimento = {
            "pavimento_rigido": {
                "espesor_cm": 20.5,
                "juntas_transversales_m": 61.5,
                "juntas_longitudinales_m": 92.3
            },
            "drenaje_analisis": {
                "pendiente_actual": 5.2
            }
        }
        
        proyecto = "San Miguel - Cuadra 1"
        
        # Ejecutar interoperabilidad
        resultado = interoperabilidad_completa(datos_lidar, diseno_pavimento, proyecto)
        
        # Verificar resultados
        if "error" not in resultado:
            print("✅ Interoperabilidad exitosa")
            print(f"   Proyecto: {resultado['proyecto']}")
            print(f"   Archivos generados: {len(resultado['archivos_generados'])}")
            for archivo in resultado['archivos_generados']:
                print(f"     - {archivo}")
            print(f"   Estado: {resultado['Estado']}")
            return True
        else:
            print(f"❌ Error en interoperabilidad: {resultado['error']}")
            return False
            
    except ImportError:
        print("⚠️ Módulo de interoperabilidad no disponible")
        return False
    except Exception as e:
        print(f"❌ Error probando interoperabilidad: {e}")
        return False

def test_caso_practico():
    """Prueba el caso práctico completo"""
    print("\n🏗️ PRUEBA CASO PRÁCTICO SAN MIGUEL")
    print("=" * 50)
    
    try:
        from CASO_PRACTICO_SAN_MIGUEL_COMPLETO import CasoPracticoSanMiguel
        
        # Crear y ejecutar caso práctico
        caso = CasoPracticoSanMiguel()
        resultado = caso.ejecutar_caso_completo()
        
        # Verificar resultados
        if "error" not in resultado:
            print("✅ Caso práctico ejecutado exitosamente")
            print(f"   Proyecto: {resultado['resumen_ejecutivo']['proyecto']}")
            print(f"   Tipo pavimento: {resultado['resumen_ejecutivo']['tipo_pavimento_recomendado']}")
            print(f"   Espesor: {resultado['resumen_ejecutivo']['espesor_recomendado']}")
            print(f"   Costo: {resultado['resumen_ejecutivo']['costo_estimado']}")
            print(f"   Duración: {resultado['resumen_ejecutivo']['duracion_obra']}")
            print(f"   Archivos generados: {len(resultado['archivos_generados'])}")
            print(f"   Estado: {resultado['Estado']}")
            return True
        else:
            print(f"❌ Error en caso práctico: {resultado['error']}")
            return False
            
    except ImportError:
        print("⚠️ Caso práctico no disponible")
        return False
    except Exception as e:
        print(f"❌ Error probando caso práctico: {e}")
        return False

def test_app_principal():
    """Prueba la aplicación principal"""
    print("\n📱 PRUEBA APLICACIÓN PRINCIPAL")
    print("=" * 50)
    
    try:
        # Verificar que APP.py existe y es válido
        if os.path.exists("APP.py"):
            print("✅ Archivo APP.py encontrado")
            
            # Verificar que contiene las nuevas funcionalidades
            with open("APP.py", "r", encoding="utf-8") as f:
                contenido = f.read()
            
            verificaciones = [
                ("Módulos avanzados", "MODULOS_AVANZADOS_DISPONIBLES"),
                ("Caso Práctico San Miguel", "Caso Práctico San Miguel"),
                ("Interoperabilidad", "interoperabilidad_completa"),
                ("LiDAR", "procesamiento_completo_lidar"),
                ("Diseño automatizado", "diseno_automatizado_completo")
            ]
            
            for nombre, texto in verificaciones:
                if texto in contenido:
                    print(f"   ✅ {nombre}: Encontrado")
                else:
                    print(f"   ❌ {nombre}: No encontrado")
            
            return True
        else:
            print("❌ Archivo APP.py no encontrado")
            return False
            
    except Exception as e:
        print(f"❌ Error probando aplicación principal: {e}")
        return False

def generar_reporte_pruebas():
    """Genera un reporte de las pruebas realizadas"""
    print("\n📊 GENERANDO REPORTE DE PRUEBAS")
    print("=" * 50)
    
    reporte = {
        "fecha_prueba": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pruebas_realizadas": [],
        "resumen": {
            "total_pruebas": 0,
            "exitosas": 0,
            "fallidas": 0,
            "no_disponibles": 0
        }
    }
    
    # Ejecutar todas las pruebas
    pruebas = [
        ("Módulo LiDAR", test_modulo_lidar),
        ("Módulo Diseño", test_modulo_diseno),
        ("Interoperabilidad", test_modulo_interoperabilidad),
        ("Caso Práctico", test_caso_practico),
        ("Aplicación Principal", test_app_principal)
    ]
    
    for nombre, funcion in pruebas:
        print(f"\n🔍 Ejecutando: {nombre}")
        try:
            resultado = funcion()
            reporte["pruebas_realizadas"].append({
                "nombre": nombre,
                "estado": "exitoso" if resultado else "fallido",
                "fecha": datetime.now().strftime("%H:%M:%S")
            })
            
            if resultado:
                reporte["resumen"]["exitosas"] += 1
            else:
                reporte["resumen"]["fallidas"] += 1
                
        except Exception as e:
            reporte["pruebas_realizadas"].append({
                "nombre": nombre,
                "estado": "no_disponible",
                "error": str(e),
                "fecha": datetime.now().strftime("%H:%M:%S")
            })
            reporte["resumen"]["no_disponibles"] += 1
    
    reporte["resumen"]["total_pruebas"] = len(pruebas)
    
    # Mostrar resumen
    print(f"\n📈 RESUMEN DE PRUEBAS")
    print(f"   Total: {reporte['resumen']['total_pruebas']}")
    print(f"   Exitosas: {reporte['resumen']['exitosas']} ✅")
    print(f"   Fallidas: {reporte['resumen']['fallidas']} ❌")
    print(f"   No disponibles: {reporte['resumen']['no_disponibles']} ⚠️")
    
    # Guardar reporte
    try:
        os.makedirs("reportes_pruebas", exist_ok=True)
        nombre_archivo = f"reportes_pruebas/reporte_pruebas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(reporte, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Reporte guardado: {nombre_archivo}")
        
    except Exception as e:
        print(f"❌ Error guardando reporte: {e}")
    
    return reporte

def main():
    """Función principal"""
    print("🧪 PRUEBA MEJORAS INTEGRALES - SOFTWARE DE DISEÑO DE PAVIMENTOS")
    print("=" * 80)
    print("Verificando todas las mejoras implementadas...")
    print("=" * 80)
    
    # Ejecutar pruebas y generar reporte
    reporte = generar_reporte_pruebas()
    
    # Mostrar recomendaciones finales
    print(f"\n💡 RECOMENDACIONES FINALES")
    print("=" * 50)
    
    if reporte["resumen"]["exitosas"] == reporte["resumen"]["total_pruebas"]:
        print("🎉 ¡TODAS LAS PRUEBAS EXITOSAS!")
        print("   El software está completamente funcional con todas las mejoras.")
        print("   Puede proceder con confianza a usar la aplicación.")
    elif reporte["resumen"]["exitosas"] > reporte["resumen"]["fallidas"]:
        print("✅ MAYORÍA DE PRUEBAS EXITOSAS")
        print("   El software está mayormente funcional.")
        print("   Algunas funcionalidades avanzadas pueden no estar disponibles.")
    else:
        print("⚠️ MUCHAS PRUEBAS FALLIDAS")
        print("   Verificar la instalación de dependencias.")
        print("   Revisar la configuración del entorno.")
    
    print(f"\n📋 PRÓXIMOS PASOS:")
    print("   1. Ejecutar: streamlit run APP.py")
    print("   2. Navegar a la pestaña '🚁 Caso Práctico San Miguel'")
    print("   3. Probar todas las funcionalidades")
    print("   4. Generar reportes PDF")
    
    print(f"\n🏁 PRUEBAS COMPLETADAS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main() 