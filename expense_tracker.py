# expense_tracker.py

expenses = []

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    description = input("Enter description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded.\n")
        return

    for idx, e in enumerate(expenses, start=1):
        print(f"{idx}. {e['date']} | {e['category']} | ${e['amount']:.2f} | {e['description']}")
    print()

def total_by_category():
    category = input("\nEnter category to get total: ")
    total = sum(e['amount'] for e in expenses if e['category'].lower() == category.lower())
    print(f"Total expenses for '{category}': ${total:.2f}\n")

def delete_expense():
    view_expenses()
    try:
        idx = int(input("Enter entry number to delete: "))
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            print(f"Deleted: {removed['description']} - ${removed['amount']:.2f}\n")
        else:
            print("Invalid entry number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def menu():
    while True:
        print("==== Simple Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total by Category")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()
