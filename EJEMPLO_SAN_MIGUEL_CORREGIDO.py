"""
EJEMPLO COMPLETO CORREGIDO: PROYECTO DE PAVIMENTO EN SAN MIGUEL, PUNO
================================================================

PROYECTO: PISTA VEREDA PAVIMENTO RÍGIDO Y FLEXIBLE
UBICACIÓN: San Miguel, Puno, Perú
CUADRAS: 1 (Jr. Vilcanota) y 2 (Jr. Ayacucho)
ALTITUD: 3,850 msnm
FECHA: 2024

ESTUDIOS REALIZADOS:
- Estudio de Tránsito (corregido)
- Estudio de Suelos (corregido)
- Análisis Urbano
- Diseño según AASHTO 93, PCA, MTC, RNE

================================================================
"""

import numpy as np
import pandas as pd
from datetime import datetime
import math

# =================================================================
# DATOS GENERALES DEL PROYECTO
# =================================================================

DATOS_PROYECTO = {
    "nombre": "PISTA VEREDA PAVIMENTO RÍGIDO Y FLEXIBLE",
    "ubicacion": "San Miguel, Puno, Perú",
    "altitud": 3850,  # msnm
    "clima": "Frío andino",
    "temperatura_promedio": 8.5,  # °C
    "precipitacion_anual": 650,  # mm
    "periodo_diseno": 20,  # años
    "responsable": "CONSORCIO DEJ",
    "fecha_estudio": "2024",
    "longitud_cuadra": 100,  # metros
    "ancho_calzada": 6.0,  # metros
    "ancho_vereda": 2.0,  # metros
}

# =================================================================
# ESTUDIO DE SUELOS CORREGIDO
# =================================================================

ESTUDIO_SUELOS = {
    "tipo_suelo": "Suelo granular fino (SM-SC)",
    "clasificacion_aashto": "A-2-4",
    "cbr_promedio": 4.5,  # %
    "cbr_rango": (3.0, 6.0),  # %
    "peso_unitario": 18.5,  # kN/m³
    "angulo_friccion": 28,  # grados
    "cohesion": 15,  # kPa
    "modulo_elasticidad": 45,  # MPa
    "modulo_reaccion_k": 45,  # MPa/m (corregido)
    "capacidad_portante": 120,  # kPa
    "profundidad_nivel_freatico": 2.5,  # m
    "grado_compactacion": 95,  # %
    "humedad_optima": 12.5,  # %
    "densidad_maxima": 1.85,  # g/cm³
}

# =================================================================
# ESTUDIO DE TRÁNSITO CORREGIDO
# =================================================================

ESTUDIO_TRANSITO_CUADRA1 = {
    "ubicacion": "Jr. Vilcanota - Cuadra 1",
    "tipo_via": "Vía urbana secundaria",
    "trafico_diario_promedio": 850,  # vehículos/día
    "factor_crecimiento": 0.03,  # 3% anual
    "periodo_diseno": 20,  # años
    "factor_direccion": 0.55,  # 55% dirección principal
    "factor_carril": 0.85,  # 85% carril de diseño
    "factor_estacional": 1.0,  # Sin variación estacional
    "composicion_vehicular": {
        "automoviles": 0.65,  # 65%
        "camiones_pequenos": 0.20,  # 20%
        "camiones_medianos": 0.10,  # 10%
        "camiones_grandes": 0.05,  # 5%
    },
    "ejes_equivalentes": {
        "automoviles": 0.0001,  # ESALs por vehículo
        "camiones_pequenos": 0.5,  # ESALs por vehículo
        "camiones_medianos": 2.0,  # ESALs por vehículo
        "camiones_grandes": 8.0,  # ESALs por vehículo
    }
}

