# expense_tracker.py

expenses = []

def print_line(char='-', length=40):
    print(char * length)

def input_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def add_expense():
    print_line()
    print("Add New Expense")
    print_line()
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category (e.g., Food, Travel): ")
    amount = input_float("Amount: ")
    if amount is None:
        return
    description = input("Description: ")

    expenses.append({
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    })

    print("Expense added successfully!\n")

def view_expenses():
    print_line()
    print("All Expenses")
    print_line()
    if not expenses:
        print("No expenses recorded.\n")
        return
    for idx, e in enumerate(expenses, 1):
        print(f"{idx}. {e['date']} | {e['category']} | ${e['amount']:.2f} | {e['description']}")
    print()

def total_by_category():
    print_line()
    category = input("Enter category to get total: ")
    total = sum(e['amount'] for e in expenses if e['category'].lower() == category.lower())
    print(f"Total for '{category}': ${total:.2f}\n")

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
        print_line('=')
        print(" SIMPLE EXPENSE TRACKER ")
        print_line('=')
        print("1.  Add Expense")
        print("2.  View All Expenses")
        print("3.  Total by Category")
        print("4.  Delete Expense")
        print("5.  Exit")
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
            print("\nExiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()
