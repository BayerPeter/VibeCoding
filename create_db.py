import sqlite3
import os

def create_tables():
    # Check if database exists
    db_exists = os.path.exists('app.db')
    
    # Connect to database (will create if doesn't exist)
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    if db_exists:
        print("Database exists, checking tables...")
    else:
        print("Creating new database...")

    # Connect to database
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    # Drop tables if they exist
    cursor.executescript('''
    DROP TABLE IF EXISTS alembic_version;
    DROP TABLE IF EXISTS session_history;
    DROP TABLE IF EXISTS similar_complaint;
    DROP TABLE IF EXISTS report;
    DROP TABLE IF EXISTS complaint;
    ''')
    
    print("Creating tables...")
    cursor.executescript('''
    -- Complaint table
    CREATE TABLE complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        image_path TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    -- Report table
    CREATE TABLE reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        complaint_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        product_info JSON,
        investigation_summary JSON,
        risk_classification VARCHAR(50),
        conclusion TEXT,
        capa_required BOOLEAN DEFAULT 0 NOT NULL,
        capa_actions JSON,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (complaint_id) REFERENCES complaints(id)
    );

    -- Similar Complaint table
    CREATE TABLE complaint_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        complaint_id INTEGER NOT NULL,
        modification_type VARCHAR(50),
        modification_data JSON,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (complaint_id) REFERENCES complaints(id)
    );

    -- Session History table
    CREATE TABLE session_history (
        id VARCHAR(36) PRIMARY KEY,
        original_text TEXT NOT NULL,
        current_analysis JSON NOT NULL,
        modification_history JSON,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    -- Alembic version table for Flask-Migrate
    CREATE TABLE alembic_version (
        version_num VARCHAR(32) NOT NULL,
        PRIMARY KEY (version_num)
    );
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully with all tables.")

if __name__ == '__main__':
    create_tables()
