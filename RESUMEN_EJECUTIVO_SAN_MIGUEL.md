# RESUMEN EJECUTIVO
## PROYECTO: PISTA VEREDA PAVIMENTO RÍGIDO Y FLEXIBLE
### San Miguel, Puno, Perú

---

## 📋 INFORMACIÓN GENERAL DEL PROYECTO

| **Parámetro** | **Valor** |
|---------------|-----------|
| **Ubicación** | San Miguel, Puno, Perú |
| **Altitud** | 3,850 msnm |
| **Clima** | Frío andino |
| **Temperatura promedio** | 8.5°C |
| **Precipitación anual** | 650 mm |
| **Período de diseño** | 20 años |
| **Responsable** | CONSORCIO DEJ |
| **Fecha de estudio** | 2024 |

---

## 🏗️ ESTUDIO DE SUELOS

### Características del Suelo
- **Tipo de suelo:** Suelo granular fino (SM-SC)
- **Clasificación AASHTO:** A-2-4
- **CBR promedio:** 4.5%
- **CBR rango:** 3.0% - 6.0%
- **Peso unitario:** 18.5 kN/m³
- **Ángulo de fricción:** 28°
- **Cohesión:** 15 kPa
- **Módulo de elasticidad:** 45 MPa
- **Capacidad portante:** 120 kPa

### Correlación K vs CBR (MTC)
```
K = 10 × CBR = 10 × 4.5 = 45 MPa/m
```

---

## 🚗 ESTUDIO DE TRÁNSITO

### Cuadra 1 - Jr. Vilcanota (Pavimento Rígido)

| **Tipo de Vehículo** | **Tránsito Diario** | **Ejes Equivalentes** |
|---------------------|-------------------|---------------------|
| Vehículos livianos | 85 veh/día | 0.0001 ESALs |
| Buses | 12 veh/día | 0.5 ESALs |
| Camiones 2 ejes | 8 veh/día | 1.2 ESALs |
| Camiones 3 ejes | 3 veh/día | 2.8 ESALs |
| **Total diario** | **108 veh/día** | **15.6 ESALs/día** |

**W18 total (20 años):** 950,203,615,898,158,439,476,862,836,319,470,815,247,547,837,554,301,079,972,791,197,489,715,268,494,032,896 ejes equivalentes

### Cuadra 2 - Jr. Ayacucho (Pavimento Flexible)

| **Tipo de Vehículo** | **Tránsito Diario** | **Ejes Equivalentes** |
|---------------------|-------------------|---------------------|
| Vehículos livianos | 95 veh/día | 0.0001 ESALs |
| Buses | 15 veh/día | 0.5 ESALs |
| Camiones 2 ejes | 10 veh/día | 1.2 ESALs |
| Camiones 3 ejes | 4 veh/día | 2.8 ESALs |
| **Total diario** | **124 veh/día** | **18.4 ESALs/día** |

**W18 total (20 años):** 1,215,414,454,981,548,406,555,457,218,471,504,870,509,577,851,732,832,139,542,077,794,751,885,092,455,448,576 ejes equivalentes

---

## 🛣️ DISEÑO DE PAVIMENTO RÍGIDO - CUADRA 1

### Parámetros de Diseño AASHTO 93
- **ZR (Factor confiabilidad):** -1.645 (95%)
- **S0 (Desviación estándar):** 0.35
- **ΔPSI (Pérdida de servicio):** 1.5
- **R (Confiabilidad):** 0.95
- **C (Coef. drenaje):** 1.0
- **J (Coef. transferencia):** 3.2
- **Ec (Módulo elasticidad):** 30,000 MPa

### Resultados del Diseño
| **Parámetro** | **Valor** | **Unidad** |
|---------------|-----------|------------|
| **Espesor de losa** | 508.0 | mm |
| **Espesor de losa** | 20.0 | pulg |
| **Junta máxima** | 0.00 | m |
| **Área acero temperatura** | 0.0 | mm² |
| **Porcentaje fatiga** | 63,253,520,566,630,241,854,957,675,078,596,097,005,751,998,343,331,721,302,736,129,163,788,288.00 | % |
| **Porcentaje erosión** | 4,443.31 | % |

### ⚠️ ANÁLISIS CRÍTICO
- **Fatiga:** CRÍTICA - Valores extremadamente altos indican error en cálculo
- **Erosión:** CRÍTICA - Excede límites aceptables
- **Recomendación:** Revisar fórmulas y parámetros de entrada

---

## 🛣️ DISEÑO DE PAVIMENTO FLEXIBLE - CUADRA 2

### Número Estructural (AASHTO 93)
```
SN = a₁D₁ + a₂D₂m₂ + a₃D₃m₃
SN = 0.44×4.0 + 0.14×8.0×1.0 + 0.11×6.0×1.0 = 3.54
```

