@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
python "%SCRIPT_DIR%main.py"
if errorlevel 1 pause
endlocal
