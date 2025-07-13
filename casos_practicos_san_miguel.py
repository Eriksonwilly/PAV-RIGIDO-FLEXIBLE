#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CASOS PRÁCTICOS - SAN MIGUEL, PUNO
===================================

Este script demuestra cómo usar la app de pavimentos para los casos prácticos:
1. Pavimento Rígido - 100 metros
2. Pavimento Flexible - 100 metros

Ubicación: San Miguel, Puno (altitud > 3800 msnm)
Longitud: 100 metros para cada caso
"""

import streamlit as st
import pandas as pd

def mostrar_caso_practico_rigido():
    """
    Caso práctico: Pavimento Rígido - San Miguel, Puno
    """
    st.markdown("""
    ## 🏗️ CASO PRÁCTICO: PAVIMENTO RÍGIDO
    ### Ubicación: San Miguel, Puno - 100 metros
    
    **Datos del Proyecto:**
    - Proyecto: "Pavimento Rígido - San Miguel"
    - Descripción: "Pavimento rígido para vía urbana en San Miguel, Puno"
    - Período de diseño: 20 años
    - Sistema de unidades: SI (Internacional)
    
    **Parámetros de Diseño:**
    - Espesor de losa: 200 mm
    - Módulo de rotura: 4.5 MPa
    - K (módulo de reacción): 50 MPa/m (CBR = 5%)
    - Dovelas: Sí
    - Bermas: No
    - Subbase: Sí, 200 mm, sin tratar
    - Acero fy: 280 MPa
    - Ancho carril: 3.05 m
    
    **Parámetros AASHTO 93:**
    - ZR: -1.645 (95% confiabilidad)
    - S0: 0.35
    - ΔPSI: 1.5
    
    **Tabla de Tránsito (por defecto):**
    - Carga: 134, 125, 116, 107, 98, 89, 80, 71, 62 kN
    - Repeticiones: 6310, 14690, 30140, 106900, 233500, 422500, 586900, 1837000, 0
    - W18 total: ~3,212,940 ejes equivalentes
    
    **Resultados Esperados:**
    - Espesor de losa calculado: ~200-250 mm
    - Junta máxima: ~4.8 m
    - Área de acero por temperatura: ~150-200 mm²
    - Porcentaje de fatiga: ~32.80%
    - Porcentaje de erosión: ~32.80%
    
    **Pasos para usar la app:**
    1. Llenar datos del proyecto
    2. Configurar parámetros de diseño
    3. Presionar "🚀 Calcular"
    4. Generar PDF Premium con "🚀 Generar PDF Premium Pavimento Rígido"
    """)

def mostrar_caso_practico_flexible():
    """
    Caso práctico: Pavimento Flexible - San Miguel, Puno
    """
    st.markdown("""
    ## 🛣️ CASO PRÁCTICO: PAVIMENTO FLEXIBLE
    ### Ubicación: San Miguel, Puno - 100 metros
    
    **Datos del Proyecto:**
    - Proyecto: "Pavimento Flexible - San Miguel"
    - Descripción: "Pavimento flexible para vía urbana en San Miguel, Puno"
    - Período de diseño: 20 años
    - Sistema de unidades: SI (Internacional)
    
    **Parámetros de Diseño AASHTO 93:**
    - a₁ (coef. capa asfáltica): 0.44
    - D₁ (espesor asfalto): 4.0 pulg
    - a₂ (coef. base): 0.14
    - D₂ (espesor base): 8.0 pulg
    - m₂ (factor drenaje base): 1.0
    - a₃ (coef. subbase): 0.11
    - D₃ (espesor subbase): 6.0 pulg
    - m₃ (factor drenaje subbase): 1.0
    
    **Análisis de Fatiga (MEPDG):**
    - k₁ (constante): 0.0796
    - k₂ (exponente εt): 3.291
    - k₃ (exponente E): 0.854
    - εt (deformación): 70 microstrain
    - E (módulo elasticidad): 4000 MPa
    
    **Resultados Esperados:**
    - Número estructural SN: ~3.54
    - Número de ciclos hasta falla (Nf): ~1,000,000+
    
    **Pasos para usar la app:**
    1. Ir a la pestaña "Pavimento Flexible"
    2. Llenar parámetros del número estructural
    3. Presionar "Calcular Número Estructural SN"
    4. Generar PDF Premium con "🚀 Generar PDF Premium Pavimento Flexible"
    5. Llenar parámetros de fatiga del asfalto
    6. Presionar "Calcular Fatiga del Asfalto"
    7. Generar PDF Premium con "🚀 Generar PDF Premium Análisis de Fatiga"
    """)

def mostrar_instrucciones_generales():
    """
    Instrucciones generales para usar la app
    """
    st.markdown("""
    ## 📋 INSTRUCCIONES GENERALES
    
    ### 🔐 Acceso a la App:
    1. Usuario: **admin** / Contraseña: **admin123**
    2. O Usuario: **demo** / Contraseña: **demo**
    
    ### 📊 Para Pavimento Rígido:
    1. **Panel Izquierdo:** Llenar datos del proyecto
    2. **Panel Central:** Configurar tabla de tránsito
    3. **Panel Derecho:** Presionar "🚀 Calcular"
    4. **Resultados:** Revisar espesor, fatiga, erosión
    5. **PDF Premium:** Generar reporte completo
    
    ### 🛣️ Para Pavimento Flexible:
    1. **Pestaña "Pavimento Flexible"**
    2. **Sección 2.1:** Calcular número estructural
    3. **Sección 2.2:** Analizar fatiga del asfalto
    4. **PDF Premium:** Generar reportes específicos
    
    ### 📄 Generación de PDFs Premium:
    - **Pavimento Rígido:** Reporte completo con análisis AASHTO 93
    - **Pavimento Flexible:** Reporte con número estructural y fatiga
    - **Análisis de Fatiga:** Reporte específico MEPDG
    
    ### 🎯 Características de los PDFs Premium:
    - Portada profesional con logo CONSORCIO DEJ
    - Índice detallado con paginación
    - Datos del proyecto específicos para San Miguel, Puno
    - Análisis técnico completo
    - Gráficos de sensibilidad
    - Recomendaciones técnicas
    - Certificación y conclusiones
    - Pie de página con paginación
    """)

def main():
    """
    Función principal para mostrar los casos prácticos
    """
    st.set_page_config(
        page_title="Casos Prácticos - San Miguel, Puno",
        page_icon="🏔️",
        layout="wide"
    )
    
    st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: #FFD700; color: #2F2F2F; border-radius: 10px; margin-bottom: 20px;">
        <h1>🏔️ CASOS PRÁCTICOS - SAN MIGUEL, PUNO</h1>
        <p style="font-size: 18px;">Diseño de Pavimentos para 100 metros de vía urbana</p>
        <p style="font-size: 14px;">Altitud: > 3800 msnm | Ubicación: San Miguel, Puno</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs para organizar los casos
    tab1, tab2, tab3 = st.tabs([
        "📋 Instrucciones Generales",
        "🏗️ Pavimento Rígido",
        "🛣️ Pavimento Flexible"
    ])
    
    with tab1:
        mostrar_instrucciones_generales()
    
    with tab2:
        mostrar_caso_practico_rigido()
    
    with tab3:
        mostrar_caso_practico_flexible()
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 10px; background-color: #f0f0f0; border-radius: 5px;">
        <p><strong>CONSORCIO DEJ</strong> - Sistema de Diseño de Pavimentos</p>
        <p>Desarrollado con Streamlit + Python | Normativas: AASHTO 93, PCA, MEPDG, MTC, RNE</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 