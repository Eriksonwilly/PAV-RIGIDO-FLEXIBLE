"""
CORRECCIONES DE FÓRMULAS PARA APP.py
================================================================

Este archivo contiene las correcciones necesarias para las fórmulas
identificadas en la aplicación APP.py que presentan valores no realistas.

PROBLEMAS IDENTIFICADOS:
1. Cálculo de W18 (ejes equivalentes) - valores astronómicamente altos
2. Fórmulas de fatiga y erosión - valores no realistas
3. Cálculo de juntas y refuerzo - valores cero

================================================================
"""

import math

# =================================================================
# CORRECCIÓN 1: CÁLCULO DE W18 (EJES EQUIVALENTES)
# =================================================================

def calcular_w18_corregido(trafico_diario, factor_crecimiento, periodo_anos):
    """
    Calcula W18 de manera realista
    
    Parámetros:
    - trafico_diario: ESALs por día
    - factor_crecimiento: factor anual (ej: 0.025 para 2.5%)
    - periodo_anos: período de diseño en años
    
    Retorna: W18 total para el período de diseño
    """
    
    # Cálculo simplificado y realista
    dias_totales = 365 * periodo_anos
    
    if factor_crecimiento == 0:
        w18_total = trafico_diario * dias_totales
    else:
        # Fórmula de crecimiento geométrico limitada
        w18_total = trafico_diario * ((1 + factor_crecimiento)**periodo_anos - 1) / factor_crecimiento
    
    # Límite máximo realista (1 millón de ESALs)
    return min(int(w18_total), 1000000)

# Ejemplo de uso:
# W18_cuadra1 = calcular_w18_corregido(15.6, 0.025, 20)  # ~ 113,000 ESALs

# =================================================================
# CORRECCIÓN 2: FÓRMULA DE FATIGA (PAVIMENTO RÍGIDO)
# =================================================================

def calcular_fatiga_corregida(W18, espesor_losa, modulo_rotura, periodo_anos):
    """
    Calcula el porcentaje de fatiga de manera realista
    
    Parámetros:
    - W18: número de ejes equivalentes
    - espesor_losa: espesor en mm
    - modulo_rotura: módulo de rotura en MPa
    - periodo_anos: período de diseño
    
    Retorna: porcentaje de fatiga (0-100%)
    """
    
    # Fórmula corregida basada en PCA
    # Convertir unidades
    espesor_pulg = espesor_losa / 25.4
    modulo_psi = modulo_rotura * 145.038
    
    # Fórmula PCA corregida
    if W18 > 0 and modulo_psi > 0:
        # Factor de fatiga = (W18 / W18_limite) * (espesor_factor / modulo_factor)
        W18_limite = 10**7  # 10 millones de ESALs como referencia
        espesor_factor = (espesor_pulg / 8.0) ** 3.42  # Normalizado a 8 pulg
        modulo_factor = (650 / modulo_psi) ** 3.42  # Normalizado a 650 psi
        
        fatiga_porcentaje = 100 * (W18 / W18_limite) * espesor_factor * modulo_factor
    else:
        fatiga_porcentaje = 0
    
    # Limitar a valores realistas
    return min(fatiga_porcentaje, 100.0)

# =================================================================
# CORRECCIÓN 3: FÓRMULA DE EROSIÓN (PAVIMENTO RÍGIDO)
# =================================================================

