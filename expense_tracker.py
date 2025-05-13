import json
import os

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(amount, category):
    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category})
    save_expenses(expenses)
    print("Expense added!")

def show_expenses():
    expenses = load_expenses()
    total = sum(item["amount"] for item in expenses)
    print(f"\nAll expenses (Total: ₹{total}):")
    for exp in expenses:
        print(f"₹{exp['amount']} on {exp['category']}")

# Example
add_expense(250, "Food")
add_expense(150, "Books")
show_expenses()
