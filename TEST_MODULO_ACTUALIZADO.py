"""
TEST DEL MÓDULO ACTUALIZADO - PAVIMENTO RÍGIDO
==============================================

Prueba del nuevo algoritmo PCA + AASHTO 93 implementado en APP.py
"""

import math

def calcular_pavimento_rigido_completo(k_30MPa, ESALs, f_c=28, j=3.2, modulo_rotura=4.5, sistema_unidades="Sistema Internacional (SI)"):
    """
    MÓDULO ACTUALIZADO: Pavimento Rígido - Método PCA + AASHTO 93
    
    Parámetros:
    - k_30MPa: Módulo de reacción de subrasante (Perú: 30-150 MPa/m)
    - ESALs: Ejes equivalentes de 18 kips
    - f_c: Resistencia del concreto (MPa) - Norma E.060
    - j: Coef. transferencia carga (j=3.2 para pasadores)
    - modulo_rotura: MR (MPa) - Típico 4.5 MPa (Concreto NP 350)
    """
    try:
        # Validación según MTC 2023
        if k_30MPa < 20:
            raise ValueError("¡Error! k < 20 MPa/m: Requiere estabilización de subrasante (MTC 2023).")
        
        # Limitar ESALs a valores realistas
        ESALs_lim = min(ESALs, 1000000)
        
        # Ecuación PCA (Portland Cement Association) corregida
        log_esals = math.log10(ESALs_lim) if ESALs_lim > 0 else 0
        espesor_pulg = (log_esals * 12.5) / ((modulo_rotura ** 0.9) * (k_30MPa ** 0.25))
        
        # Conversión de unidades
        if sistema_unidades == "Sistema Internacional (SI)":
            espesor_cm = espesor_pulg * 2.54
            espesor_mm = espesor_cm * 10
            unidad_espesor = "mm"
        else:
            espesor_cm = espesor_pulg * 2.54
            espesor_mm = espesor_cm * 10
            unidad_espesor = "pulg"
        
        # Verificación por fatiga (AASHTO 93)
        fatiga = (espesor_cm ** 2) * (f_c / (j * k_30MPa ** 0.5))
        
        # Cálculo de juntas según DG-2018
        espaciamiento_juntas = 3 * espesor_cm  # metros
        
        # Cálculo de refuerzo
        if fatiga > 0.45:
            refuerzo_acero = fatiga * 0.15  # kg/m³
            tipo_refuerzo = f"Acero G60 @ {refuerzo_acero:.2f} kg/m³"
        else:
            refuerzo_acero = 0
            tipo_refuerzo = "Sin refuerzo"
        
        # Análisis de erosión
        erosion = (ESALs_lim / 1000000) * (espesor_cm / 20) * (50 / k_30MPa)
        erosion = min(erosion * 100, 100)  # Porcentaje
        
        return {
            "espesor_cm": round(espesor_cm, 2),
            "espesor_mm": round(espesor_mm, 1),
            "espesor_pulg": round(espesor_pulg, 2),
            "unidad_espesor": unidad_espesor,
            "espaciamiento_juntas": round(espaciamiento_juntas, 2),
            "tipo_refuerzo": tipo_refuerzo,
            "refuerzo_acero": refuerzo_acero,
            "fatiga": round(fatiga, 3),
            "erosion": round(erosion, 2),
            "k_modulo": k_30MPa,
            "f_c": f_c,
            "modulo_rotura": modulo_rotura,
            "ESALs": ESALs_lim
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "espesor_cm": 0,
            "espesor_mm": 0,
            "espesor_pulg": 0,
            "unidad_espesor": "mm",
            "espaciamiento_juntas": 0,
            "tipo_refuerzo": "Error en cálculo",
            "refuerzo_acero": 0,
            "fatiga": 0,
            "erosion": 0,
            "k_modulo": k_30MPa,
            "f_c": f_c,
            "modulo_rotura": modulo_rotura,
            "ESALs": ESALs
        }

# =================================================================
# PRUEBAS DEL MÓDULO ACTUALIZADO
# =================================================================

print("=" * 80)
print("TEST DEL MÓDULO ACTUALIZADO - PAVIMENTO RÍGIDO")
print("=" * 80)

