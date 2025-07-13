"""
EJEMPLO COMPLETO: PROYECTO DE PAVIMENTO EN SAN MIGUEL, PUNO
================================================================

PROYECTO: PISTA VEREDA PAVIMENTO RÍGIDO Y FLEXIBLE
UBICACIÓN: San Miguel, Puno, Perú
CUADRAS: 1 (Jr. Vilcanota) y 2 (Jr. Ayacucho)
ALTITUD: 3,850 msnm
FECHA: 2024

ESTUDIOS REALIZADOS:
- Estudio de Tránsito
- Estudio de Suelos
- Análisis Urbano
- Diseño según AASHTO 93, PCA, MTC, RNE

================================================================
"""

import numpy as np
import pandas as pd
from datetime import datetime

# =================================================================
# DATOS GENERALES DEL PROYECTO
# =================================================================

DATOS_PROYECTO = {
    "nombre": "Pista Vereda Pavimento Rígido y Flexible - San Miguel, Puno",
    "ubicacion": "San Miguel, Puno, Perú",
    "altitud": 3850,  # msnm
    "clima": "Frío andino",
    "temperatura_promedio": 8.5,  # °C
    "precipitacion_anual": 650,  # mm
    "periodo_diseno": 20,  # años
    "fecha_estudio": "2024",
    "responsable": "CONSORCIO DEJ"
}

# =================================================================
# ESTUDIO DE SUELOS - SAN MIGUEL, PUNO
# =================================================================

ESTUDIO_SUELOS = {
    "tipo_suelo": "Suelo granular fino (SM-SC)",
    "clasificacion": "A-2-4 según AASHTO",
    "CBR_promedio": 4.5,  # %
    "CBR_minimo": 3.0,    # %
    "CBR_maximo": 6.0,    # %
    "peso_unitario": 18.5,  # kN/m³
    "angulo_friccion": 28,  # grados
    "cohesion": 15,  # kPa
    "modulo_elasticidad_suelo": 45,  # MPa
    "profundidad_nivel_freatico": 3.5,  # m
    "capacidad_portante": 120,  # kPa
    "observaciones": [
        "Suelo típico de la región andina",
        "Buena estabilidad natural",
        "Requiere compactación adecuada",
        "Drenaje moderado"
    ]
}

# Correlación K vs CBR según MTC
def calcular_k_por_cbr(cbr):
    """Calcula el módulo de reacción K según correlación MTC"""
    if cbr <= 50:
        return 10 * cbr  # MPa/m
    else:
        return 500  # Límite máximo según MTC

# =================================================================
# ESTUDIO DE TRÁNSITO - CUADRA 1 (Jr. Vilcanota)
# =================================================================

ESTUDIO_TRANSITO_CUADRA1 = {
    "ubicacion": "Jr. Vilcanota, Cuadra 1",
    "longitud": 100,  # metros
    "ancho_calzada": 6.0,  # metros
    "tipo_via": "Vía urbana secundaria",
    "clasificacion": "Colectora",
    "velocidad_diseno": 30,  # km/h
    
    # Tránsito actual (2024)
    "trafico_actual": {
        "vehiculos_livianos": 85,  # veh/día
        "buses": 12,  # veh/día
        "camiones_2_ejes": 8,  # veh/día
        "camiones_3_ejes": 3,  # veh/día
        "total_diario": 108  # veh/día
    },
    
    # Factor de crecimiento anual
    "factor_crecimiento": 0.025,  # 2.5% anual
    
    # Factores de distribución
    "factor_direccion": 0.55,  # 55% dirección principal
    "factor_carril": 0.85,  # 85% carril de diseño
    "factor_estacional": 1.1,  # 10% incremento estacional
    
    # Ejes equivalentes por tipo de vehículo
    "ejes_equivalentes": {
        "vehiculos_livianos": 0.0001,  # ESALs por vehículo
        "buses": 0.5,  # ESALs por vehículo
        "camiones_2_ejes": 1.2,  # ESALs por vehículo
        "camiones_3_ejes": 2.8  # ESALs por vehículo
    }
}