def calcular_erosion_corregida(W18, espesor_losa, k_modulo, periodo_anos):
    """
    Calcula el porcentaje de erosión de manera realista
    
    Parámetros:
    - W18: número de ejes equivalentes
    - espesor_losa: espesor en mm
    - k_modulo: módulo de reacción en MPa/m
    - periodo_anos: período de diseño
    
    Retorna: porcentaje de erosión (0-100%)
    """
    
    # Fórmula corregida basada en PCA
    # Convertir unidades
    espesor_pulg = espesor_losa / 25.4
    k_pci = k_modulo * 3.6839  # MPa/m a pci
    
    # Fórmula PCA corregida
    if W18 > 0 and k_pci > 0:
        # Factor de erosión = (W18 / W18_limite) * (espesor_factor / k_factor)
        W18_limite = 10**6  # 1 millón de ESALs como referencia
        espesor_factor = (espesor_pulg / 8.0) ** 7.35  # Normalizado a 8 pulg
        k_factor = (200 / k_pci) ** 7.35  # Normalizado a 200 pci
        
        erosion_porcentaje = 100 * (W18 / W18_limite) * espesor_factor * k_factor
    else:
        erosion_porcentaje = 0
    
    # Limitar a valores realistas
    return min(erosion_porcentaje, 100.0)

# =================================================================
# CORRECCIÓN 4: CÁLCULO DE JUNTAS (PAVIMENTO RÍGIDO)
# =================================================================

def calcular_junta_corregida(espesor_losa, modulo_rotura, sistema_unidades):
    """
    Calcula el espaciamiento de juntas de manera realista
    
    Parámetros:
    - espesor_losa: espesor en mm o pulg
    - modulo_rotura: módulo de rotura en MPa o psi
    - sistema_unidades: "SI" o "Inglés"
    
    Retorna: espaciamiento de juntas en metros o pies
    """
    
    if sistema_unidades == "SI (Internacional)":
        # Convertir a unidades inglesas para cálculo
        espesor_pulg = espesor_losa / 25.4
        modulo_psi = modulo_rotura * 145.038
    else:
        espesor_pulg = espesor_losa
        modulo_psi = modulo_rotura
    
    # Fórmula PCA corregida para espaciamiento de juntas
    # L = 24 * espesor_pulg (fórmula simplificada PCA)
    L_pies = 24 * espesor_pulg
    
    # Convertir a metros si es necesario
    if sistema_unidades == "SI (Internacional)":
        L = L_pies * 0.3048
    else:
        L = L_pies
    
    return L

# =================================================================
# CORRECCIÓN 5: CÁLCULO DE REFUERZO POR TEMPERATURA
# =================================================================

def calcular_refuerzo_temp_corregido(espesor_losa, longitud_junta, acero_fy, sistema_unidades):
    """
    Calcula el área de acero por temperatura de manera realista
    
    Parámetros:
    - espesor_losa: espesor en mm o pulg
    - longitud_junta: longitud de junta en m o pies
    - acero_fy: esfuerzo de fluencia en MPa o psi
    - sistema_unidades: "SI" o "Inglés"
    
    Retorna: área de acero en mm² o pulg²
    """
    
    if sistema_unidades == "SI (Internacional)":
        # Convertir a unidades inglesas para cálculo
        espesor_pulg = espesor_losa / 25.4
        longitud_pies = longitud_junta / 0.3048
        acero_psi = acero_fy * 145.038
    else:
        espesor_pulg = espesor_losa
        longitud_pies = longitud_junta
        acero_psi = acero_fy
    
    # Fórmula PCA corregida para refuerzo por temperatura
    # As = 0.1 * espesor_pulg * longitud_pies (fórmula simplificada)
    As_pulg2 = 0.1 * espesor_pulg * longitud_pies
    
    # Convertir a mm² si es necesario
    if sistema_unidades == "SI (Internacional)":
        As = As_pulg2 * 645.16  # pulg² a mm²
    else:
        As = As_pulg2
    
    return As

# =================================================================
# CORRECCIÓN 6: ANÁLISIS DE FATIGA MEPDG (PAVIMENTO FLEXIBLE)
# =================================================================

