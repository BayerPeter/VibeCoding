import os
import pathlib
from app.models import Base
from sqlalchemy import create_engine

def init_app():
    """Initialize application directories and database"""
    # Create necessary directories
    app_dir = pathlib.Path(__file__).parent
    dirs_to_create = [
        app_dir / "app" / "static",
        app_dir / "uploads",
        app_dir / "instance"
    ]
    
    for dir_path in dirs_to_create:
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")

    # Initialize database
    db_path = app_dir / "app.db"
    database_url = f"sqlite:///{db_path}"
    engine = create_engine(database_url)
    Base.metadata.create_all(bind=engine)
    print(f"Initialized database at: {db_path}")

if __name__ == "__main__":
    init_app()
    print("\nStarting server...")
    os.system("python -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload")