def calcular_w18_cuadra1():
    """Calcula el número de ejes equivalentes W18 para Cuadra 1"""
    trafico = ESTUDIO_TRANSITO_CUADRA1["trafico_actual"]
    ejes = ESTUDIO_TRANSITO_CUADRA1["ejes_equivalentes"]
    factores = ESTUDIO_TRANSITO_CUADRA1
    
    # Cálculo diario
    w18_diario = (
        trafico["vehiculos_livianos"] * ejes["vehiculos_livianos"] +
        trafico["buses"] * ejes["buses"] +
        trafico["camiones_2_ejes"] * ejes["camiones_2_ejes"] +
        trafico["camiones_3_ejes"] * ejes["camiones_3_ejes"]
    )
    
    # Aplicar factores
    w18_diseno = w18_diario * factores["factor_direccion"] * factores["factor_carril"] * factores["factor_estacional"]
    
    # Cálculo para período de diseño (20 años)
    n = 365 * DATOS_PROYECTO["periodo_diseno"]
    r = factores["factor_crecimiento"]
    
    if r != 0:
        w18_total = w18_diseno * ((1 + r)**n - 1) / r
    else:
        w18_total = w18_diseno * n
    
    return int(w18_total)

# =================================================================
# ESTUDIO DE TRÁNSITO - CUADRA 2 (Jr. Ayacucho)
# =================================================================

ESTUDIO_TRANSITO_CUADRA2 = {
    "ubicacion": "Jr. Ayacucho, Cuadra 2",
    "longitud": 100,  # metros
    "ancho_calzada": 6.0,  # metros
    "tipo_via": "Vía urbana secundaria",
    "clasificacion": "Colectora",
    "velocidad_diseno": 30,  # km/h
    
    # Tránsito actual (2024) - Ligeramente mayor que Cuadra 1
    "trafico_actual": {
        "vehiculos_livianos": 95,  # veh/día
        "buses": 15,  # veh/día
        "camiones_2_ejes": 10,  # veh/día
        "camiones_3_ejes": 4,  # veh/día
        "total_diario": 124  # veh/día
    },
    
    # Factor de crecimiento anual
    "factor_crecimiento": 0.025,  # 2.5% anual
    
    # Factores de distribución
    "factor_direccion": 0.55,  # 55% dirección principal
    "factor_carril": 0.85,  # 85% carril de diseño
    "factor_estacional": 1.1,  # 10% incremento estacional
    
    # Ejes equivalentes por tipo de vehículo
    "ejes_equivalentes": {
        "vehiculos_livianos": 0.0001,  # ESALs por vehículo
        "buses": 0.5,  # ESALs por vehículo
        "camiones_2_ejes": 1.2,  # ESALs por vehículo
        "camiones_3_ejes": 2.8  # ESALs por vehículo
    }
}

def calcular_w18_cuadra2():
    """Calcula el número de ejes equivalentes W18 para Cuadra 2"""
    trafico = ESTUDIO_TRANSITO_CUADRA2["trafico_actual"]
    ejes = ESTUDIO_TRANSITO_CUADRA2["ejes_equivalentes"]
    factores = ESTUDIO_TRANSITO_CUADRA2
    
    # Cálculo diario
    w18_diario = (
        trafico["vehiculos_livianos"] * ejes["vehiculos_livianos"] +
        trafico["buses"] * ejes["buses"] +
        trafico["camiones_2_ejes"] * ejes["camiones_2_ejes"] +
        trafico["camiones_3_ejes"] * ejes["camiones_3_ejes"]
    )
    
    # Aplicar factores
    w18_diseno = w18_diario * factores["factor_direccion"] * factores["factor_carril"] * factores["factor_estacional"]
    
    # Cálculo para período de diseño (20 años)
    n = 365 * DATOS_PROYECTO["periodo_diseno"]
    r = factores["factor_crecimiento"]
    
    if r != 0:
        w18_total = w18_diseno * ((1 + r)**n - 1) / r
    else:
        w18_total = w18_diseno * n
    
    return int(w18_total)

# =================================================================
# PARÁMETROS DE DISEÑO AASHTO 93
# =================================================================

