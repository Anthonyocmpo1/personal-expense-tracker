from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base  # Import Base from the new database.py

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    expenses = relationship("Expense", back_populates="category")

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, default=datetime.utcnow)  # Added created_at field to store the date of creation

    category = relationship("Category", back_populates="expenses")

class Receipt(Base):
    __tablename__ = 'receipts'

    id = Column(Integer, primary_key=True, index=True)
    receipt_number = Column(String, index=True)
    expense_id = Column(Integer, ForeignKey('expenses.id'))
    notes = Column(String)
    date = Column(String)

    expense = relationship("Expense")
