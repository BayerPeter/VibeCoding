@echo off
setlocal enabledelayedexpansion

set PYTHON_CMD="C:\Users\gmytp\AppData\Local\Programs\Python\Python312\python.exe"

echo Checking Python installation...
if not exist %PYTHON_CMD% (
    echo Python is not found at %PYTHON_CMD%
    echo Please ensure Python is installed
    pause
    exit /b 1
)

echo Creating necessary directories...
if not exist "app\static" mkdir "app\static"
if not exist "uploads" mkdir "uploads"
if not exist "instance" mkdir "instance"

echo Installing required packages...
%PYTHON_CMD% -m pip install -r requirements.txt
if !ERRORLEVEL! NEQ 0 (
    echo Failed to install required packages
    pause
    exit /b 1
)

echo Initializing database...
%PYTHON_CMD% -c "from app.models import Base; from sqlalchemy import create_engine; import os; engine = create_engine(f'sqlite:///{os.path.abspath(\"app.db\")}'); Base.metadata.create_all(bind=engine)"
if !ERRORLEVEL! NEQ 0 (
    echo Failed to initialize database
    pause
    exit /b 1
)

echo Starting the server...
echo Server will be available at http://localhost:8080
echo Press Ctrl+C to stop the server
%PYTHON_CMD% -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
if !ERRORLEVEL! NEQ 0 (
    echo Failed to start the server
    echo Please check if port 8080 is available
    pause
    exit /b 1
)

pause
