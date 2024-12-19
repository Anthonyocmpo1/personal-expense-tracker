import os
from config import session
from models import Category, Expense, Receipt, Base
from datetime import datetime

# Ensure tables are created before any interaction with the DB
Base.metadata.create_all(session.bind)

# ===================== CATEGORY FUNCTIONS =======================
# View all Categories
def view_categories():
    categories = session.query(Category).all()
    print("Available Categories:")
    for category in categories:
        print(f"ID: {category.id} | Name: {category.name}")

# Add a Category
def add_category():
    name = input("Enter the Category name: ")
    category = Category(name=name)
    session.add(category)
    session.commit()
    print("Category added successfully!")

# ===================== EXPENSE FUNCTIONS ========================
# View all Expenses
def view_expenses():
    expenses = session.query(Expense).all()
    print("Expenses List:")
    for expense in expenses:
        print(f"ID: {expense.id} | Description: {expense.description} | Amount: {expense.amount} | "
              f"Category: {expense.category.name if expense.category else 'None'} | Date: {expense.created_at}")

# Add an Expense
def add_expense():
    description = input("Enter expense description: ")
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    
    view_categories()
    category_id = int(input("Enter Category ID: "))

    # Check if the category exists
    category = session.query(Category).filter_by(id=category_id).first()
    if not category:
        print("Invalid Category ID.")
        return

    expense = Expense(description=description, amount=amount, category_id=category_id)
    session.add(expense)
    session.commit()
    print("Expense added successfully!")

# Update an Expense
def update_expense():
    view_expenses()
    expense_id = int(input("Enter the Expense ID to update: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()

    if not expense:
        print("Expense not found.")
        return

    description = input("Enter new description (or leave blank to keep the same): ")
    amount = input("Enter new amount (or leave blank to keep the same): ")

    if description:
        expense.description = description
    if amount:
        try:
            expense.amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return

    session.commit()
    print("Expense updated successfully!")

# Delete an Expense
def delete_expense():
    view_expenses()
    expense_id = int(input("Enter the Expense ID to delete: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()

    if not expense:
        print("Expense not found.")
        return

    session.delete(expense)
    session.commit()
    print("Expense deleted successfully!")

# View Expenses by Category
def view_expenses_by_category():
    view_categories()
    category_id = int(input("Enter Category ID to view expenses: "))
    expenses = session.query(Expense).filter_by(category_id=category_id).all()

    if expenses:
        print(f"Expenses in Category {category_id}:")
        for expense in expenses:
            print(f"ID: {expense.id} | Description: {expense.description} | Amount: {expense.amount} | Date: {expense.created_at}")
    else:
        print("No expenses found in this category.")

# ===================== RECEIPT FUNCTIONS ========================
# View all Receipts
def view_receipts():
    receipts = session.query(Receipt).all()
    for receipt in receipts:
        print(f"ID: {receipt.id} | Receipt No: {receipt.receipt_number} | Expense ID: {receipt.expense_id} | Date: {receipt.date} | Notes: {receipt.notes}")

# Add a Receipt
def add_receipt():
    view_expenses()  # Show all expenses first
    expense_id = int(input("Enter the Expense ID to associate with this receipt: "))
    receipt_number = input("Enter Receipt Number: ")
    notes = input("Enter any notes (optional): ")

    # Check if the Expense ID exists
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if not expense:
        print("Expense not found. Cannot add a receipt.")
        return

    receipt = Receipt(receipt_number=receipt_number, expense_id=expense_id, notes=notes, date=datetime.now())
    session.add(receipt)
    session.commit()
    print("Receipt added successfully!")

# View Receipts by Expense
def view_receipts_by_expense():
    view_expenses()  # Show all expenses first
    expense_id = int(input("Enter Expense ID to view its receipts: "))

    receipts = session.query(Receipt).filter_by(expense_id=expense_id).all()
    if receipts:
        print(f"Receipts for Expense ID {expense_id}:")
        for receipt in receipts:
            print(f"ID: {receipt.id} | Receipt No: {receipt.receipt_number} | Date: {receipt.date} | Notes: {receipt.notes}")
    else:
        print("No receipts found for this expense.")

# ===================== MAIN MENU ========================
def main():
    while True:
        # Clear terminal for different platforms
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix-like (Linux/macOS)
            os.system('clear')

        print("Expense Tracker CLI")
        print("1. View Categories")
        print("2. Add Category")
        print("3. View Expenses")
        print("4. Add Expense")
        print("5. Update Expense")
        print("6. Delete Expense")
        print("7. View Expenses by Category")
        print("8. View Receipts")
        print("9. Add Receipt")
        print("10. View Receipts by Expense")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_categories()
        elif choice == '2':
            add_category()
        elif choice == '3':
            view_expenses()
        elif choice == '4':
            add_expense()
        elif choice == '5':
            update_expense()
        elif choice == '6':
            delete_expense()
        elif choice == '7':
            view_expenses_by_category()
        elif choice == '8':
            view_receipts()
        elif choice == '9':
            add_receipt()
        elif choice == '10':
            view_receipts_by_expense()
        elif choice == '11':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
