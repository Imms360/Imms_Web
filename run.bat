@echo off
REM Run the Flet app using the virtual environment
cd /d "%~dp0"
.\.venv\Scripts\python.exe main.py %*
pause
