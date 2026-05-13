@echo off
setlocal

set PORT=9021
set SCRIPT_DIR=%~dp0

if /i "%~1"=="stop" goto :stop
goto :start

:stop
echo Stopping server on port %PORT%...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":%PORT% " ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo Done.
goto :end

:start
REM Kill any process already listening on the port
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":%PORT% " ^| findstr "LISTENING"') do (
    echo Stopping existing server on port %PORT%...
    taskkill /F /PID %%a >nul 2>&1
)

REM Activate venv if present
if exist "%SCRIPT_DIR%.venv\Scripts\activate.bat" (
    call "%SCRIPT_DIR%.venv\Scripts\activate.bat"
)

echo Starting vima on http://127.0.0.1:%PORT%
cd /d "%SCRIPT_DIR%"

REM Try venv python, then py launcher, then python on PATH
if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    "%SCRIPT_DIR%.venv\Scripts\python.exe" app.py
) else (
    py app.py
)

:end
endlocal
