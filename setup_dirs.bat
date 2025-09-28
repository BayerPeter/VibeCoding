@echo off
echo Creating static directories...

mkdir "app\static" 2>nul
mkdir "app\static\css" 2>nul
mkdir "app\static\js" 2>nul
mkdir "uploads" 2>nul
mkdir "instance" 2>nul

echo Moving static files...
copy "app\static\css\styles.css" "app\static\css\styles.css" >nul 2>&1
copy "app\static\js\main.js" "app\static\js\main.js" >nul 2>&1

echo Done. Starting server...
.\run_new.bat
