@echo off
setlocal enabledelayedexpansion

REM Force the virtual environment to be used
set VIRTUAL_ENV=%~dp0.venv
set PYTHONPATH=%VIRTUAL_ENV%\Lib\site-packages
set PYTHONHOME=
set PATH=%VIRTUAL_ENV%\Scripts;%PATH%

REM Verify it exists
if not exist "%VIRTUAL_ENV%\Scripts\python.exe" (
    echo ERROR: Virtual environment not found at %VIRTUAL_ENV%
    exit /b 1
)

echo Using Python: %VIRTUAL_ENV%\Scripts\python.exe
echo Running: main.py

REM Run the app
"%VIRTUAL_ENV%\Scripts\python.exe" "%~dp0main.py" %*

pause
