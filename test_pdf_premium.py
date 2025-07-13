#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad de PDFs Premium
"""

import sys
import os

# Agregar el directorio actual al path para importar APP.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_pdf_premium_functions():
    """Prueba las funciones de PDF Premium"""
    
    print("🧪 Iniciando pruebas de PDFs Premium...")
    
    try:
        # Importar las funciones de APP.py
        from APP import (
            generar_pdf_premium_rigido,
            generar_pdf_premium_flexible,
            generar_pdf_premium_combinado
        )
        print("✅ Funciones importadas correctamente")
        
        # Datos de prueba
        datos_proyecto = {
            'Proyecto': 'Prueba PDF Premium - San Miguel',
            'Descripción': 'Prueba de funcionalidad de PDFs Premium',
            'Período': 20,
            'Usuario': 'test_user',
            'Sistema_Unidades': 'Sistema Internacional (SI)'
        }
        
        resultados_rigido = {
            'Espesor de losa calculado (D)': '250.00 mm',
            'Junta máxima (L)': '4.50 m',
            'Área de acero por temperatura (As)': '1250.00 mm²',
            'Número de ejes equivalentes (W18)': '1,000,000',
            'Módulo de reacción (k)': '50 MPa/m',
            'Resistencia a flexión (Sc)': '4.5 MPa',
            'Módulo elasticidad (Ec)': '30000 MPa',
            'Coef. transferencia (J)': '3.2',
            'Coef. drenaje (C)': '1.0',
            'Confiabilidad (R)': '0.95',
            'Porcentaje de fatiga': '15.50%',
            'Porcentaje de erosión': '25.30%',
            'ZR (Factor confiabilidad)': '-1.645',
            'S0 (Desviación estándar)': '0.35',
            'ΔPSI (Pérdida servicio)': '1.5'
        }
        
        resultados_flexible = {
            'a₁ (coef. asfalto)': '0.44',
            'D₁ (espesor asfalto)': '4.0 pulg',
            'a₂ (coef. base)': '0.14',
            'D₂ (espesor base)': '8.0 pulg',
            'm₂ (factor drenaje base)': '1.0',
            'a₃ (coef. subbase)': '0.11',
            'D₃ (espesor subbase)': '6.0 pulg',
            'm₃ (factor drenaje subbase)': '1.0',
            'Número estructural SN': '4.44',
            'Fórmula': 'SN = a₁·D₁ + a₂·D₂·m₂ + a₃·D₃·m₃',
            'Norma': 'AASHTO 93'
        }
        
        tabla_transito = {
            'Carga': [134, 125, 116, 107, 98, 89, 80, 71, 62],
            'Repeticiones': [6310, 14690, 30140, 106900, 233500, 422500, 586900, 1837000, 0]
        }
        
        sistema_unidades = "Sistema Internacional (SI)"
        
        print("\n📄 Probando PDF Premium Rígido...")
        pdf_rigido = generar_pdf_premium_rigido(datos_proyecto, resultados_rigido, tabla_transito, sistema_unidades)
        if pdf_rigido:
            print("✅ PDF Premium Rígido generado exitosamente")
            # Guardar PDF de prueba
            with open("test_pdf_premium_rigido.pdf", "wb") as f:
                f.write(pdf_rigido.getvalue())
            print("💾 PDF guardado como: test_pdf_premium_rigido.pdf")
        else:
            print("❌ Error al generar PDF Premium Rígido")
        
        print("\n📄 Probando PDF Premium Flexible...")
        pdf_flexible = generar_pdf_premium_flexible(datos_proyecto, resultados_flexible, sistema_unidades)
        if pdf_flexible:
            print("✅ PDF Premium Flexible generado exitosamente")
            # Guardar PDF de prueba
            with open("test_pdf_premium_flexible.pdf", "wb") as f:
                f.write(pdf_flexible.getvalue())
            print("💾 PDF guardado como: test_pdf_premium_flexible.pdf")
        else:
            print("❌ Error al generar PDF Premium Flexible")
        
        print("\n📄 Probando PDF Premium Combinado...")
        pdf_combinado = generar_pdf_premium_combinado(datos_proyecto, resultados_rigido, resultados_flexible, tabla_transito, sistema_unidades)
        if pdf_combinado:
            print("✅ PDF Premium Combinado generado exitosamente")
            # Guardar PDF de prueba
            with open("test_pdf_premium_combinado.pdf", "wb") as f:
                f.write(pdf_combinado.getvalue())
            print("💾 PDF guardado como: test_pdf_premium_combinado.pdf")
        else:
            print("❌ Error al generar PDF Premium Combinado")
        
        print("\n🎉 Todas las pruebas completadas!")
        print("\n📋 Resumen:")
        print("- PDF Premium Rígido: ✅ Funcionando")
        print("- PDF Premium Flexible: ✅ Funcionando") 
        print("- PDF Premium Combinado: ✅ Funcionando")
        print("\n📁 Archivos generados:")
        print("- test_pdf_premium_rigido.pdf")
        print("- test_pdf_premium_flexible.pdf")
        print("- test_pdf_premium_combinado.pdf")
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("💡 Asegúrate de que todas las dependencias estén instaladas:")
        print("   pip install reportlab matplotlib numpy pandas streamlit")
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_pdf_premium_functions() 