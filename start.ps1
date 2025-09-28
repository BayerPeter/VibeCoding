$pythonPath = "C:\Users\gmytp\AppData\Local\Programs\Python\Python312\python.exe"

Write-Host "Installing required packages..."
& $pythonPath -m pip install -r requirements.txt

Write-Host "Creating directories..."
New-Item -ItemType Directory -Force -Path "app\static"
New-Item -ItemType Directory -Force -Path "uploads"
New-Item -ItemType Directory -Force -Path "instance"

Write-Host "Starting server..."
Write-Host "Server will be available at http://localhost:8080"
& $pythonPath -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