PARAMETROS_AASHTO93 = {
    "ZR": -1.645,  # Factor de confiabilidad estándar normal (95%)
    "S0": 0.35,    # Desviación estándar
    "delta_PSI": 1.5,  # Pérdida de servicio
    "R": 0.95,     # Confiabilidad
    "C": 1.0,      # Coeficiente de drenaje
    "J": 3.2,      # Coeficiente de transferencia de carga
    "Ec": 30000,   # Módulo de elasticidad del concreto (MPa)
}

# =================================================================
# CÁLCULOS PAVIMENTO RÍGIDO - CUADRA 1
# =================================================================

def calcular_pavimento_rigido_cuadra1():
    """Calcula el pavimento rígido para Cuadra 1"""
    
    # Datos de entrada
    W18 = calcular_w18_cuadra1()
    k = calcular_k_por_cbr(ESTUDIO_SUELOS["CBR_promedio"])
    Sc = 4.5  # MPa (resistencia a flexión)
    
    # Convertir a unidades inglesas para AASHTO 93
    W18_ingles = W18
    k_ingles = k * 3.6839  # MPa/m a pci
    Sc_ingles = Sc * 145.038  # MPa a psi
    Ec_ingles = PARAMETROS_AASHTO93["Ec"] * 145.038  # MPa a psi
    
    # Fórmula AASHTO 93 (iterativa)
    def calcular_espesor_losa_AASHTO93(W18, ZR, S0, delta_PSI, Sc, J, k, C, D_init=8.0):
        import math
        D = D_init
        for _ in range(30):
            term1 = ZR * S0
            term2 = math.log10(delta_PSI / (4.5 - 1.5))
            term3 = 7.35 * math.log10(D + 1) - 0.06
            term4 = 1 + 1.624e7 / (Sc ** 2.96 * D ** 8.46)
            term5 = 0.75 * math.log10(J * k * C / (Sc * D ** 0.75))
            logW18_calc = term1 + term3 + term2 / term4 - term5
            W18_calc = 10 ** logW18_calc
            error = math.log10(W18) - logW18_calc
            if abs(error) < 0.0001:
                break
            D += error * 10
            if D < 6: D = 6
            if D > 20: D = 20
        return D
    
    # Calcular espesor
    D_pulg = calcular_espesor_losa_AASHTO93(
        W18_ingles, 
        PARAMETROS_AASHTO93["ZR"], 
        PARAMETROS_AASHTO93["S0"], 
        PARAMETROS_AASHTO93["delta_PSI"], 
        Sc_ingles, 
        PARAMETROS_AASHTO93["J"], 
        k_ingles, 
        PARAMETROS_AASHTO93["C"]
    )
    
    D_mm = D_pulg * 25.4
    
    # Calcular juntas
    sigma_t = 45  # esfuerzo admisible (psi)
    gamma_c = 2400  # peso unitario (pcf)
    f = 1.5  # factor de fricción
    mu = 1.0  # coeficiente de fricción
    w = D_pulg * 1.0  # peso de losa
    
    L_junta_pies = (f * sigma_t) / (gamma_c * w * mu)
    L_junta_m = L_junta_pies * 0.3048
    
    # Calcular refuerzo por temperatura
    fa = 1.5
    fs = 280  # MPa (acero)
    As_temp_mm2 = (gamma_c * L_junta_m * D_mm * fa) / (2 * fs * 1000)
    
    # Análisis de fatiga y erosión
    porcentaje_fatiga = 100 * (W18 / (10**7)) * (D_mm / 25.4 / (Sc * 145.038)) ** 3.42
    porcentaje_erosion = 100 * (DATOS_PROYECTO["periodo_diseno"] / 20) * (D_mm / 250) * (30 / k) * 32.80
    
    return {
        "espesor_losa": D_mm,
        "espesor_losa_pulg": D_pulg,
        "junta_maxima": L_junta_m,
        "area_acero_temp": As_temp_mm2,
        "fatiga_porcentaje": porcentaje_fatiga,
        "erosion_porcentaje": porcentaje_erosion,
        "W18": W18,
        "k": k,
        "Sc": Sc
    }

