@echo off
echo ========================================
echo INSTALACION DE DEPENDENCIAS - APP PAVIMENTOS
echo ========================================
echo.

echo Instalando dependencias principales...
pip install streamlit numpy matplotlib pandas plotly reportlab

echo.
echo Verificando instalacion...
python -c "import streamlit, numpy, matplotlib, pandas, plotly, reportlab; print('Todas las dependencias instaladas correctamente')"

echo.
echo ========================================
echo INSTALACION COMPLETADA
echo ========================================
echo.
echo Para ejecutar la app:
echo python -m streamlit run APP.py --server.port 8501
echo.
pause 