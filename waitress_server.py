from waitress import serve
from app import create_app
import os

# Set environment variables
os.environ['FLASK_APP'] = 'run.py'
os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = '1'
os.environ['DATABASE_URL'] = 'sqlite:///app.db'
os.environ['RAG_API_URL'] = 'http://localhost:8000'

# Create and configure the app
app = create_app()

if __name__ == '__main__':
    print("Starting server with Waitress...")
    print("You can access the application at:")
    print("* Local:   http://localhost:8080")
    print("* Network: http://0.0.0.0:8080")
    serve(app, host='0.0.0.0', port=8080)
