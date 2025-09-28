@echo off
"C:\Users\gmytp\AppData\Local\Programs\Python\Python312\python.exe" -m uvicorn debug_server:app --host 0.0.0.0 --port 8080 --reload --log-level debug
pause
