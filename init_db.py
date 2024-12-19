from config import engine, Base
from models import Category, Expense, Receipt

# Drop all existing tables
Base.metadata.drop_all(engine)

# Recreate all tables based on the models
Base.metadata.create_all(engine)

print("Database schema updated successfully!")
