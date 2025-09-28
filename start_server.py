import os
import subprocess
import sys
from sqlalchemy import create_engine
from app.models import Base
from app.main import DATABASE_URL

def init_database():
    """Initialize the database"""
    print("Initializing database...")
    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

def main():
    # Get the Python executable path
    python_path = sys.executable
    print(f"Using Python from: {python_path}")

    # Create necessary directories
    dirs = ['app/static', 'uploads', 'instance']
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created directory: {d}")

    # Install requirements
    print("Installing requirements...")
    subprocess.run([python_path, "-m", "pip", "install", "-r", "requirements.txt"])

    # Initialize database
    init_database()

    # Start the server
    print("\nStarting server...")
    print("Server will be available at http://localhost:8080")
    subprocess.run([
        python_path, "-m", "uvicorn",
        "app:create_app",
        "--factory",
        "--reload",
        "--host", "0.0.0.0",
        "--port", "8080"
    ])

if __name__ == "__main__":
    main()