# =================================================================
# CÁLCULOS PAVIMENTO FLEXIBLE - CUADRA 2
# =================================================================

def calcular_pavimento_flexible_cuadra2():
    """Calcula el pavimento flexible para Cuadra 2"""
    
    # Datos de entrada
    W18 = calcular_w18_cuadra2()
    
    # Coeficientes de capa según AASHTO 93
    a1 = 0.44  # Coeficiente capa asfáltica
    D1 = 4.0   # Espesor capa asfáltica (pulg)
    a2 = 0.14  # Coeficiente base
    D2 = 8.0   # Espesor base (pulg)
    m2 = 1.0   # Factor drenaje base
    a3 = 0.11  # Coeficiente subbase
    D3 = 6.0   # Espesor subbase (pulg)
    m3 = 1.0   # Factor drenaje subbase
    
    # Calcular número estructural
    SN = a1 * D1 + a2 * D2 * m2 + a3 * D3 * m3
    
    # Análisis de fatiga MEPDG
    E_asfalto = 3000  # MPa (módulo de elasticidad del asfalto)
    epsilon_t = 70  # microstrain (deformación por tracción)
    
    # Fórmula MEPDG para fatiga
    k1 = 0.0796
    k2 = 3.291
    k3 = 0.854
    
    Nf = k1 * (1/epsilon_t)**k2 * (1/E_asfalto)**k3
    
    # Convertir a años
    Nf_anios = Nf / (365 * ESTUDIO_TRANSITO_CUADRA2["trafico_actual"]["total_diario"])
    
    return {
        "numero_estructural": SN,
        "espesor_asfalto": D1 * 25.4,  # mm
        "espesor_base": D2 * 25.4,     # mm
        "espesor_subbase": D3 * 25.4,  # mm
        "vida_fatiga": Nf_anios,
        "W18": W18,
        "coeficientes": {
            "a1": a1,
            "a2": a2,
            "a3": a3,
            "m2": m2,
            "m3": m3
        }
    }

# =================================================================
# CÁLCULOS DRENAJE
# =================================================================

def calcular_drenaje():
    """Calcula el sistema de drenaje"""
    
    # Datos de entrada
    area_cuadra = 100 * 6  # m² (100m x 6m)
    intensidad_lluvia = 25  # mm/h (San Miguel, Puno)
    coeficiente_escorrentia = 0.85  # Pavimento impermeable
    
    # Método racional
    caudal_diseno = (coeficiente_escorrentia * intensidad_lluvia * area_cuadra) / (3.6 * 10**6)  # m³/s
    
    # Diámetro mínimo según MTC
    diametro_minimo = 0.30  # m (30 cm)
    
    # Capacidad del tubo (Manning)
    n_manning = 0.013  # Coeficiente de rugosidad (PVC)
    pendiente = 0.02   # 2%
    radio_hidraulico = diametro_minimo / 4  # Para tubo circular lleno
    
    velocidad = (1/n_manning) * (radio_hidraulico**(2/3)) * (pendiente**(1/2))
    capacidad_tubo = velocidad * (np.pi * (diametro_minimo/2)**2)
    
    return {
        "caudal_diseno": caudal_diseno,
        "diametro_minimo": diametro_minimo,
        "velocidad": velocidad,
        "capacidad_tubo": capacidad_tubo,
        "factor_seguridad": capacidad_tubo / caudal_diseno
    }

# =================================================================
# AJUSTES POR ALTITUD (MTC)
# =================================================================

def ajustar_resistencia_altitud(fc_original, altitud):
    """Ajusta la resistencia del concreto por altitud según MTC"""
    if altitud > 3800:
        return fc_original + 5  # MPa
    else:
        return fc_original

# =================================================================
# EJECUTAR CÁLCULOS
# =================================================================