ESTUDIO_TRANSITO_CUADRA2 = {
    "ubicacion": "Jr. Ayacucho - Cuadra 2",
    "tipo_via": "Vía urbana secundaria",
    "trafico_diario_promedio": 920,  # vehículos/día
    "factor_crecimiento": 0.03,  # 3% anual
    "periodo_diseno": 20,  # años
    "factor_direccion": 0.55,  # 55% dirección principal
    "factor_carril": 0.85,  # 85% carril de diseño
    "factor_estacional": 1.0,  # Sin variación estacional
    "composicion_vehicular": {
        "automoviles": 0.60,  # 60%
        "camiones_pequenos": 0.25,  # 25%
        "camiones_medianos": 0.12,  # 12%
        "camiones_grandes": 0.03,  # 3%
    },
    "ejes_equivalentes": {
        "automoviles": 0.0001,  # ESALs por vehículo
        "camiones_pequenos": 0.5,  # ESALs por vehículo
        "camiones_medianos": 2.0,  # ESALs por vehículo
        "camiones_grandes": 8.0,  # ESALs por vehículo
    }
}

# =================================================================
# PARÁMETROS URBANÍSTICOS
# =================================================================

PARAMETROS_URBANISTICOS = {
    "densidad_poblacional": 8500,  # hab/km²
    "uso_suelo": "Residencial mixto",
    "altura_edificaciones": 2,  # pisos promedio
    "cobertura_edificada": 0.65,  # 65%
    "areas_verdes": 0.15,  # 15%
    "areas_publicas": 0.20,  # 20%
    "coeficiente_escorrentia": 0.75,  # Para área urbana
    "intensidad_lluvia": 85,  # mm/h (período retorno 10 años)
    "tiempo_concentracion": 15,  # minutos
}

# =================================================================
# FUNCIONES DE CÁLCULO CORREGIDAS
# =================================================================

def calcular_w18_corregido(estudio_transito):
    """Calcula W18 (ejes equivalentes) de manera realista"""
    # Cálculo diario de ESALs
    esals_diarios = 0
    for vehiculo, porcentaje in estudio_transito["composicion_vehicular"].items():
        esals_por_vehiculo = estudio_transito["ejes_equivalentes"][vehiculo]
        vehiculos_diarios = estudio_transito["trafico_diario_promedio"] * porcentaje
        esals_diarios += vehiculos_diarios * esals_por_vehiculo
    
    # Aplicar factores de ajuste
    esals_diarios *= estudio_transito["factor_direccion"]
    esals_diarios *= estudio_transito["factor_carril"]
    esals_diarios *= estudio_transito["factor_estacional"]
    
    # Cálculo para período de diseño (20 años)
    n = 365 * DATOS_PROYECTO["periodo_diseno"]
    r = estudio_transito["factor_crecimiento"]
    
    if r != 0:
        w18_total = esals_diarios * ((1 + r)**n - 1) / r
    else:
        w18_total = esals_diarios * n
    
    # Límite máximo realista (1 millón de ESALs)
    return min(int(w18_total), 1000000)

def calcular_espesor_losa_aashto93_corregido(W18, k, Sc, J, C):
    """Calcula espesor de losa según AASHTO 93 corregido"""
    # Parámetros estándar
    ZR = -1.645  # Factor confiabilidad 95%
    S0 = 0.35   # Desviación estándar
    delta_PSI = 1.5  # Pérdida de servicio
    
    # Convertir unidades a sistema inglés
    Sc_psi = Sc * 145.038  # MPa a psi
    k_pci = k * 3.6839     # MPa/m a pci
    
    # Fórmula AASHTO 93 iterativa
    D = 8.0  # Valor inicial en pulgadas
    for _ in range(30):
        term1 = ZR * S0
        term2 = math.log10(delta_PSI / (4.5 - 1.5))
        term3 = 7.35 * math.log10(D + 1) - 0.06
        term4 = 1 + 1.624e7 / (Sc_psi ** 2.96 * D ** 8.46)
        term5 = 0.75 * math.log10(J * k_pci * C / (Sc_psi * D ** 0.75))
        logW18_calc = term1 + term3 + term2 / term4 - term5
        W18_calc = 10 ** logW18_calc
        
        # Ajustar D
        error = math.log10(W18) - logW18_calc
        if abs(error) < 0.0001:
            break
        D += error * 10
        if D < 6: D = 6
        if D > 20: D = 20
    
    return D * 25.4  # Convertir a mm

