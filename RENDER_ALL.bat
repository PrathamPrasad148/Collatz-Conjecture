@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" call SETUP.bat
if errorlevel 1 exit /b 1
"%CD%\.venv\Scripts\python.exe" render_all.py --quality high
pause