def ejecutar_calculos_completos():
    """Ejecuta todos los cálculos del proyecto"""
    
    print("=" * 80)
    print("PROYECTO: PISTA VEREDA PAVIMENTO RÍGIDO Y FLEXIBLE")
    print("UBICACIÓN: San Miguel, Puno, Perú")
    print("FECHA:", datetime.now().strftime("%d/%m/%Y"))
    print("=" * 80)
    
    # Calcular W18 para ambas cuadras
    W18_cuadra1 = calcular_w18_cuadra1()
    W18_cuadra2 = calcular_w18_cuadra2()
    
    print(f"\n📊 ESTUDIO DE TRÁNSITO:")
    print(f"Cuadra 1 (Jr. Vilcanota): W18 = {W18_cuadra1:,} ejes equivalentes")
    print(f"Cuadra 2 (Jr. Ayacucho):  W18 = {W18_cuadra2:,} ejes equivalentes")
    
    # Calcular módulo de reacción K
    K = calcular_k_por_cbr(ESTUDIO_SUELOS["CBR_promedio"])
    
    print(f"\n🏗️ ESTUDIO DE SUELOS:")
    print(f"CBR promedio: {ESTUDIO_SUELOS['CBR_promedio']}%")
    print(f"Módulo de reacción K: {K:.1f} MPa/m")
    print(f"Tipo de suelo: {ESTUDIO_SUELOS['tipo_suelo']}")
    
    # Calcular pavimento rígido - Cuadra 1
    print(f"\n🛣️ PAVIMENTO RÍGIDO - CUADRA 1 (Jr. Vilcanota):")
    resultado_rigido = calcular_pavimento_rigido_cuadra1()
    print(f"Espesor de losa: {resultado_rigido['espesor_losa']:.1f} mm ({resultado_rigido['espesor_losa_pulg']:.1f} pulg)")
    print(f"Junta máxima: {resultado_rigido['junta_maxima']:.2f} m")
    print(f"Área de acero por temperatura: {resultado_rigido['area_acero_temp']:.1f} mm²")
    print(f"Porcentaje de fatiga: {resultado_rigido['fatiga_porcentaje']:.2f}%")
    print(f"Porcentaje de erosión: {resultado_rigido['erosion_porcentaje']:.2f}%")
    
    # Calcular pavimento flexible - Cuadra 2
    print(f"\n🛣️ PAVIMENTO FLEXIBLE - CUADRA 2 (Jr. Ayacucho):")
    resultado_flexible = calcular_pavimento_flexible_cuadra2()
    print(f"Número estructural SN: {resultado_flexible['numero_estructural']:.2f}")
    print(f"Espesor capa asfáltica: {resultado_flexible['espesor_asfalto']:.1f} mm")
    print(f"Espesor base: {resultado_flexible['espesor_base']:.1f} mm")
    print(f"Espesor subbase: {resultado_flexible['espesor_subbase']:.1f} mm")
    print(f"Vida útil por fatiga: {resultado_flexible['vida_fatiga']:.1f} años")
    
    # Calcular drenaje
    print(f"\n🌊 SISTEMA DE DRENAJE:")
    resultado_drenaje = calcular_drenaje()
    print(f"Caudal de diseño: {resultado_drenaje['caudal_diseno']*1000:.1f} L/s")
    print(f"Diámetro mínimo de tubo: {resultado_drenaje['diametro_minimo']*100:.0f} cm")
    print(f"Velocidad en el tubo: {resultado_drenaje['velocidad']:.2f} m/s")
    print(f"Factor de seguridad: {resultado_drenaje['factor_seguridad']:.1f}")
    
    # Ajustes por altitud
    print(f"\n🏔️ AJUSTES POR ALTITUD (MTC):")
    fc_original = 28  # MPa
    fc_ajustado = ajustar_resistencia_altitud(fc_original, DATOS_PROYECTO["altitud"])
    print(f"Altitud: {DATOS_PROYECTO['altitud']} msnm")
    print(f"f'c original: {fc_original} MPa")
    print(f"f'c ajustado: {fc_ajustado} MPa")
    print(f"Estado: {'Ajustado (+5 MPa)' if fc_ajustado > fc_original else 'Sin ajuste'}")
    
    # Recomendaciones
    print(f"\n💡 RECOMENDACIONES:")
    if resultado_rigido['fatiga_porcentaje'] > 100:
        print("⚠️ Fatiga crítica en pavimento rígido. Considerar aumentar espesor.")
    elif resultado_rigido['fatiga_porcentaje'] > 50:
        print("ℹ️ Fatiga moderada en pavimento rígido. Diseño en límite aceptable.")
    else:
        print("✅ Fatiga dentro de límites seguros en pavimento rígido.")
    
    if resultado_rigido['erosion_porcentaje'] > 100:
        print("⚠️ Erosión crítica en pavimento rígido. Mejorar subrasante.")
    elif resultado_rigido['erosion_porcentaje'] > 50:
        print("ℹ️ Erosión moderada en pavimento rígido. Verificar drenaje.")
    else:
        print("✅ Erosión dentro de límites seguros en pavimento rígido.")
    
    if resultado_flexible['vida_fatiga'] < DATOS_PROYECTO["periodo_diseno"]:
        print("⚠️ Vida útil por fatiga menor al período de diseño en pavimento flexible.")
    else:
        print("✅ Vida útil por fatiga adecuada en pavimento flexible.")
    
    if resultado_drenaje['factor_seguridad'] < 1.5:
        print("⚠️ Factor de seguridad del drenaje bajo. Considerar tubo de mayor diámetro.")
    else:
        print("✅ Sistema de drenaje adecuado.")
    
    print(f"\n📋 NORMATIVAS APLICADAS:")
    print("• AASHTO 93 - Diseño de pavimentos")
    print("• PCA - Análisis de fatiga y erosión")
    print("• MTC - Correlación K vs CBR y ajustes por altitud")
    print("• RNE - Especificaciones técnicas")
    
    print(f"\n" + "=" * 80)
    print("FIN DEL REPORTE")
    print("=" * 80)

