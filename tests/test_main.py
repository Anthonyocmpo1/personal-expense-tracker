import pytest
from main import add_category, add_expense, add_receipt  # Import functions from main.py
from models import Category, Expense, Receipt
from config import SessionLocal, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an in-memory SQLite engine for testing
TEST_DATABASE_URL = "sqlite:///:memory:"
TestEngine = create_engine(TEST_DATABASE_URL, echo=False)
TestSession = sessionmaker(bind=TestEngine)

@pytest.fixture
def setup_database():
    # Create tables in the in-memory test database
    Base.metadata.create_all(TestEngine)
    test_session = TestSession()
    
    # Override the global session with the test session
    global session
    session = test_session
    
    yield  # Run the test
    
    # Cleanup: Drop all tables and close the session
    Base.metadata.drop_all(TestEngine)
    test_session.close()

def test_create_category(setup_database):
    category = Category(name="Food")
    session.add(category)
    session.commit()
    
    assert category.id is not None
    assert category.name == "Food"

def test_create_expense(setup_database):
    category = Category(name="Transport")
    session.add(category)
    session.commit()
    
    expense = Expense(description="Taxi fare", amount=15.0, category_id=category.id)
    session.add(expense)
    session.commit()
    
    assert expense.id is not None
    assert expense.description == "Taxi fare"
    assert expense.amount == 15.0
    assert expense.category_id == category.id

def test_create_receipt(setup_database):
    category = Category(name="Bills")
    session.add(category)
    session.commit()
    
    expense = Expense(description="Electricity bill", amount=50.0, category_id=category.id)
    session.add(expense)
    session.commit()

    receipt = Receipt(receipt_number="R12345", expense_id=expense.id, notes="Paid on time")
    session.add(receipt)
    session.commit()
    
    assert receipt.id is not None
    assert receipt.receipt_number == "R12345"
    assert receipt.notes == "Paid on time"
    assert receipt.expense_id == expense.id
