expense = []

def add_expense(name, amount):
    expense.append({"name": name, "amount": amount})
    print(f"Expense '{name}' of amount ₹{amount} adexpded successfully.")

def delete_expense(name):
    for e in expense:
        if e["name"] == name:
            expense.remove(e)
            print(f"Expense '{name}' deleted successfully.")
            return

    print(f"Expense '{name}' not found.")

def view_expense():
    if not expense:
        print("No Expenses Recorded.")
    else:
        print("Expenses:")
        for e in expense:
            print(f"Name: {e['name']}, Amount: ₹{e['amount']}")
    total_expense = sum(i['amount'] for i in expense)
    print(f"Total Expense: ₹{total_expense: .2f}")

