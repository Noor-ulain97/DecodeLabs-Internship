import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Enter category (Food, Travel, Bills, Shopping, Other): ")
        date = datetime.now().strftime("%Y-%m-%d")

        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        save_data(expenses)

        print("Expense added successfully!")

    except ValueError:
        print("Invalid input! Please enter a number.")


def view_all(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n------ All Expenses ------")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} | {e['category']} | {e['amount']}")

    total = sum(e["amount"] for e in expenses)
    print("--------------------------")
    print("Total Spent:", total)


def category_summary(expenses):
    if not expenses:
        print("No data available.")
        return

    summary = {}

    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]

    print("\n------ Category Summary ------")
    for cat, amt in summary.items():
        print(f"{cat}: {amt}")

    print("------------------------------")


def monthly_summary(expenses):
    month = datetime.now().strftime("%Y-%m")

    monthly_total = 0

    for e in expenses:
        if e["date"].startswith(month):
            monthly_total += e["amount"]

    print(f"\nTotal spent in {month}: {monthly_total}")


def delete_last(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    removed = expenses.pop()
    save_data(expenses)

    print(f"Deleted last expense: {removed['category']} - {removed['amount']}")


def main():
    expenses = load_data()

    while True:
        print("\n===== ADVANCED EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Delete Last Expense")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_all(expenses)

        elif choice == "3":
            category_summary(expenses)

        elif choice == "4":
            monthly_summary(expenses)

        elif choice == "5":
            delete_last(expenses)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


main()