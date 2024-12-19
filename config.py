from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Only import Base here from models.py

# Database URL (adjust it to your actual database setup)
DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL

# Set up the engine to connect to the database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the session instance
session = SessionLocal()

# Create all tables in the database
Base.metadata.create_all(bind=engine)
