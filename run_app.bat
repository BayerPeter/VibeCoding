@echo off
echo Starting FastAPI application...

:: Try to find Python in common locations
where python > nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_PATH=python
) else (
    where py > nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        set PYTHON_PATH=py
    ) else (
        echo Python not found in PATH
        exit /b 1
    )
)

echo Using Python: %PYTHON_PATH%

:: Install requirements if needed
%PYTHON_PATH% -m pip install -r requirements.txt

:: Run the application with debug output
%PYTHON_PATH% debug_server.py
pause
