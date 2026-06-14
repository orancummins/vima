@echo off

REM One-call usage:
REM
REM   Clean install (clones repo, provisions API keys, runs tests, cleans up):
REM     .\test.bat --clean --sso --email you@mastercard.com --smoke
REM     .\test.bat --clean --sso --email you@mastercard.com --full
REM     .\test.bat --clean --sso --email you@mastercard.com --storepass foobar!!
REM     .\test.bat --clean --portal-password secret --email you@mastercard.com
REM
REM   Existing install (uses this directory as-is, no portal login needed):
REM     .\test.bat --existing --smoke
REM     .\test.bat --existing --full
REM     .\test.bat --existing            (prompts for scope)
REM
REM   Clean-install flags (--email, --sso, --portal-password, --storepass,
REM   --key-password, --skip-provision, --nocleanup) are an error with --existing.

echo.
echo ============================================================
echo  Vima / Solution Studio - Test Suite
echo ============================================================
echo.

REM ── Parse CLI arguments ───────────────────────────────────────
set "EMAIL="
set "SSO="
set "PORTAL_PASSWORD="
set "INSTALL_TYPE="
set "KEY_PASSWORD="
set "TEST_SCOPE="
set "SKIP_PROVISION="
set "NO_SERVER="
set "NOCLEANUP="
set "_CLEAN_FLAGS="

:parse_args
if "%~1"=="" goto :args_done
if /i "%~1"=="--email"           ( set "EMAIL=%~2"           & set "_CLEAN_FLAGS=1" & shift /1 & shift /1 & goto :parse_args )
if /i "%~1"=="--sso"             ( set "SSO=Y"               & set "_CLEAN_FLAGS=1" & shift /1             & goto :parse_args )
if /i "%~1"=="--portal-password" ( set "PORTAL_PASSWORD=%~2" & set "_CLEAN_FLAGS=1" & shift /1 & shift /1 & goto :parse_args )
if /i "%~1"=="--clean"           ( set "INSTALL_TYPE=C"                             & shift /1             & goto :parse_args )
if /i "%~1"=="--existing"        ( set "INSTALL_TYPE=E"                             & shift /1             & goto :parse_args )
if /i "%~1"=="--key-password"    ( set "KEY_PASSWORD=%~2"    & set "_CLEAN_FLAGS=1" & shift /1 & shift /1 & goto :parse_args )
if /i "%~1"=="--storepass"       ( set "KEY_PASSWORD=%~2"    & set "_CLEAN_FLAGS=1" & shift /1 & shift /1 & goto :parse_args )
if /i "%~1"=="--smoke"           ( set "TEST_SCOPE=S"                               & shift /1             & goto :parse_args )
if /i "%~1"=="--full"            ( set "TEST_SCOPE=F"                               & shift /1             & goto :parse_args )
if /i "%~1"=="--skip-provision"  ( set "SKIP_PROVISION=1"    & set "_CLEAN_FLAGS=1" & shift /1             & goto :parse_args )
if /i "%~1"=="--no-server"       ( set "NO_SERVER=1"                                & shift /1             & goto :parse_args )
if /i "%~1"=="--nocleanup"       ( set "NOCLEANUP=1"         & set "_CLEAN_FLAGS=1" & shift /1             & goto :parse_args )
echo ERROR: Unknown flag: %~1
exit /b 1
:args_done
setlocal enabledelayedexpansion

REM ── Collect: install type (first, so we know which prompts to show) ───────
if /i "!INSTALL_TYPE!"=="C" goto :type_ok
if /i "!INSTALL_TYPE!"=="E" goto :type_ok
echo.
echo Install type:
echo   C - Clean     (clone repo into a temp dir, provision API keys, run tests)
echo   E - Existing  (use this directory as-is, no portal login needed)
echo.
:ask_type
set /p "INSTALL_TYPE=Choice [C/E]: "
if /i "!INSTALL_TYPE!"=="C" goto :type_ok
if /i "!INSTALL_TYPE!"=="E" goto :type_ok
echo   Please enter C or E.
goto :ask_type
:type_ok

REM ── Existing install: reject clean-only flags, then go straight to scope ──
if /i "!INSTALL_TYPE!"=="E" (
    if "!_CLEAN_FLAGS!"=="1" (
        echo.
        echo ERROR: The following flags are only valid with --clean:
        echo          --email, --sso, --portal-password, --storepass,
        echo          --key-password, --skip-provision, --nocleanup
        echo        For an existing install only --smoke and --full are accepted.
        exit /b 1
    )
    goto :collect_scope
)

REM ── Clean install: collect email, SSO, portal password, key password ──────

REM ── Collect: email ────────────────────────────────────────────
if not "!EMAIL!"=="" goto :email_ok
:ask_email
set /p "EMAIL=Mastercard Developers email: "
if "!EMAIL!"=="" ( echo   Email is required. & goto :ask_email )
:email_ok

