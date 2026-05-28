@echo off
:: addapi.bat — Provision a Mastercard API from its documentation URL.
::
:: Usage:
::   addapi.bat <MASTERCARD_DOCS_URL>
::   addapi.bat --headful <MASTERCARD_DOCS_URL>     force browser window
::   addapi.bat --init-session                      cache portal session
::
:: Example:
::   addapi.bat https://developer.mastercard.com/bin-lookup/documentation/
::
:: What it does:
::   1. Sets up the mcd-key-automation venv (first run only).
::   2. Runs provision-api <url> — creates portal project, downloads keys,
::      writes credentials to config\.env.generated, smoke-tests the API.
::   3. Prints instructions for merging credentials into config\.env.
::
:: Prerequisites:
::   - Add MCD_PORTAL_EMAIL and MCD_PORTAL_PASSWORD to config\.env first.
::   - Run addapi.bat --init-session once to cache your portal session so
::     subsequent calls run headless (no browser window).
setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0
set TOOL_DIR=%SCRIPT_DIR%tools\mcd-key-automation
set TOOL_VENV=%TOOL_DIR%\.venv
set MCD_CMD=%TOOL_VENV%\Scripts\mcd-key-automation.exe

:: ── Parse arguments ──────────────────────────────────────────────────────────
set HEADFUL=
set INIT_SESSION=
set URL=

:parse_args
if "%~1"=="" goto :args_done
if /i "%~1"=="--headful"      set HEADFUL=--headful & shift & goto :parse_args
if /i "%~1"=="--init-session" set INIT_SESSION=yes  & shift & goto :parse_args
if /i "%~1"=="--help"         goto :show_help
if /i "%~1"=="-h"             goto :show_help
:: Treat anything starting with http as the URL
set _arg=%~1
if /i "!_arg:~0,4!"=="http" (
    set URL=%~1
    shift
    goto :parse_args
)
echo Unknown argument: %~1 >&2
echo Usage: addapi.bat [--headful] [--init-session] ^<MASTERCARD_DOCS_URL^> >&2
exit /b 1

:args_done

:: ── Ensure tool venv exists ──────────────────────────────────────────────────
if not exist "%TOOL_VENV%\Scripts\python.exe" (
    echo.
    echo Setting up API key automation tool ^(first run only^)...
    echo   [1/3] Creating virtual environment...
    if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
        "%SCRIPT_DIR%.venv\Scripts\python.exe" -m venv "%TOOL_VENV%"
    ) else (
        py -m venv "%TOOL_VENV%"
    )
    echo   [2/3] Installing dependencies...
    "%TOOL_VENV%\Scripts\pip.exe" install --use-feature=truststore -e "%TOOL_DIR%" --quiet
    echo   [3/3] Installing Chromium browser...
    "%TOOL_VENV%\Scripts\playwright.exe" install chromium
    echo.
    echo API key automation tool ready.
    echo.
)

:: ── Init-session mode ────────────────────────────────────────────────────────
if "%INIT_SESSION%"=="yes" (
    echo Establishing portal session ^(browser will open for login + MFA^)...
    "%MCD_CMD%" init-session
    if errorlevel 1 goto :err
    echo.
    echo Session cached. Subsequent addapi.bat calls will run headless.
    goto :end
)

:: ── Require URL ──────────────────────────────────────────────────────────────
if "%URL%"=="" (
    echo Error: No Mastercard Developers URL provided. >&2
    echo. >&2
    echo Usage: addapi.bat ^<MASTERCARD_DOCS_URL^> >&2
    echo. >&2
    echo Examples: >&2
    echo   addapi.bat https://developer.mastercard.com/bin-lookup/documentation/ >&2
    echo   addapi.bat https://developer.mastercard.com/merchant-identifier/documentation/ >&2
    echo. >&2
    echo First time? Cache your portal session so subsequent calls are headless: >&2
    echo   addapi.bat --init-session >&2
    exit /b 1
)

:: ── Run provision-api ────────────────────────────────────────────────────────
echo Adding API from: %URL%
echo.
"%MCD_CMD%" provision-api %HEADFUL% "%URL%"
if errorlevel 1 goto :err

echo.
echo Done. To activate the credentials:
echo   type config\.env.generated ^>^> config\.env
echo   run.bat  ^(restart the server^)
goto :end

:show_help
echo addapi.bat ^<MASTERCARD_DOCS_URL^> [--headful] [--init-session]
echo.
echo  --init-session   Cache your portal session ^(run once; enables headless mode^)
echo  --headful        Force browser window open ^(useful when session expired^)
echo.
echo Example:
echo   addapi.bat https://developer.mastercard.com/bin-lookup/documentation/
goto :end

:err
echo.
echo addapi failed — check tools\mcd-key-automation\logs\execution.log for details. >&2
exit /b 1

:end
endlocal
