@echo off
echo ========================================
echo    INSTALACION DEPENDENCIAS BASICAS
echo    CONSORCIO DEJ - Software de Pavimentos
echo ========================================
echo.

echo [1/4] Instalando dependencias principales...
pip install streamlit>=1.28.0
if %errorlevel% neq 0 (
    echo Error instalando streamlit
    pause
    exit /b 1
)

echo [2/4] Instalando librerias de datos...
pip install pandas>=1.5.0
pip install numpy>=1.21.0
pip install openpyxl>=3.0.0
pip install scipy>=1.9.0

echo [3/4] Instalando librerias de graficos...
pip install matplotlib>=3.5.0
pip install plotly>=5.0.0

echo [4/4] Instalando librerias de reportes...
pip install reportlab>=3.6.0

echo.
echo ========================================
echo    INSTALACION COMPLETADA
echo ========================================
echo.
echo Para ejecutar la aplicacion:
echo   streamlit run APP.py
echo.
echo Para instalar dependencias LiDAR opcionales:
echo   pip install laspy open3d rasterio earthengine-api geemap pyautocad scikit-learn
echo.
echo ========================================
pause 