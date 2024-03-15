import json

def enter_transaction():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    transaction = {"category": category, "amount": amount}
    # Store the transaction in memory or save it to a file/database

def calculate_budget(income, expenses):
    remaining_budget = income - sum(expenses)
    return remaining_budget

def analyze_expenses(expenses):
    # Categorize expenses
    # Calculate spending trends
    # Display the spending trends to the user

 def save_transactions(transactions):
    with open("transactions.json", "w") as f:
        json.dump(transactions, f)

def load_transactions():
    try:
        with open("transactions.json", "r") as f:
            transactions = json.load(f)
            return transactions
    except FileNotFoundError:
        return []

# Main program loop
transactions = load_transactions()

while True:
    print("1. Enter Transaction")
    print("2. Calculate Budget")
    print("3. Analyze Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enter_transaction()
    elif choice == "2":
        income = float(input("Enter income: "))
        expenses = [transaction["amount"] for transaction in transactions]
        remaining_budget = calculate_budget(income, expenses)
        print("Remaining budget:", remaining_budget)
    elif choice == "3":
        expenses = [transaction["amount"] for transaction in transactions]
        analyze_expenses(expenses)
    elif choice == "4":
       save_transactions(transactions)
    else:
        print("Invalid choice. Please try again.")