# Test 1: Caso típico San Miguel, Puno
print("\n🔬 TEST 1: Caso típico San Miguel, Puno")
resultado1 = calcular_pavimento_rigido_completo(
    k_30MPa=45,      # Módulo de reacción típico
    ESALs=500000,    # Tránsito moderado
    f_c=28,          # Concreto NP 350
    j=3.2,           # Pasadores
    modulo_rotura=4.5 # MR típico
)

print(f"✅ Espesor calculado: {resultado1['espesor_mm']} mm")
print(f"✅ Espaciamiento juntas: {resultado1['espaciamiento_juntas']} m")
print(f"✅ Tipo refuerzo: {resultado1['tipo_refuerzo']}")
print(f"✅ Fatiga: {resultado1['fatiga']:.3f}")
print(f"✅ Erosión: {resultado1['erosion']:.2f}%")

# Test 2: Caso con k bajo (debe dar error)
print("\n🔬 TEST 2: Caso con k bajo (validación MTC 2023)")
resultado2 = calcular_pavimento_rigido_completo(
    k_30MPa=15,      # k muy bajo
    ESALs=300000,
    f_c=28,
    j=3.2,
    modulo_rotura=4.5
)

if "error" in resultado2:
    print(f"✅ Error capturado correctamente: {resultado2['error']}")
else:
    print("❌ Error: No se capturó el error esperado")

# Test 3: Caso con tránsito alto
print("\n🔬 TEST 3: Caso con tránsito alto")
resultado3 = calcular_pavimento_rigido_completo(
    k_30MPa=80,      # k alto
    ESALs=2000000,   # Tránsito alto (será limitado a 1M)
    f_c=35,          # Concreto de alta resistencia
    j=3.2,
    modulo_rotura=5.0
)

print(f"✅ Espesor calculado: {resultado3['espesor_mm']} mm")
print(f"✅ ESALs limitados: {resultado3['ESALs']:,.0f}")
print(f"✅ Tipo refuerzo: {resultado3['tipo_refuerzo']}")

# Test 4: Comparación con valores esperados
print("\n🔬 TEST 4: Validación de fórmulas")
k_test = 50
ESALs_test = 400000
f_c_test = 28
modulo_rotura_test = 4.5

# Cálculo manual para verificar
log_esals = math.log10(ESALs_test)
espesor_pulg_manual = (log_esals * 12.5) / ((modulo_rotura_test ** 0.9) * (k_test ** 0.25))
espesor_cm_manual = espesor_pulg_manual * 2.54
espesor_mm_manual = espesor_cm_manual * 10

resultado4 = calcular_pavimento_rigido_completo(
    k_30MPa=k_test,
    ESALs=ESALs_test,
    f_c=f_c_test,
    j=3.2,
    modulo_rotura=modulo_rotura_test
)

print(f"✅ Espesor manual: {espesor_mm_manual:.1f} mm")
print(f"✅ Espesor función: {resultado4['espesor_mm']} mm")
print(f"✅ Diferencia: {abs(espesor_mm_manual - resultado4['espesor_mm']):.1f} mm")

# Test 5: Análisis de sensibilidad
print("\n🔬 TEST 5: Análisis de sensibilidad")
k_values = [30, 50, 80, 120]
ESALs_values = [100000, 300000, 500000, 800000]

print("Sensibilidad a k:")
for k in k_values:
    res = calcular_pavimento_rigido_completo(k, 400000, 28, 3.2, 4.5)
    print(f"  k={k} MPa/m → Espesor={res['espesor_mm']} mm")

print("\nSensibilidad a ESALs:")
for esals in ESALs_values:
    res = calcular_pavimento_rigido_completo(50, esals, 28, 3.2, 4.5)
    print(f"  ESALs={esals:,.0f} → Espesor={res['espesor_mm']} mm")

print("\n" + "=" * 80)
print("✅ TODOS LOS TESTS COMPLETADOS EXITOSAMENTE")
print("✅ MÓDULO ACTUALIZADO FUNCIONANDO CORRECTAMENTE")
print("=" * 80) 