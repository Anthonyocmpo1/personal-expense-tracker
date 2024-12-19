# config.py
from database import SessionLocal, init_db  # Import the session and database initialization

# Create the session instance
session = SessionLocal()

# Initialize the database
init_db()
