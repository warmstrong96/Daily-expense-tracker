import csv
import math
from collections import defaultdict
from datetime import date
from pathlib import Path


CSV_FILE = Path(__file__).with_name("expenses.csv")
CSV_FIELDS = ("amount", "description", "category", "date")


def load_expenses():
    if not CSV_FILE.exists():
        return []

    expenses = []
    try:
        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != list(CSV_FIELDS):
                raise ValueError("The CSV file has an unexpected format.")

            for row_number, row in enumerate(reader, start=2):
                amount = float(row["amount"])
                if not math.isfinite(amount) or amount <= 0:
                    raise ValueError(f"Invalid amount on CSV row {row_number}.")
                date.fromisoformat(row["date"])
                if not row["description"].strip() or not row["category"].strip():
                    raise ValueError(f"Missing description or category on CSV row {row_number}.")
                expenses.append({
                    "amount": amount,
                    "description": row["description"].strip(),
                    "category": row["category"].strip(),
                    "date": row["date"],
                })
    except (OSError, csv.Error, TypeError, ValueError) as error:
        print(f"Could not load {CSV_FILE.name}: {error}")
        return []

    return expenses


def save_expenses(expenses):
    try:
        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(expenses)
    except (OSError, csv.Error) as error:
        print(f"Could not save expenses: {error}")
        return False
    return True


def prompt_nonempty(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("This field cannot be empty.")


def prompt_amount():
    while True:
        raw_amount = input("Amount: ").strip()
        try:
            amount = float(raw_amount)
            if not math.isfinite(amount) or amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Enter a valid amount greater than zero.")


def prompt_date():
    while True:
        raw_date = input("Date (YYYY-MM-DD, blank for today): ").strip()
        if not raw_date:
            return date.today().isoformat()
        try:
            return date.fromisoformat(raw_date).isoformat()
        except ValueError:
            print("Enter a real date in YYYY-MM-DD format.")


def add_expense(expenses):
    expense = {
        "amount": prompt_amount(),
        "description": prompt_nonempty("Description: "),
        "category": prompt_nonempty("Category: "),
        "date": prompt_date(),
    }
    expenses.append(expense)
    if save_expenses(expenses):
        print("Expense added and saved.")
    else:
        expenses.pop()
        print("Expense was not added because it could not be saved.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nYour expenses:")
    for index, expense in enumerate(expenses, 1):
        print(
            f"{index}. {expense['date']} | {expense['category']} | "
            f"{expense['description']} | ${expense['amount']:.2f}"
        )


def show_report(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(expense["amount"] for expense in expenses)
    average = total / len(expenses)
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense["category"]] += expense["amount"]

    print("\nExpense summary:")
    print(f"Entries: {len(expenses)}")
    print(f"Total: ${total:.2f}")
    print(f"Average: ${average:.2f}")
    print("Totals by category:")
    for category, amount in sorted(category_totals.items()):
        print(f"  {category}: ${amount:.2f}")


def main():
    expenses = load_expenses()
    print("Welcome to the Daily Expense Tracker!")
    print(f"Loaded {len(expenses)} expense(s) from {CSV_FILE.name}.")

    while True:
        print("""
Menu:
1. Add a new expense
2. View all expenses
3. Show summary and category totals
4. Clear all expenses
5. Exit""")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_report(expenses)
        elif choice == "4":
            if not expenses:
                print("There are no expenses to clear.")
            elif input("Delete all saved expenses? (y/N): ").strip().lower() == "y":
                if save_expenses([]):
                    expenses.clear()
                    print("All expenses cleared.")
            else:
                print("Clear cancelled.")
        elif choice == "5":
            print("Exiting the Daily Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\nInput ended. Exiting the Daily Expense Tracker.")
