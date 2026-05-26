@echo off
setlocal

set VIMA_PORT=9021
set SCRIPT_DIR=%~dp0

if /i "%~1"=="stop" goto :stop
goto :start

:stop
echo Stopping vima on port %VIMA_PORT%...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":%VIMA_PORT% " ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo Server stopped.
goto :end

:start
REM Free port
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":%VIMA_PORT% " ^| findstr "LISTENING"') do (
    echo Stopping existing process on port %VIMA_PORT%...
    taskkill /F /PID %%a >nul 2>&1
)

REM Activate venv if present
if exist "%SCRIPT_DIR%.venv\Scripts\activate.bat" (
    call "%SCRIPT_DIR%.venv\Scripts\activate.bat"
)

cd /d "%SCRIPT_DIR%"

REM Install dependencies using OS cert store (handles corporate proxies)
echo Installing dependencies...
if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    "%SCRIPT_DIR%.venv\Scripts\python.exe" -m pip install --use-feature=truststore -r requirements.txt --quiet 2>nul
) else (
    py -m pip install --use-feature=truststore -r requirements.txt --quiet 2>nul
)

REM ── Set up key-automation tool (once, on first run) ──────────────────
set TOOL_DIR=%SCRIPT_DIR%tools\mcd-key-automation
set TOOL_VENV=%TOOL_DIR%\.venv
if not exist "%TOOL_VENV%\Scripts\python.exe" (
    echo Setting up API key automation tool (first run only^)...
    if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
        "%SCRIPT_DIR%.venv\Scripts\python.exe" -m venv "%TOOL_VENV%"
    ) else (
        py -m venv "%TOOL_VENV%"
    )
    "%TOOL_VENV%\Scripts\pip.exe" install --use-feature=truststore -q -e "%TOOL_DIR%" 2>nul
    echo Installing browser for key automation...
    "%TOOL_VENV%\Scripts\playwright.exe" install chromium
    echo API key automation tool ready.
)

REM Start vima (Vima Chat is now embedded in-process at /chat)
echo Starting Mastercard Solution Studio on http://127.0.0.1:%VIMA_PORT%
if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    "%SCRIPT_DIR%.venv\Scripts\python.exe" app.py
) else (
    py app.py
)

:end
endlocal
