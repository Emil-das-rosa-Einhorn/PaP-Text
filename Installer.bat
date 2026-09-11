@echo off
:: ============================================================
:: Auto-UAC: Requesting Admin rights
:: ============================================================
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting Admin rights...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

setlocal enabledelayedexpansion

echo ============================================================
echo         Game-Instalation-Skript (Windows)
echo ============================================================
echo.

set "FOLDER_NAME=PaP-Adventure"
set /p FOLDER_NAME="Choose the name of the Gamefolder (default: PaP-Adventure): "
set "TARGET_DIR=%LOCALAPPDATA%\%FOLDER_NAME%"

echo.
echo Zielordner: %TARGET_DIR%
echo.

if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"
if not exist "%TARGET_DIR%\updates" mkdir "%TARGET_DIR%\updates"
if not exist "%TARGET_DIR%\gamefiles" mkdir "%TARGET_DIR%\gamefile"

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing Python 3.12 via winget...
    winget install Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements
    
    :: Pfad fuer die aktuelle Session aktualisieren
    set "PATH=%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%ProgramFiles%\Python312;%ProgramFiles%\Python312\Scripts;%PATH%"
) else (
    echo [OK] Python installt already.
)

set "RAW_BASE_URL=https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/PaP-Text/refs/heads/main/"

echo.
echo Loading requiered Gamedata...

powershell -Command "Invoke-WebRequest -Uri '%RAW_BASE_URL%/RPG-Main.py' -OutFile '%TARGET_DIR%\RPG-Main.py'"
powershell -Command "Invoke-WebRequest -Uri '%RAW_BASE_URL%/loader.py' -OutFile '%TARGET_DIR%\loader.py'"
powershell -Command "Invoke-WebRequest -Uri '%RAW_BASE_URL%/assets.py' -OutFile '%TARGET_DIR%\assets.py'"
powershell -Command "Invoke-WebRequest -Uri '%RAW_BASE_URL%/LICENSE' -OutFile '%TARGET_DIR%\LICENSE'"
powershell -Command "Invoke-WebRequest -Uri '%RAW_BASE_URL%/updater.py' -OutFile '%TARGET_DIR%\updater.py'"
powershell -Command "Invoke-WebRequest -Uri '%RAW_BASE_URL%/requirements.txt' -OutFile '%TARGET_DIR%\requirements.txt'"

echo [OK] Succsessfully downloaded.

cd /d "%TARGET_DIR%"

echo.
echo Instaling requirements...

if exist "requirements.txt" (
    python -m pip install --upgrade pip --quiet
    python -m pip install -r requirements.txt
    echo [OK] Requirements installt succsesfully.
) else (
    echo [WARNUNG] No requirements found.
)

echo @echo off > "%TARGET_DIR%\start_game.bat"
echo title Game starter >> "%TARGET_DIR%\start_game.bat"
echo cd /d "%%~dp0" >> "%TARGET_DIR%\start_game.bat"
echo echo current dir: %%cd%% >> "%TARGET_DIR%\start_game.bat"
echo echo Starting Game... >> "%TARGET_DIR%\start_game.bat"
echo python RPG-Main.py >> "%TARGET_DIR%\start_game.bat"
echo pause >> "%TARGET_DIR%\start_game.bat"

echo.
set /p CREATE_SHORTCUT="Do you want to create a Shortcut on the Desktop? (J/N): "

if /i "%CREATE_SHORTCUT%"=="J" (
    echo Creating Shortcut...
    powershell -Command "$desktop = [Environment]::GetFolderPath('Desktop'); $ws = New-Object -ComObject WScript.Shell; $sc = $ws.CreateShortcut(\"$desktop\%FOLDER_NAME%.lnk\"); $sc.TargetPath = '%TARGET_DIR%\start_game.bat'; $sc.WorkingDirectory = '%TARGET_DIR%'; $sc.Save()"
    echo [OK] shortcut created.
) else (
    echo No shortcut created.
)

echo.
echo ============================================================
echo   Insalation Succsesfull!
echo.
echo   lokation: %TARGET_DIR%
echo   To start the Game klick "start_game.bat" in the Game direktory or use the Shortcut.
echo ============================================================
echo.
pause