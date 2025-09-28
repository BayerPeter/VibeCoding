from flask.cli import FlaskGroup
from app import create_app, db
import os

cli = FlaskGroup(create_app=create_app)

@cli.command('db_init')
def db_init():
    """Initialize the database with migrations"""
    try:
        # Remove existing database
        if os.path.exists('app.db'):
            os.remove('app.db')
            print("Removed existing database.")

        # Remove existing migrations
        if os.path.exists('migrations'):
            import shutil
            shutil.rmtree('migrations')
            print("Removed existing migrations.")

        # Initialize migrations
        os.system('flask db init')
        print("Initialized migrations directory.")

        # Create initial migration
        os.system('flask db migrate -m "Initial database setup"')
        print("Created initial migration.")

        # Apply migrations
        os.system('flask db upgrade')
        print("Applied migrations successfully.")

    except Exception as e:
        print(f"Error during database initialization: {e}")
        raise

if __name__ == '__main__':
    cli()
