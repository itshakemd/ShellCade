@echo off
REM Tetris launcher - keeps tetris.py in the same folder as this .bat file
setlocal
set "SCRIPT_DIR=%~dp0"

where python >nul 2>nul
if %errorlevel%==0 (
    python "%SCRIPT_DIR%tetris.py"
    goto :eof
)

where py >nul 2>nul
if %errorlevel%==0 (
    py "%SCRIPT_DIR%tetris.py"
    goto :eof
)

echo Python was not found on this system.
echo Please install Python from https://www.python.org/downloads/
echo and make sure "Add python.exe to PATH" is checked during install.
pause
endlocal