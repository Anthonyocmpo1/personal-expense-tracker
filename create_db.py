from models import Base
from config import engine

# Create all tables
Base.metadata.create_all(engine)
print("Database and tables created successfully.")
