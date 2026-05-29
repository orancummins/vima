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
    "%SCRIPT_DIR%.venv\Scripts\python.exe" -m pip install --use-feature=truststore -r requirements.txt --quiet
) else (
    py -m pip install --use-feature=truststore -r requirements.txt --quiet
)
if errorlevel 1 (
    echo ERROR: Failed to install Python dependencies. Aborting.
    goto :end
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
        py -m venv "%TOOL_VENV%"
    )
    if errorlevel 1 (
        echo ERROR: Failed to create tool virtual environment. Aborting.
        goto :end
    )
    echo   [2/4] Upgrading pip ^(required for truststore support^)...
    "%TOOL_PY%" -m pip install --upgrade pip --quiet
    if errorlevel 1 (
        echo ERROR: Failed to upgrade pip in tool venv. Aborting.
        goto :end
    )
    echo   [3/4] Installing dependencies via python -m pip ^(no .exe shims, this may take a minute^)...
    "%TOOL_PY%" -m pip install --use-feature=truststore -r "%TOOL_DIR%\requirements.txt"
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

REM If the chromium download was skipped, drive system Edge instead.
if exist "%TOOL_VENV%\.chromium-skipped" (
    set PLAYWRIGHT_BROWSER_CHANNEL=msedge
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
