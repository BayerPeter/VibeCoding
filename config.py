import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Pagination Configuration
    COMPLAINTS_PER_PAGE = 10
    REPORTS_PER_PAGE = 10
    
    # Complaint System Configuration
    SIMILAR_COMPLAINTS_MONTHS = 24  # Number of months to look back for similar complaints
    
    # File Upload Configuration
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = os.path.join(basedir, 'app/static/uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}
    
    # Ensure upload directory exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # Flash message categories
    FLASH_CATEGORIES = ['success', 'info', 'warning', 'error']
    
    # Date format for display
    DATE_FORMAT = '%Y-%m-%d %H:%M'
    
    # Status configurations
    COMPLAINT_STATUSES = ['pending', 'in_review', 'completed']
    REPORT_STATUSES = ['draft', 'in_review', 'approved']
    
    # Risk classifications
    RISK_CLASSIFICATIONS = ['critical', 'major', 'minor', 'negligible']
