@echo off
echo Starting FastAPI server...

:: Set environment variables
set DATABASE_URL=sqlite:///app.db
set RAG_API_URL=http://localhost:8000

:: Initialize database
python -c "from app.models import Base; from sqlalchemy import create_engine; engine = create_engine('sqlite:///app.db'); Base.metadata.create_all(bind=engine)"

:: Start the FastAPI server
python -m uvicorn app:create_app --factory --reload --host 0.0.0.0 --port 8080
pause