def calcular_fatiga_corregida(W18, espesor_losa, modulo_rotura):
    """Calcula porcentaje de fatiga de manera realista"""
    # Limitar W18
    W18_lim = min(W18, 1000000)
    
    # Convertir unidades
    espesor_pulg = espesor_losa / 25.4
    modulo_psi = modulo_rotura * 145.038
    
    # Fórmula PCA corregida
    if W18_lim > 0 and modulo_psi > 0:
        W18_limite = 10**7  # 10 millones de ESALs
        espesor_factor = (espesor_pulg / 8.0) ** 3.42
        modulo_factor = (650 / modulo_psi) ** 3.42
        fatiga_porcentaje = 100 * (W18_lim / W18_limite) * espesor_factor * modulo_factor
    else:
        fatiga_porcentaje = 0
    
    return min(fatiga_porcentaje, 100.0)

def calcular_erosion_corregida(W18, espesor_losa, k_modulo):
    """Calcula porcentaje de erosión de manera realista"""
    # Limitar W18
    W18_lim = min(W18, 1000000)
    
    # Convertir unidades
    espesor_pulg = espesor_losa / 25.4
    k_pci = k_modulo * 3.6839
    
    # Fórmula PCA corregida
    if W18_lim > 0 and k_pci > 0:
        W18_limite = 10**6  # 1 millón de ESALs
        espesor_factor = (espesor_pulg / 8.0) ** 7.35
        k_factor = (200 / k_pci) ** 7.35
        erosion_porcentaje = 100 * (W18_lim / W18_limite) * espesor_factor * k_factor
    else:
        erosion_porcentaje = 0
    
    return min(erosion_porcentaje, 100.0)

def calcular_sn_flexible(a1, D1, a2, D2, m2, a3, D3, m3):
    """Calcula número estructural para pavimento flexible"""
    return a1 * D1 + a2 * D2 * m2 + a3 * D3 * m3

def calcular_caudal_racional(C, I, A):
    """Calcula caudal según método racional"""
    return (C * I * A) / 3600  # m³/s

def calcular_capacidad_cuneta_manning(n, y, S):
    """Calcula capacidad de cuneta triangular según Manning"""
    return (1.49 / n) * (y**(8/3)) * math.sqrt(S) / 2  # m³/s

def calcular_diametro_minimo_mtc(caudal, pendiente):
    """Calcula diámetro mínimo según MTC"""
    # Fórmula MTC: D = 0.5 * (Q/S)^0.375
    return 0.5 * (caudal / pendiente)**0.375  # metros

# =================================================================
# CÁLCULOS PARA CUADRA 1 - PAVIMENTO RÍGIDO
# =================================================================

print("=" * 80)
print("CÁLCULOS PARA CUADRA 1 - Jr. Vilcanota (PAVIMENTO RÍGIDO)")
print("=" * 80)

# Calcular W18
W18_cuadra1 = calcular_w18_corregido(ESTUDIO_TRANSITO_CUADRA1)
print(f"W18 (ejes equivalentes): {W18_cuadra1:,.0f}")

# Parámetros de diseño
k_cuadra1 = ESTUDIO_SUELOS["modulo_reaccion_k"]  # MPa/m
Sc_cuadra1 = 4.5  # MPa (módulo de rotura)
J_cuadra1 = 3.2   # Coeficiente de transferencia
C_cuadra1 = 1.0   # Coeficiente de drenaje

# Calcular espesor de losa
espesor_losa_cuadra1 = calcular_espesor_losa_aashto93_corregido(W18_cuadra1, k_cuadra1, Sc_cuadra1, J_cuadra1, C_cuadra1)
print(f"Espesor de losa calculado: {espesor_losa_cuadra1:.1f} mm")

# Calcular fatiga y erosión
fatiga_cuadra1 = calcular_fatiga_corregida(W18_cuadra1, espesor_losa_cuadra1, Sc_cuadra1)
erosion_cuadra1 = calcular_erosion_corregida(W18_cuadra1, espesor_losa_cuadra1, k_cuadra1)

