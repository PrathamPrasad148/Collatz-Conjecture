@echo off
setlocal EnableExtensions
cd /d "%~dp0"

title Collatz Reel - Setup

echo ============================================================
echo        COLLATZ CONJECTURE REEL - FIRST TIME SETUP
echo ============================================================
echo.

rem Prefer a Python version supported by current Manim.
set "PY_CMD="
py -3.13 -c "import sys; print(sys.version)" >nul 2>nul && set "PY_CMD=py -3.13"
if not defined PY_CMD py -3.12 -c "import sys; print(sys.version)" >nul 2>nul && set "PY_CMD=py -3.12"
if not defined PY_CMD py -3.11 -c "import sys; print(sys.version)" >nul 2>nul && set "PY_CMD=py -3.11"

if not defined PY_CMD (
    echo ERROR: Python 3.11, 3.12, or 3.13 was not found.
    echo Install Python from https://www.python.org/downloads/
    echo and make sure the Python Launcher is installed.
    pause
    exit /b 1
)

%PY_CMD% -c "import sys; print('Using Python:', sys.version)"

echo.
echo Creating local virtual environment...
if not exist ".venv\Scripts\python.exe" (
    %PY_CMD% -m venv .venv
    if errorlevel 1 (
        echo ERROR: Could not create the virtual environment.
        pause
        exit /b 1
    )
)

set "VENV_PY=%CD%\.venv\Scripts\python.exe"

echo Updating pip...
"%VENV_PY%" -m pip install --upgrade pip setuptools wheel
if errorlevel 1 goto :pip_error

echo.
echo Installing Manim and project dependencies...
"%VENV_PY%" -m pip install -r requirements.txt
if errorlevel 1 goto :pip_error

echo.

where ffmpeg >nul 2>nul
if errorlevel 1 (
    echo FFmpeg was not found. Trying to install it automatically with WinGet...
    where winget >nul 2>nul
    if errorlevel 1 (
        echo WARNING: WinGet is not available. FFmpeg must be installed manually.
    ) else (
        winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
        if errorlevel 1 echo WARNING: Automatic FFmpeg installation failed. Install it manually.
    )
) else (
    echo FFmpeg found: OK
)

echo.
echo ============================================================
echo SETUP COMPLETE
 echo ============================================================
echo.
echo Double-click START_PROJECT.bat to render the project.
pause
exit /b 0

:pip_error
echo.
echo ERROR: Dependency installation failed.
echo Check your internet connection and try SETUP.bat again.
echo If pip reports a Python-version problem, install Python 3.11-3.13.
pause
exit /b 1
