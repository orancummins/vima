@echo off
REM ============================================================================
REM  ofin - Open Finance CLI launcher / builder  (Windows)
REM ----------------------------------------------------------------------------
REM  Usage:
REM    ofin.bat                Run the CLI from this repo (dev mode). With no
REM                            extra args it prints the ofin welcome screen.
REM    ofin.bat <args...>      Run an ofin command, e.g.  ofin.bat us auth token
REM    ofin.bat build          Build a self-contained bundle in cli\dist\ that
REM                            you can copy and run on any machine with Python.
REM    ofin.bat help           Show this help.
REM
REM  Requirements: Python 3.9+ with 'requests' and 'cryptography' installed
REM                (pip install requests cryptography)
REM ============================================================================
setlocal
set "REPO_DIR=%~dp0"
set "CLI_DIR=%REPO_DIR%cli"

if /I "%~1"=="help"   goto :usage
if /I "%~1"=="--help" goto :usage
if /I "%~1"=="/?"     goto :usage

if /I "%~1"=="build" (
    echo Building self-contained bundle into cli\dist\ ...
    python "%CLI_DIR%\build.py"
    echo.
    echo Done. The bundle in cli\dist\ is portable - copy it anywhere:
    echo     cli\dist\ofin.cmd config show
    echo     python cli\dist\ofin.pyz --env-file cli\dist\ofin.env us auth token
    echo.
    echo Build outputs ^(cli\dist\^) are gitignored.
    goto :eof
)

REM Default: run the CLI from the repo (dev mode). Pass all args straight through.
set "PYTHONPATH=%CLI_DIR%;%PYTHONPATH%"
python -m ofin %*
goto :eof

:usage
echo ofin - Open Finance CLI launcher ^(Windows^)
echo.
echo   ofin.bat               Run the CLI ^(dev mode^); no args shows the welcome screen
echo   ofin.bat ^<args...^>     Run a command, e.g.  ofin.bat us auth token
echo   ofin.bat build         Build a portable bundle in cli\dist\ ^(run anywhere^)
echo   ofin.bat help          Show this help
echo.
echo Requirements: Python 3.9+ with 'requests' and 'cryptography'.
echo Config is auto-discovered from config\.env; see cli\README.md for details.
goto :eof
