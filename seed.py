from faker import Faker
from config import session
from models import Category, Expense, Receipt
import random

fake = Faker()

# Add Categories
categories = ["Food", "Transport", "Rent", "Entertainment", "Utilities", "Healthcare"]
for name in categories:
    category = Category(name=name)
    session.add(category)
session.commit()

# Add Expenses
for _ in range(20):
    expense = Expense(
        description=fake.sentence(nb_words=4),
        amount=round(random.uniform(10, 500), 2),
        category_id=random.randint(1, len(categories))
    )
    session.add(expense)
session.commit()

print("Sample data seeded successfully.")
