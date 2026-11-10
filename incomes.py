incomes = []

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
    total_income = sum(i['amount'] for i in incomes)
    print(f"Total Income: ₹{total_income:.2f}")
def delete_income(name):
    for i in incomes:
        if i['name'] == name:
            amount = i['amount']
            incomes.remove(i)
            print(f"Income {name} of amount ₹{amount} deleted successfully.")
            print("Remaining Incomes: ")
            for i in incomes:
                print(f"Name: {i['name']}, Amount:{i['amount']}")
            return
    print(f"Income '{name}' not found.") 
