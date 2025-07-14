@echo off
echo ========================================
echo EJECUTANDO APP PAVIMENTOS
echo ========================================
echo.

echo Iniciando aplicacion Streamlit...
echo.
echo La app se abrira en tu navegador en:
echo http://localhost:8501
echo.
echo Presiona Ctrl+C para detener la app
echo.

python -m streamlit run APP.py --server.port 8501

pause 