@echo off
:: addapi.bat - Provision a Mastercard API from its documentation URL.
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
::   1. Sets up the mcd-key-automation venv (first run only). Installs only
::      Python dependencies via `python -m pip install -r requirements.txt`
::      so NO pip-generated console_script .exe shims are created.
::   2. Runs `python -m app.main provision-api <url>` from the tool dir -
::      creates the portal project, downloads keys, writes credentials to
::      config\.env.generated, smoke-tests the API.
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
set TOOL_PY=%TOOL_VENV%\Scripts\python.exe

:: We never invoke pip-generated console_script .exe shims. All CLI work
:: goes through `python -m`.

:: ── Parse arguments ──────────────────────────────────────────────────────────
set HEADFUL=
set INIT_SESSION=
set RECORD=
set URL=

:parse_args
if "%~1"=="" goto :args_done
if /i "%~1"=="--headful"      ( set "HEADFUL=--headful" & shift & goto :parse_args )
if /i "%~1"=="--init-session" ( set "INIT_SESSION=yes" & shift & goto :parse_args )
if /i "%~1"=="--record"       ( set "RECORD=yes"       & shift & goto :parse_args )
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
echo Usage: addapi.bat [--headful] [--init-session] [--record] ^<MASTERCARD_DOCS_URL^> >&2
exit /b 1

:args_done

:: ── Ensure tool venv exists ──────────────────────────────────────────────────
if not exist "%TOOL_PY%" (
    echo.
    echo Setting up API key automation tool ^(first run only^)...
    echo   [1/3] Creating virtual environment...
    if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
        "%SCRIPT_DIR%.venv\Scripts\python.exe" -m venv "%TOOL_VENV%"
    ) else (
        py -m venv "%TOOL_VENV%"
    )
    echo   [2/3] Installing dependencies via python -m pip ^(no .exe shims^)...
    "%TOOL_PY%" -m pip install --use-feature=truststore -r "%TOOL_DIR%\requirements.txt" --quiet
    echo   [3/3] Installing Chromium browser via python -m playwright...
    "%TOOL_PY%" -m playwright install chromium
    echo.
    echo API key automation tool ready.
    echo.
)

:: Belt-and-braces: if a prior install left the console_script .exe shim
:: behind, remove it so the user can't accidentally launch it.
if exist "%TOOL_VENV%\Scripts\mcd-key-automation.exe" (
    del /q "%TOOL_VENV%\Scripts\mcd-key-automation.exe" >nul 2>&1
)

:: ── Init-session mode ────────────────────────────────────────────────────────
if "%INIT_SESSION%"=="yes" (
    echo Establishing portal session ^(browser will open for login + MFA^)...
    pushd "%TOOL_DIR%"
    "%TOOL_PY%" -m app.main init-session
    set _rc=!errorlevel!
    popd
    if not "!_rc!"=="0" goto :err
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

:: -- Record mode -------------------------------------------------------------
:: Derive portal slug from the docs URL: https://developer.mastercard.com/<slug>/...
:: for /f collapses consecutive delimiters (// after https:), so the slug lands
:: in token 3, not 4.
for /f "tokens=3 delims=/" %%S in ("%URL%") do set "SLUG=%%S"
if "%RECORD%"=="yes" (
    if "%SLUG%"=="" (
        echo Error: Could not extract API slug from URL: %URL% >&2
        exit /b 1
    )
    echo Recording portal create-project flow for slug=%SLUG%
    echo   A browser window will open. Drive the flow end-to-end ^(create project,
    echo   download key file^). When done, return here and press Enter.
    echo.
    pushd "%TOOL_DIR%"
    "%TOOL_PY%" -m app.main record-api --api-slug "%SLUG%" --start-url "https://developer.mastercard.com/create-project?services=%SLUG%"
    set _rc=!errorlevel!
    popd
    if not "!_rc!"=="0" goto :err
    echo.
    echo Playbook saved. Re-run 'addapi.bat %URL%' to replay it headlessly.
    goto :end
)

:: -- Run provision-api -------------------------------------------------------
echo Adding API from: %URL%
echo.
pushd "%TOOL_DIR%"
"%TOOL_PY%" -m app.main provision-api %HEADFUL% "%URL%"
set _rc=%errorlevel%
popd
if not "%_rc%"=="0" goto :err

echo.
echo Done. To activate the credentials:
echo   type config\.env.generated ^>^> config\.env
echo   run.bat  ^(restart the server^)
goto :end

:show_help
echo addapi.bat ^<MASTERCARD_DOCS_URL^> [--headful] [--init-session] [--record]
echo.
echo  --init-session   Cache your portal session ^(run once; enables headless mode^)
echo  --headful        Force browser window open ^(useful when session expired^)
echo  --record         Open headful browser; you drive the wizard once and the
echo                   selectors are saved to playbooks\mastercard\^<slug^>.json
echo                   so subsequent runs can replay it headlessly.
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
