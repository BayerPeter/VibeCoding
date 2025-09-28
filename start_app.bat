@echo off
setlocal enabledelayedexpansion

REM Switch to cmd.exe
cmd.exe /c "

REM Set Python path
set PYTHON_PATH=C:\Users\gmytp\AppData\Local\Programs\Python\Python312\python.exe

echo Checking Python installation...
if not exist %PYTHON_PATH% (
    echo Python not found at %PYTHON_PATH%
    echo Please ensure Python is installed
    pause
    exit /b 1
)

echo Creating directories...
mkdir "app\static" 2>nul
mkdir "uploads" 2>nul
mkdir "instance" 2>nul

echo Installing packages...
call %PYTHON_PATH% -m pip install --disable-pip-version-check -r requirements.txt
if !ERRORLEVEL! NEQ 0 (
    echo Failed to install packages
    pause
    exit /b 1
)

echo Creating database...
call %PYTHON_PATH% -c "from app.models import Base; from sqlalchemy import create_engine; import os; engine = create_engine(f'sqlite:///{os.path.abspath(\"app.db\")}'); Base.metadata.create_all(bind=engine)"
if !ERRORLEVEL! NEQ 0 (
    echo Failed to create database
    pause
    exit /b 1
)

echo Starting server...
echo Server will be available at http://localhost:8080
echo Press Ctrl+C to stop the server
call %PYTHON_PATH% -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

if !ERRORLEVEL! NEQ 0 (
    echo Failed to start server
    echo Check if port 8080 is available
    pause
    exit /b 1
)

"
pause
