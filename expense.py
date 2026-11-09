expense = []
incomes = []

def add_expense(name, amount):
    expense.append({"name": name, "amount": amount})
    print(f"Expense '{name}' of amount ₹{amount} added successfully.")

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

def add_income(name, amount):
    incomes.append({"name": name, "amount": amount})
    print(f"Income '{name}' of amount ₹'{amount}' added successfully.")
def view_income():
    if not incomes:
        print("No Incomes recorded.")
    else: 
        print("Incomes:")
        for i in incomes:
            print(f"Name: {i['name']}, Amount: ₹{i['amount']}")
