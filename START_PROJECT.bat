@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title Collatz Conjecture Reel

if not exist ".venv\Scripts\python.exe" (
    echo First run detected. Starting setup...
    call SETUP.bat
    if errorlevel 1 exit /b 1
)

:menu
cls
echo ============================================================
echo             COLLATZ CONJECTURE - REEL PROJECT
echo ============================================================
echo.
echo   1. Quick preview of the complete reel
 echo 2. Final HD reel (1080x1920, 60 FPS)
echo   3. Render one scene
  4. Open project folder
  5. Setup / repair dependencies
  6. Push / Update Git repository
  0. Exit
echo.
set /p choice=Choose an option: 

if "%choice%"=="1" goto preview
if "%choice%"=="2" goto hd
if "%choice%"=="3" goto scene
if "%choice%"=="4" start "Project Folder" explorer "%CD%" & goto menu
if "%choice%"=="5" call SETUP.bat & goto menu
if "%choice%"=="6" call git-update.bat & goto menu
if "%choice%"=="0" exit /b 0
goto menu

:preview
cls
echo Rendering quick preview...
"%CD%\.venv\Scripts\python.exe" render_all.py --quality low
if errorlevel 1 pause
goto menu

:hd
cls
echo Rendering FINAL HD reel. This can take a while...
"%CD%\.venv\Scripts\python.exe" render_all.py --quality high
if errorlevel 1 pause
goto menu

:scene
cls
echo Available scenes: intro, sequence, trajectory, bars, comparison, spiral, stats, conclusion
echo.
set /p scene=Enter scene name: 
"%CD%\.venv\Scripts\python.exe" quick_render.py "%scene%"
pause
goto menu