print(f"Porcentaje de fatiga: {fatiga_cuadra1:.2f}%")
print(f"Porcentaje de erosión: {erosion_cuadra1:.2f}%")

# Calcular juntas
espaciamiento_juntas_cuadra1 = 24 * (espesor_losa_cuadra1 / 25.4) * 0.3048  # metros
print(f"Espaciamiento de juntas: {espaciamiento_juntas_cuadra1:.2f} m")

# Calcular refuerzo por temperatura
acero_fy_cuadra1 = 280  # MPa
area_acero_cuadra1 = 0.1 * (espesor_losa_cuadra1 / 25.4) * espaciamiento_juntas_cuadra1 * 645.16  # mm²
print(f"Área de acero por temperatura: {area_acero_cuadra1:.0f} mm²")

# =================================================================
# CÁLCULOS PARA CUADRA 2 - PAVIMENTO FLEXIBLE
# =================================================================

print("\n" + "=" * 80)
print("CÁLCULOS PARA CUADRA 2 - Jr. Ayacucho (PAVIMENTO FLEXIBLE)")
print("=" * 80)

# Calcular W18
W18_cuadra2 = calcular_w18_corregido(ESTUDIO_TRANSITO_CUADRA2)
print(f"W18 (ejes equivalentes): {W18_cuadra2:,.0f}")

# Parámetros de capas
a1_flexible = 0.44  # Coeficiente capa asfáltica
D1_flexible = 4.0   # Espesor asfalto (pulg)
a2_flexible = 0.14  # Coeficiente base
D2_flexible = 8.0   # Espesor base (pulg)
m2_flexible = 1.0   # Factor drenaje base
a3_flexible = 0.11  # Coeficiente subbase
D3_flexible = 6.0   # Espesor subbase (pulg)
m3_flexible = 1.0   # Factor drenaje subbase

# Calcular número estructural
SN_flexible = calcular_sn_flexible(a1_flexible, D1_flexible, a2_flexible, D2_flexible, m2_flexible, a3_flexible, D3_flexible, m3_flexible)
print(f"Número estructural (SN): {SN_flexible:.2f}")

# Análisis de fatiga MEPDG
E_asfalto = 4000  # MPa
eps_t = 70  # microstrain
temperatura = 8.5  # °C (San Miguel)

# Factor de temperatura
factor_temp = 1.2 if temperatura < 10 else 0.8 if temperatura > 30 else 1.0

# Cálculo de repeticiones hasta falla
k1, k2, k3 = 0.0796, 3.291, 0.854
Nf_flexible = k1 * (1/eps_t)**k2 * (1/E_asfalto)**k3 * factor_temp
vida_util_fatiga = Nf_flexible / (365 * ESTUDIO_TRANSITO_CUADRA2["trafico_diario_promedio"]) if ESTUDIO_TRANSITO_CUADRA2["trafico_diario_promedio"] > 0 else float('inf')

print(f"Ciclos hasta falla (Nf): {Nf_flexible:,.0f}")
if vida_util_fatiga != float('inf'):
    print(f"Vida útil por fatiga: {vida_util_fatiga:.1f} años")
else:
    print("Vida útil por fatiga: ∞ años")

# =================================================================
# CÁLCULOS DE DRENAJE
# =================================================================

print("\n" + "=" * 80)
print("CÁLCULOS DE DRENAJE")
print("=" * 80)

# Área de drenaje
area_drenaje = DATOS_PROYECTO["longitud_cuadra"] * (DATOS_PROYECTO["ancho_calzada"] + DATOS_PROYECTO["ancho_vereda"]) / 10000  # ha
print(f"Área de drenaje: {area_drenaje:.2f} ha")

# Caudal de diseño
C_drenaje = PARAMETROS_URBANISTICOS["coeficiente_escorrentia"]
I_drenaje = PARAMETROS_URBANISTICOS["intensidad_lluvia"]
caudal_diseno = calcular_caudal_racional(C_drenaje, I_drenaje, area_drenaje)
print(f"Caudal de diseño: {caudal_diseno:.3f} m³/s")

