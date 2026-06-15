@echo off
setlocal

REM Navigate to script directory
cd /d "%~dp0"

REM Absolute paths
set VENV_DIR=%cd%\.venv
set PYTHON_EXE=%VENV_DIR%\Scripts\python.exe
set MAIN_PY=%cd%\main.py

REM Check if venv exists
if not exist "%PYTHON_EXE%" (
    echo.
    echo ERROR: Virtual environment not found!
    echo Expected path: %PYTHON_EXE%
    echo.
    echo Please run: python -m venv .venv
    echo Then run: .\.venv\Scripts\pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

REM Clear any conflicting environment variables
set PYTHONHOME=
set PYTHONPATH=
set UV_PYTHON=

REM Set venv-specific variables
set VIRTUAL_ENV=%VENV_DIR%
set PATH=%VENV_DIR%\Scripts;%PATH%

REM Display diagnostic info
echo.
echo ========================================
echo Starting Cosmic Portfolio
echo ========================================
echo Python: %PYTHON_EXE%
echo Virtual Env: %VIRTUAL_ENV%
echo Script: %MAIN_PY%
echo.

REM Verify packages
"%PYTHON_EXE%" -c "import flet; import flet_desktop; print('Packages verified OK')" || (
    echo.
    echo ERROR: Required packages not found!
    echo Installing now...
    "%PYTHON_EXE%" -m pip install flet flet-desktop
)

echo.
echo Running application...
echo.

REM Run the app
"%PYTHON_EXE%" "%MAIN_PY%"

pause
