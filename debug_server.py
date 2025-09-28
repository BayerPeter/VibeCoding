import uvicorn
import os
import logging
import sys
from app import create_app
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.models import Base
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def init_database():
    """Initialize the database"""
    try:
        logger.info("Initializing database...")
        engine = create_engine('sqlite:///app.db')
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully!")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise

def main():
    try:
        # Set environment variables
        os.environ['DATABASE_URL'] = 'sqlite:///app.db'
        os.environ['RAG_API_URL'] = 'http://localhost:8000'
        logger.info("Environment variables set")

        # Initialize database
        init_database()

        # Create app
        logger.info("Creating FastAPI application...")
        app = create_app()
        logger.info("FastAPI application created successfully")

        # Mount static files and templates
        STATIC_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "static"))
        TEMPLATES_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "templates"))

        logger.info(f"Static directory: {STATIC_DIR}")
        logger.info(f"Templates directory: {TEMPLATES_DIR}")

        # Ensure static directory exists
        os.makedirs(STATIC_DIR, exist_ok=True)
        logger.info("Static directory created/verified")

        # Create uploads directory
        os.makedirs("uploads", exist_ok=True)
        logger.info("Uploads directory created/verified")

        logger.info("Starting Uvicorn development server...")
        logger.info("You can access the application at:")
        logger.info("* Local:   http://localhost:8080")
        logger.info("* Network: http://0.0.0.0:8080")
        
        uvicorn.run("app:create_app", factory=True, host="0.0.0.0", port=8080, reload=True, log_level="debug")
    except Exception as e:
        logger.error(f"Application startup failed: {str(e)}", exc_info=True)
        raise

if __name__ == '__main__':
    main()
