@echo off
setlocal

set VIMA_PORT=9021
set SCRIPT_DIR=%~dp0
set APP_ARGS=%*

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

REM Detect a Python launcher to use when no project venv is present
where py >nul 2>&1
if not errorlevel 1 (set PYLAUNCHER=py) else (set PYLAUNCHER=python)
where %PYLAUNCHER% >nul 2>&1
if errorlevel 1 (
    echo ERROR: No Python found. Install Python from https://www.python.org/downloads/ then re-run.
    goto :end
)

REM Install dependencies only when requirements.txt changed since last install
set DEPS_MARKER=%SCRIPT_DIR%.venv\.deps-installed
if not exist "%SCRIPT_DIR%.venv\Scripts\python.exe" set DEPS_MARKER=%SCRIPT_DIR%.deps-installed
set REQ_HASH=
for /f "usebackq delims=" %%h in (`powershell -NoProfile -Command "(Get-FileHash '%SCRIPT_DIR%requirements.txt' -Algorithm SHA256).Hash"`) do set REQ_HASH=%%h
set STORED_HASH=
if exist "%DEPS_MARKER%" set /p STORED_HASH=<"%DEPS_MARKER%"
if "%REQ_HASH%"=="%STORED_HASH%" (
    echo Dependencies already up to date, skipping install.
) else (
    REM Install dependencies using OS cert store (handles corporate proxies)
    echo Installing dependencies...
    if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
        "%SCRIPT_DIR%.venv\Scripts\python.exe" -m pip install -r requirements.txt --quiet --no-warn-script-location
    ) else (
        %PYLAUNCHER% -m pip install -r requirements.txt --quiet --no-warn-script-location
    )
    if errorlevel 1 (
        echo ERROR: Failed to install Python dependencies. Aborting.
        goto :end
    )
    >"%DEPS_MARKER%" echo %REQ_HASH%
)

REM ── Set up key-automation tool (once, on first run) ──────────────────
REM Use a sentinel file as the install marker - python.exe alone is not
REM enough because it exists immediately after `python -m venv` even if the
REM subsequent pip install failed, leaving auto-provisioning broken.
REM We avoid pip-generated console_script .exe shims (e.g. playwright.exe,
REM mcd-key-automation.exe) so corporate AV / lockdown policies that block
REM unsigned generated executables don't break setup.
set TOOL_DIR=%SCRIPT_DIR%tools\mcd-key-automation
set TOOL_VENV=%TOOL_DIR%\.venv
set TOOL_PY=%TOOL_VENV%\Scripts\python.exe
set TOOL_MARKER=%TOOL_VENV%\.tool-installed
if not exist "%TOOL_MARKER%" (
    echo.
    echo Setting up API key automation tool ^(first run only^)...
    if exist "%TOOL_PY%" (
        echo   Detected incomplete tool venv from a previous run - reinstalling...
    )
    echo   [1/4] Creating Python virtual environment...
    if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
        "%SCRIPT_DIR%.venv\Scripts\python.exe" -m venv "%TOOL_VENV%"
    ) else (
        %PYLAUNCHER% -m venv "%TOOL_VENV%"
    )
    if errorlevel 1 (
        echo ERROR: Failed to create tool virtual environment. Aborting.
        goto :end
    )
    echo   [2/4] Upgrading pip ^(required for truststore support^)...
    "%TOOL_PY%" -m pip install --upgrade pip --quiet --no-warn-script-location
    if errorlevel 1 (
        echo ERROR: Failed to upgrade pip in tool venv. Aborting.
        goto :end
    )
    echo   [3/4] Installing dependencies via python -m pip ^(no .exe shims, this may take a minute^)...
    "%TOOL_PY%" -m pip install -r "%TOOL_DIR%\requirements.txt" --no-warn-script-location
    if errorlevel 1 (
        echo ERROR: Failed to install key-automation tool dependencies. Aborting.
        goto :end
    )
    echo   [4/4] Installing browser via python -m playwright ^(downloading, please wait^)...
    "%TOOL_PY%" -m playwright install chromium
    if errorlevel 1 (
        echo.
        echo WARNING: Playwright chromium download failed ^(often blocked by
        echo          corporate proxies^). Falling back to system-installed Edge.
        echo          Set PLAYWRIGHT_BROWSER_CHANNEL=msedge to use it.
        echo.
        REM Persist a skip marker so we don't keep retrying the download every run.
        echo skipped > "%TOOL_VENV%\.chromium-skipped"
    )
    REM Belt-and-braces: remove any pip-generated console_script .exe shims.
    if exist "%TOOL_VENV%\Scripts\mcd-key-automation.exe" del /q "%TOOL_VENV%\Scripts\mcd-key-automation.exe" >nul 2>&1
    REM Touch the install-complete marker last so a partial install retries next run.
    echo installed > "%TOOL_MARKER%"
    echo.
    echo API key automation tool ready.
    echo.
)

REM Browser selection is handled automatically by the key-automation tool
REM (tools/mcd-key-automation/browser/session.py): it tries Playwright's bundled
REM Chromium first and transparently falls back to a system-installed Chrome
REM (preferred) or Edge when the Chromium download was blocked. No channel env
REM var is needed; set PLAYWRIGHT_BROWSER_CHANNEL only to force a specific one.

REM Start vima (Vima Chat is now embedded in-process at /chat)
echo Starting Mastercard Solution Studio on http://127.0.0.1:%VIMA_PORT%
if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    "%SCRIPT_DIR%.venv\Scripts\python.exe" app.py %APP_ARGS%
) else (
    %PYLAUNCHER% app.py %APP_ARGS%
)

:end
endlocal