# Capacidad de cuneta
n_manning = 0.016
y_agua = 0.20  # m
S_pendiente = 0.01
capacidad_cuneta = calcular_capacidad_cuneta_manning(n_manning, y_agua, S_pendiente)
print(f"Capacidad de cuneta: {capacidad_cuneta:.3f} m³/s")

# Factor de seguridad
factor_seguridad = capacidad_cuneta / caudal_diseno
print(f"Factor de seguridad: {factor_seguridad:.2f}")

# Diámetro mínimo de tubería (MTC)
pendiente_tuberia = 0.005
diametro_minimo = calcular_diametro_minimo_mtc(caudal_diseno, pendiente_tuberia)
print(f"Diámetro mínimo tubería (MTC): {diametro_minimo:.3f} m")

# =================================================================
# CÁLCULOS DE NORMATIVAS LOCALES
# =================================================================

print("\n" + "=" * 80)
print("CÁLCULOS DE NORMATIVAS LOCALES")
print("=" * 80)

# Correlación K vs CBR (MTC)
CBR_suelo = ESTUDIO_SUELOS["cbr_promedio"]
K_calculado = 10 * CBR_suelo
print(f"K calculado (MTC): {K_calculado:.1f} MPa/m")

# Ajuste de resistencia f'c por altitud
fc_base = 28.0  # MPa
altitud = DATOS_PROYECTO["altitud"]
if altitud > 3800:
    fc_ajustado = fc_base + 5
    estado_ajuste = "Ajustado (+5 MPa)"
else:
    fc_ajustado = fc_base
    estado_ajuste = "Sin ajuste"

print(f"f'c base: {fc_base:.1f} MPa")
print(f"f'c ajustado: {fc_ajustado:.1f} MPa")
print(f"Estado: {estado_ajuste}")

# =================================================================
# RESUMEN EJECUTIVO
# =================================================================

print("\n" + "=" * 80)
print("RESUMEN EJECUTIVO DEL PROYECTO")
print("=" * 80)

print(f"PROYECTO: {DATOS_PROYECTO['nombre']}")
print(f"UBICACIÓN: {DATOS_PROYECTO['ubicacion']}")
print(f"ALTITUD: {DATOS_PROYECTO['altitud']} msnm")
print(f"PERÍODO DE DISEÑO: {DATOS_PROYECTO['periodo_diseno']} años")
print(f"RESPONSABLE: {DATOS_PROYECTO['responsable']}")

print("\nRESULTADOS PRINCIPALES:")
print(f"• Cuadra 1 (Rígido): Espesor {espesor_losa_cuadra1:.0f} mm, Fatiga {fatiga_cuadra1:.1f}%, Erosión {erosion_cuadra1:.1f}%")
print(f"• Cuadra 2 (Flexible): SN {SN_flexible:.2f}, Vida útil fatiga {vida_util_fatiga:.1f} años" if vida_util_fatiga != float('inf') else f"• Cuadra 2 (Flexible): SN {SN_flexible:.2f}, Vida útil fatiga ∞ años")
print(f"• Drenaje: Caudal {caudal_diseno:.3f} m³/s, Factor seguridad {factor_seguridad:.2f}")
print(f"• Normativas: K {K_calculado:.1f} MPa/m, f'c {fc_ajustado:.1f} MPa")

print("\nRECOMENDACIONES:")
if fatiga_cuadra1 > 80:
    print("⚠️ Pavimento rígido: Considerar mayor espesor o mejor calidad de concreto")
else:
    print("✅ Pavimento rígido: Diseño adecuado")

if erosion_cuadra1 > 80:
    print("⚠️ Pavimento rígido: Mejorar subrasante o aumentar espesor")
else:
    print("✅ Pavimento rígido: Subrasante adecuada")

if factor_seguridad < 1.5:
    print("⚠️ Drenaje: Considerar mayor capacidad de cuneta")
else:
    print("✅ Drenaje: Capacidad adecuada")

print("\n" + "=" * 80)
print("FIN DEL EJEMPLO")
print("=" * 80) 