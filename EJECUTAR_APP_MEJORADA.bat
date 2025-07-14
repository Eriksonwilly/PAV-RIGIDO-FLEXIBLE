@echo off
echo ========================================
echo    CONSORCIO DEJ - APP MEJORADA
echo ========================================
echo.
echo Iniciando aplicacion de pavimentos...
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor instale Python 3.8+ desde https://python.org
    pause
    exit /b 1
)

REM Verificar si Streamlit está instalado
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Instalando Streamlit...
    pip install streamlit
    if errorlevel 1 (
        echo ERROR: No se pudo instalar Streamlit
        pause
        exit /b 1
    )
)

REM Verificar otras dependencias
echo Verificando dependencias...
python -c "import numpy, matplotlib, pandas" >nul 2>&1
if errorlevel 1 (
    echo Instalando dependencias básicas...
    pip install numpy matplotlib pandas
)

echo.
echo ========================================
echo    INICIANDO APLICACION
echo ========================================
echo.
echo La aplicación se abrirá en tu navegador
echo URL: http://localhost:8501
echo.
echo Para detener la aplicación, presiona Ctrl+C
echo.

REM Ejecutar la aplicación
streamlit run APP.py --server.port 8501 --server.headless false

echo.
echo Aplicacion detenida.
pause 