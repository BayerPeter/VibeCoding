import uvicorn
from app.models import Base
from sqlalchemy import create_engine
import os

def init_database():
    """Initialize the database"""
    print("Initializing database...")
    engine = create_engine("sqlite:///app.db")
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

def main():
    # Set environment variables
    os.environ["DATABASE_URL"] = "sqlite:///app.db"
    os.environ["RAG_API_URL"] = "http://localhost:8000"

    # Initialize database
    init_database()

    # Start FastAPI server
    print("Starting FastAPI server...")
    uvicorn.run(
        "app:create_app",
        factory=True,
        reload=True,
        host="0.0.0.0",
        port=8080
    )

if __name__ == "__main__":
    main()
