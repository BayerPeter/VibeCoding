import uvicorn
from app.main import app
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Get port from environment variable or use default
    port = int(os.getenv("PORT", 8000))
    
    # Get host from environment variable or use default
    host = os.getenv("HOST", "127.0.0.1")
    
    # Run the FastAPI application
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=True,  # Enable auto-reload during development
        workers=1     # Single worker for development
    )
