# Personal Expense Tracker
# Overview
- The Personal Expense Tracker is a Python-based application that helps users track and manage their personal finances. It allows users to organize their spending into categories, add individual expenses, and associate receipts with these expenses. The application uses SQLAlchemy ORM for database interaction and Alembic for managing database migrations. The project features a Command-Line Interface (CLI) that enables users to interact with the system and manage their financial data.
# Features

- Category Management: Create and manage categories (e.g., Food, Travel, Entertainment) to group expenses.
- Expense Management: Track individual expenses with descriptions, amounts, and categories.
- Receipt Tracking: Attach receipts to specific expenses to maintain documentation for financial records.
- CLI Interface: A simple and intuitive command-line interface for interacting with the system.
- Database Migrations: Use Alembic to manage and apply database migrations for schema changes.
# Technologies Used
- Python 3: Programming language.
- SQLAlchemy: ORM for database interaction.
- Alembic: Database migration tool for managing schema changes.
- SQLite: Lightweight database for storing data.
# Setup Instructions
###### Clone the Repository
- git clone git@github.com:Anthonyocmpo1/personal-expense-tracker.git
- cd personal-expense-tracker
##### Set up the environment as mentioned in the previous instructions:
Create a virtual environment.
Install dependencies from requirements.txt.
Set up the database using Alembic and SQLAlchemy migrations.
#### Install Dependencies
Install the required Python packages listed in requirements.txt.
pip install -r requirements.txt
### Set Up the Database
- 1.Create the Database:
# python create_db.py
- 2.Run Alembic Migrations:
# alembic init alembic

# How to Use the CLI
- python main.py
# menu of options.
- 1 View Categories
- 2: Add Category
- 3: View Expenses
- 4: Add Expense
- 5: Update Expense
- 6: Delete Expense
- 7: View Expenses by Category
- 8: View Receipts
- 9: Add Receipt
- 10: View Receipts by Expense
- 11: Exit
# Code Structure
# models.py


Category: Represents categories for expenses.
Expense: Represents individual expenses.
Receipt: Represents receipts linked to expenses.
# database.py
Handles database configuration and session management using SQLAlchemy.

# main.py
Provides the logic for the command-line interface and handles user input, calling functions from the models and database.

# alembic
Contains Alembic migration files to track and apply schema changes to the database.

# Database Schema


# ategory Table: Stores category information.

- id: Primary key.
- name: Name of the category (e.g., Food, Transport).

# Expense Table: Stores expense information.
- id: Primary key.
- description: Description of the expense (e.g., Lunch).
- amount: Amount spent.
- category_id: Foreign key referencing the Category table.
- created_at: Timestamp of when the expense was added.

# Receipt Table: Stores receipt information.
- id: Primary key.
- receipt_number: Unique receipt identifier.
- expense_id: Foreign key referencing the Expense table.
- notes: Optional notes associated with the receipt.
- date: Date the receipt was created.

# Author
This project was created by Anthony Mwaura.
- Email:mwauraa634@gmail.com

# License
This project is licensed under the MIT License. See the LICENSE file for more details
