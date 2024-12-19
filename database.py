from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL (adjust this as per your actual DB setup)
DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL

# Create an engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session maker for interacting with the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base object which will be used to define models
Base = declarative_base()

# Create all tables in the database
def init_db():
    Base.metadata.create_all(bind=engine)

# Create a new session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
