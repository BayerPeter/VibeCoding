from sqlalchemy import create_engine
import os
from app.models import Base

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{os.path.abspath('app.db')}")
engine = create_engine(DATABASE_URL)

def init_db():
    """Initialize the database by creating all tables"""
    try:
        # Drop all tables first to ensure a clean slate
        Base.metadata.drop_all(bind=engine)
        print("Dropped existing tables.")

        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("Created all tables successfully.")
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        raise

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Database initialization completed.")