# =================================================================
# DATOS PARA LA APLICACIÓN STREAMLIT
# =================================================================

def obtener_datos_streamlit():
    """Retorna los datos organizados para la aplicación Streamlit"""
    
    # Datos para pavimento rígido - Cuadra 1
    datos_rigido = {
        "proyecto": "Pavimento Rígido - Jr. Vilcanota, Cuadra 1",
        "descripcion": "Pavimento rígido para vía urbana en San Miguel, Puno",
        "periodo": 20,
        "sistema_unidades": "SI (Internacional)",
        "espesor_losa": 500,  # mm
        "modulo_rotura": 4.5,  # MPa
        "dovelas": "Sí",
        "bermas": "No",
        "subrasante_tipo": "Correlación con CBR",
        "cbr": 4.5,
        "subbase": True,
        "espesor_subbase": 200,  # mm
        "tipo_subbase": "Sin tratar",
        "diam_barras": "1/2\"",
        "acero_fy": 280,  # MPa
        "ancho_carril": 3.05,  # m
        "ZR": -1.645,
        "S0": 0.35,
        "delta_PSI": 1.5,
        "factor_seg": 1.2,
        "tipo_ejes": "Ejes Simples",
        "tabla_transito": {
            "Carga": [134, 125, 116, 107, 98, 89, 80, 71, 62],
            "Repeticiones": [6310, 14690, 30140, 106900, 233500, 422500, 586900, 1837000, 0]
        }
    }
    
    # Datos para pavimento flexible - Cuadra 2
    datos_flexible = {
        "proyecto": "Pavimento Flexible - Jr. Ayacucho, Cuadra 2",
        "descripcion": "Pavimento flexible para vía urbana en San Miguel, Puno",
        "periodo": 20,
        "sistema_unidades": "SI (Internacional)",
        "a1": 0.44,
        "D1": 4.0,
        "a2": 0.14,
        "D2": 8.0,
        "m2": 1.0,
        "a3": 0.11,
        "D3": 6.0,
        "m3": 1.0,
        "factor_seg": 1.2,
        "tipo_ejes": "Ejes Simples",
        "tabla_transito": {
            "Carga": [134, 125, 116, 107, 98, 89, 80, 71, 62],
            "Repeticiones": [7000, 16000, 33000, 115000, 250000, 450000, 620000, 1950000, 0]
        }
    }
    
    return datos_rigido, datos_flexible

# =================================================================
# EJECUTAR SI SE LLAMA DIRECTAMENTE
# =================================================================

if __name__ == "__main__":
    ejecutar_calculos_completos() 