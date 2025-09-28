@echo off
set FLASK_APP=run.py
set FLASK_ENV=development
set FLASK_DEBUG=1
set DATABASE_URL=sqlite:///app.db
set RAG_API_URL=http://localhost:8000
"C:\Users\gmytp\AppData\Local\Programs\Python\Python312\python.exe" -m flask run --host=0.0.0.0 --port=8080
pause
