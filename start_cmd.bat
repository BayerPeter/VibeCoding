@echo off
cmd /k "C:\Users\gmytp\AppData\Local\Programs\Python\Python312\python.exe" -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
