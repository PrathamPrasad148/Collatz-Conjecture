@echo off
setlocal EnableExtensions EnableDelayedExpansion
cd /d "%~dp0"
title Collatz Conjecture Reel - Git Update

echo ============================================================
echo             COLLATZ REEL - GIT PUSH / RE-INITIALIZE
echo ============================================================
echo.

:: 1. Check if git is installed
where git >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git is not found on your system PATH.
    echo Please install Git from https://git-scm.com/ and try again.
    echo.
    pause
    exit /b 1
)

:: 2. Check or initialize local git repository
if not exist ".git" (
    echo [*] No Git repository detected. Initializing new repository...
    git init
    if errorlevel 1 (
        echo [ERROR] Failed to initialize Git repository.
        pause
        exit /b 1
    )
    git branch -M main
    echo [+] Repository initialized with default branch 'main'.
) else (
    echo [*] Existing Git repository detected.
)
echo.

:: 3. Remote URL detection and setup
set "REPO_URL="
for /f "delims=" %%u in ('git remote get-url origin 2^>nul') do set "REPO_URL=%%u"

:: If a URL was passed as command line argument %1, use it
if not "%~1"=="" (
    set "TARGET_URL=%~1"
    if "!REPO_URL!"=="" (
        echo [*] Adding remote origin: !TARGET_URL!
        git remote add origin "!TARGET_URL!"
    ) else (
        echo [*] Updating remote origin to: !TARGET_URL!
        git remote set-url origin "!TARGET_URL!"
    )
    set "REPO_URL=!TARGET_URL!"
) else (
    if "!REPO_URL!"=="" (
        echo [!] No remote repository is configured.
        echo.
        set /p "TARGET_URL=Enter your remote Git repository URL (e.g., https://github.com/user/collatz-reel.git): "
        if "!TARGET_URL!"=="" (
            echo [ERROR] No remote repository URL provided. Aborting.
            pause
            exit /b 1
        )
        git remote add origin "!TARGET_URL!"
        set "REPO_URL=!TARGET_URL!"
        echo [+] Remote origin configured: !REPO_URL!
    ) else (
        echo Current remote origin: !REPO_URL!
        set /p "CHANGE_URL=Press ENTER to keep this remote, or enter a new URL: "
        if not "!CHANGE_URL!"=="" (
            git remote set-url origin "!CHANGE_URL!"
            set "REPO_URL=!CHANGE_URL!"
            echo [+] Remote origin updated to: !REPO_URL!
        )
    )
)
echo.

:: 4. Erase all old history/data and replace with current clean snapshot
echo ============================================================
echo   PREPARING CLEAN CODEBASE (WIPING REMOTE & REPLACING)
echo ============================================================
echo.
echo [*] Creating fresh orphan branch to wipe prior history...
git checkout --orphan temp_fresh_branch >nul 2>&1
if errorlevel 1 (
    git checkout -b temp_fresh_branch >nul 2>&1
)

echo [*] Staging all current project files...
git add -A

echo [*] Creating clean snapshot commit...
git commit -m "Collatz Reel: complete visual redesign & production update" --allow-empty

echo [*] Setting branch to main...
git branch -D main >nul 2>&1
git branch -m main

echo.
echo ============================================================
echo   FORCE-PUSHING TO REMOTE REPOSITORY
echo ============================================================
echo Target: !REPO_URL!
echo.
echo [*] Overwriting remote repository with current code...
git push -u origin main --force

if errorlevel 1 (
    echo.
    echo [ERROR] Push failed!
    echo Possible causes:
    echo  1. Authentication issue (ensure you are logged into GitHub/GitLab).
    echo  2. Incorrect remote URL.
    echo  3. Repository permission restrictions.
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   SUCCESS! All code has been pushed cleanly to:
echo   !REPO_URL!
echo ============================================================
echo.
pause
exit /b 0