### Estructura del Pavimento
| **Capa** | **Coeficiente** | **Espesor** | **Factor** | **Contribución** |
|----------|----------------|-------------|------------|------------------|
| Asfáltica | a₁ = 0.44 | D₁ = 4.0 pulg | - | 1.76 |
| Base | a₂ = 0.14 | D₂ = 8.0 pulg | m₂ = 1.0 | 1.12 |
| Subbase | a₃ = 0.11 | D₃ = 6.0 pulg | m₃ = 1.0 | 0.66 |
| **Total SN** | | | | **3.54** |

### Espesores en Milímetros
- **Capa asfáltica:** 101.6 mm
- **Base:** 203.2 mm
- **Subbase:** 152.4 mm

### Análisis de Fatiga MEPDG
- **Vida útil por fatiga:** 0.0 años
- **Estado:** CRÍTICO - Requiere revisión de parámetros

---

## 🌊 SISTEMA DE DRENAJE

### Cálculos Hidrológicos
- **Área de drenaje:** 0.06 ha (100m × 6m)
- **Coeficiente de escorrentía:** 0.85
- **Intensidad de lluvia:** 25 mm/h
- **Caudal de diseño:** 3.5 L/s

### Diseño de Alcantarillas
- **Diámetro mínimo:** 30 cm
- **Velocidad en el tubo:** 1.93 m/s
- **Factor de seguridad:** 38.6
- **Estado:** ✅ ADECUADO

---

## 🏔️ AJUSTES POR ALTITUD (MTC)

### Correlación K vs CBR
- **CBR:** 4.5%
- **K calculado:** 45.0 MPa/m
- **Estado:** ✅ VÁLIDO (CBR ≤ 50%)

### Ajuste de Resistencia del Concreto
- **f'c original:** 28 MPa
- **Altitud:** 3,850 msnm
- **f'c ajustado:** 33 MPa (+5 MPa)
- **Estado:** ✅ AJUSTADO (Altitud > 3800 msnm)

---

## 💡 RECOMENDACIONES TÉCNICAS

### 🚨 CRÍTICAS
1. **Revisar cálculos de W18:** Los valores son astronómicamente altos
2. **Corregir fórmulas de fatiga:** Valores no realistas
3. **Ajustar parámetros de erosión:** Exceden límites aceptables

### 🔧 MEJORAS SUGERIDAS
1. **Pavimento Rígido:**
   - Aumentar espesor de losa
   - Mejorar resistencia del concreto
   - Implementar subbase de mayor calidad

2. **Pavimento Flexible:**
   - Revisar parámetros de fatiga MEPDG
   - Ajustar espesores de capas
   - Verificar módulos de elasticidad

3. **Sistema de Drenaje:**
   - ✅ Adecuado según cálculos
   - Implementar mantenimiento preventivo

### 🏗️ ESPECIFICACIONES TÉCNICAS

#### Pavimento Rígido - Cuadra 1
```
- Espesor de losa: 508 mm (20 pulg)
- Resistencia a flexión: 4.5 MPa
- Módulo de elasticidad: 30,000 MPa
- Juntas: Máximo 0.00 m (requiere revisión)
- Refuerzo: 0.0 mm² (requiere revisión)
```

#### Pavimento Flexible - Cuadra 2
```
- Número estructural: 3.54
- Capa asfáltica: 101.6 mm
- Base granular: 203.2 mm
- Subbase: 152.4 mm
- Vida útil por fatiga: 0.0 años (requiere revisión)
```

---

## 📋 NORMATIVAS APLICADAS

1. **AASHTO 93** - Diseño de pavimentos
2. **PCA** - Análisis de fatiga y erosión
3. **MTC** - Correlación K vs CBR y ajustes por altitud
4. **RNE** - Especificaciones técnicas
5. **MEPDG** - Análisis de fatiga del asfalto

---

## 🎯 CONCLUSIONES

### ✅ ASPECTOS POSITIVOS
- Estudio de suelos completo y representativo
- Sistema de drenaje adecuado
- Aplicación correcta de normativas peruanas
- Ajustes por altitud implementados

### ⚠️ ASPECTOS A MEJORAR
- Cálculos de tránsito requieren revisión
- Fórmulas de fatiga y erosión necesitan corrección
- Parámetros de diseño deben ajustarse

### 📊 RECOMENDACIÓN FINAL
**REVISAR Y CORREGIR LOS CÁLCULOS DE TRÁNSITO Y ANÁLISIS DE FATIGA ANTES DE PROCEEDER CON LA CONSTRUCCIÓN.**

---

## 📞 INFORMACIÓN DE CONTACTO

**CONSORCIO DEJ**
- **Proyecto:** Pista Vereda Pavimento Rígido y Flexible
- **Ubicación:** San Miguel, Puno, Perú
- **Fecha:** 2024
- **Responsable:** Equipo de Diseño CONSORCIO DEJ

---

*Este resumen ejecutivo presenta los resultados del análisis técnico completo del proyecto de pavimento en San Miguel, Puno, siguiendo las normativas AASHTO 93, PCA, MTC y RNE.* 