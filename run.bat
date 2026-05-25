@echo off
setlocal

set VIMA_PORT=9021
set CHAT_PORT=3333
set SCRIPT_DIR=%~dp0
set CHAT_DIR=%SCRIPT_DIR%chat

if /i "%~1"=="stop" goto :stop
goto :start

:stop
echo Stopping vima on port %VIMA_PORT%...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":%VIMA_PORT% " ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo Stopping vima-chat on port %CHAT_PORT%...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":%CHAT_PORT% " ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo All servers stopped.
goto :end

:start
REM Free ports
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":%VIMA_PORT% " ^| findstr "LISTENING"') do (
    echo Stopping existing process on port %VIMA_PORT%...
    taskkill /F /PID %%a >nul 2>&1
)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":%CHAT_PORT% " ^| findstr "LISTENING"') do (
    echo Stopping existing process on port %CHAT_PORT%...
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
    "%SCRIPT_DIR%.venv\Scripts\python.exe" -m pip install --use-feature=truststore -r requirements.txt -r chat\requirements.txt --quiet 2>nul
) else (
    py -m pip install --use-feature=truststore -r requirements.txt -r chat\requirements.txt --quiet 2>nul
)

REM Start vima-chat in background if chat\ exists
if exist "%CHAT_DIR%\app.py" (
    echo Starting vima-chat on http://127.0.0.1:%CHAT_PORT%
    if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
        start /B "" "%SCRIPT_DIR%.venv\Scripts\python.exe" "%CHAT_DIR%\app.py" > "%CHAT_DIR%\server.log" 2>&1
    ) else (
        start /B "" py "%CHAT_DIR%\app.py" > "%CHAT_DIR%\server.log" 2>&1
    )
    echo vima-chat starting in background ^(logs: chat\server.log^)
) else (
    echo Warning: chat\app.py not found - skipping vima-chat
)

REM Start vima in foreground
echo Starting vima on http://127.0.0.1:%VIMA_PORT%
if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    "%SCRIPT_DIR%.venv\Scripts\python.exe" app.py
) else (
    py app.py
)

:end
endlocal
