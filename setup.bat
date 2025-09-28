@echo off
cd /d %~dp0

echo Installing packages...
cmd /c ""C:\Users\gmytp\AppData\Local\Programs\Python\Python312\python.exe" -m pip install -r requirements.txt"

echo Starting server...
cmd /c ""C:\Users\gmytp\AppData\Local\Programs\Python\Python312\python.exe" -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8080 --log-level debug"

pause