REM ── Collect: SSO ──────────────────────────────────────────────
REM   SSO (Y)     = corporate/federated login; email is auto-filled in the
REM                 browser and the SSO redirect completes the login.
REM   Non-SSO (N) = standard login; email + password are pre-filled and
REM                 submitted automatically (MFA still requires human action).
if /i "!SSO!"=="Y" goto :sso_done
if /i "!SSO!"=="N" goto :sso_done
echo.
:ask_sso
set /p "SSO=Mastercard Developers SSO [Y/N]: "
if /i "!SSO!"=="Y" goto :sso_done
if /i "!SSO!"=="N" goto :sso_done
echo   Please enter Y or N.
goto :ask_sso
:sso_done

REM ── Collect: portal password (non-SSO only) ───────────────────
if /i "!SSO!"=="Y" goto :portal_pw_skip
if not "!PORTAL_PASSWORD!"=="" goto :portal_pw_skip
echo.
set /p "PORTAL_PASSWORD=Mastercard Developers password: "
:portal_pw_skip

REM ── Collect: key password ─────────────────────────────────────
REM NOTE: Default is foobar!! (^! is the batch escape for ! in delayed-expansion mode.)
if not "!KEY_PASSWORD!"=="" goto :key_pw_done
echo.
echo   NOTE: Default keystore password for provisioned .p12 certs is: foobar^!^!
set /p "KEY_PW_INPUT=Key password [default: foobar^!^!]: "
if not "!KEY_PW_INPUT!"=="" (
    set "KEY_PASSWORD=!KEY_PW_INPUT!"
) else (
    set "KEY_PASSWORD=foobar^!^!"
)
:key_pw_done

REM ── Collect: test scope ───────────────────────────────────────
:collect_scope
if /i "!TEST_SCOPE!"=="S" goto :scope_done
if /i "!TEST_SCOPE!"=="F" goto :scope_done
echo.
echo Test scope:
echo   S - Smoke  (connectivity + basic checks, fast)
echo   F - Full   (smoke + API + use case + bundles + SDKs)
echo.
:ask_scope
set /p "TEST_SCOPE=Choice [S/F, default S]: "
if "!TEST_SCOPE!"=="" set "TEST_SCOPE=S"
if /i "!TEST_SCOPE!"=="S" goto :scope_done
if /i "!TEST_SCOPE!"=="F" goto :scope_done
echo   Please enter S or F.
goto :ask_scope
:scope_done

echo.

REM ── Normalize WORK_DIR (%~dp0 always has a trailing \, which causes
REM    Windows to interpret the closing " as escaped when passed to Python)
set "WORK_DIR=%~dp0"
if "%WORK_DIR:~-1%"=="\" set "WORK_DIR=%WORK_DIR:~0,-1%"

REM ── Resolve Python ────────────────────────────────────────────
set "PYTHON="
if exist "!WORK_DIR!\.venv\Scripts\python.exe" (
    set "PYTHON=!WORK_DIR!\.venv\Scripts\python.exe"
) else (
    where py >nul 2>&1
    if not errorlevel 1 (
        set "PYTHON=py"
    ) else (
        where python >nul 2>&1
        if not errorlevel 1 set "PYTHON=python"
    )
)
if "!PYTHON!"=="" (
    echo ERROR: Python not found. Install Python 3.9+ and re-run.
    exit /b 1
)

REM ── Launch: existing install ──────────────────────────────────
if /i "!INSTALL_TYPE!"=="E" (
    set "_XARGS="
    if /i "!TEST_SCOPE!"=="F" set "_XARGS=!_XARGS! --full"
    if /i "!TEST_SCOPE!"=="S" set "_XARGS=!_XARGS! --smoke"
    if "!NO_SERVER!"=="1"     set "_XARGS=!_XARGS! --no-server"
    "!PYTHON!" "!WORK_DIR!\tests\run.py" --install-type E --work-dir "!WORK_DIR!" !_XARGS!
    exit /b %ERRORLEVEL%
)

REM ── Launch: clean install ─────────────────────────────────────
set "_XARGS="
if /i "!SSO!"=="Y"             set "_XARGS=!_XARGS! --sso"
if not "!PORTAL_PASSWORD!"=="" set "_XARGS=!_XARGS! --portal-password "!PORTAL_PASSWORD!""
if /i "!TEST_SCOPE!"=="F"      set "_XARGS=!_XARGS! --full"
if /i "!TEST_SCOPE!"=="S"      set "_XARGS=!_XARGS! --smoke"
if "!SKIP_PROVISION!"=="1"     set "_XARGS=!_XARGS! --skip-provision"
if "!NO_SERVER!"=="1"          set "_XARGS=!_XARGS! --no-server"
if "!NOCLEANUP!"=="1"          set "_XARGS=!_XARGS! --nocleanup"
"!PYTHON!" "!WORK_DIR!\tests\run.py" --email "!EMAIL!" --install-type C --key-password "!KEY_PASSWORD!" --work-dir "!WORK_DIR!" !_XARGS!

exit /b %ERRORLEVEL%
