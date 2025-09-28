from flask import Flask
from app import create_app, db
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    # Set environment variables
    os.environ['FLASK_APP'] = 'run.py'
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = '1'
    os.environ['DATABASE_URL'] = 'sqlite:///app.db'
    os.environ['RAG_API_URL'] = 'http://localhost:8001'

    # Create the Flask application
    app = create_app()

    # Initialize database
    with app.app_context():
        try:
            # Import models to ensure they're known to SQLAlchemy
            from app.models import Complaint, Report, SimilarComplaint, SessionHistory
            
            # Drop all tables and recreate them
            print("Dropping all tables...")
            db.drop_all()
            print("Creating all tables...")
            db.create_all()
            print("Database initialized successfully!")
        except Exception as e:
            print(f"Error setting up database: {e}")
            db.session.rollback()
            raise

    if __name__ == '__main__':
        # Run the application
        print("Starting server...")
        print("You can access the application at:")
        print("* Local:   http://localhost:5000")
        print("* Network: http://0.0.0.0:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
except Exception as e:
    logger.error(f"Error starting server: {str(e)}", exc_info=True)
    raise