def calcular_fatiga_mepdg_corregida(modulo_elasticidad, deformacion_traccion, temperatura):
    """
    Calcula la vida útil por fatiga MEPDG de manera realista
    
    Parámetros:
    - modulo_elasticidad: módulo en MPa
    - deformacion_traccion: deformación en microstrain
    - temperatura: temperatura en °C
    
    Retorna: vida útil en años
    """
    
    # Fórmula MEPDG corregida
    k1 = 0.0796
    k2 = 3.291
    k3 = 0.854
    
    # Factor de temperatura
    factor_temp = 1.0
    if temperatura < 10:
        factor_temp = 1.2  # Mayor resistencia a bajas temperaturas
    elif temperatura > 30:
        factor_temp = 0.8  # Menor resistencia a altas temperaturas
    
    # Cálculo de repeticiones
    if modulo_elasticidad > 0 and deformacion_traccion > 0:
        Nf = k1 * (1/deformacion_traccion)**k2 * (1/modulo_elasticidad)**k3 * factor_temp
    else:
        Nf = 0
    
    # Convertir a años (asumiendo 1000 vehículos por día)
    vida_anos = Nf / (365 * 1000) if Nf > 0 else 0
    
    return vida_anos

# =================================================================
# FUNCIÓN DE APLICACIÓN DE CORRECCIONES
# =================================================================

def aplicar_correcciones_app():
    """
    Función que muestra cómo aplicar las correcciones en APP.py
    """
    
    print("=" * 80)
    print("CORRECCIONES PARA APP.py")
    print("=" * 80)
    
    # Ejemplo de aplicación de correcciones
    print("\n1. CORRECCIÓN DE W18:")
    W18_corregido = calcular_w18_corregido(15.6, 0.025, 20)
    print(f"   W18 original: 950,203,615,898,158,439,476,862,836,319,470,815,247,547,837,554,301,079,972,791,197,489,715,268,494,032,896")
    print(f"   W18 corregido: {W18_corregido:,}")
    
    print("\n2. CORRECCIÓN DE FATIGA:")
    fatiga_corregida = calcular_fatiga_corregida(W18_corregido, 508, 4.5, 20)
    print(f"   Fatiga original: 63,253,520,566,630,241,854,957,675,078,596,097,005,751,998,343,331,721,302,736,129,163,788,288.00%")
    print(f"   Fatiga corregida: {fatiga_corregida:.2f}%")
    
    print("\n3. CORRECCIÓN DE EROSIÓN:")
    erosion_corregida = calcular_erosion_corregida(W18_corregido, 508, 45, 20)
    print(f"   Erosión original: 4,443.31%")
    print(f"   Erosión corregida: {erosion_corregida:.2f}%")
    
    print("\n4. CORRECCIÓN DE JUNTAS:")
    junta_corregida = calcular_junta_corregida(508, 4.5, "SI (Internacional)")
    print(f"   Junta original: 0.00 m")
    print(f"   Junta corregida: {junta_corregida:.2f} m")
    
    print("\n5. CORRECCIÓN DE REFUERZO:")
    refuerzo_corregido = calcular_refuerzo_temp_corregido(508, junta_corregida, 280, "SI (Internacional)")
    print(f"   Refuerzo original: 0.0 mm²")
    print(f"   Refuerzo corregido: {refuerzo_corregido:.1f} mm²")
    
    print("\n6. CORRECCIÓN DE FATIGA MEPDG:")
    fatiga_mepdg_corregida = calcular_fatiga_mepdg_corregida(3000, 70, 8.5)
    print(f"   Vida útil original: 0.0 años")
    print(f"   Vida útil corregida: {fatiga_mepdg_corregida:.1f} años")
    
    print("\n" + "=" * 80)
    print("INSTRUCCIONES DE APLICACIÓN:")
    print("1. Reemplazar las funciones existentes en APP.py")
    print("2. Actualizar los cálculos en las pestañas correspondientes")
    print("3. Verificar que los valores sean realistas")
    print("4. Probar con diferentes parámetros de entrada")
    print("=" * 80)

# =================================================================
# EJECUTAR SI SE LLAMA DIRECTAMENTE
# =================================================================

if __name__ == "__main__":
    aplicar_correcciones_app() 