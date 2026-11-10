import expense as ex
import incomes as incm
import calculations as calc
print("Imported files: ", ex.__file__,", ",incm.__file__)
print("Available functions:", dir(ex),"\n", dir(incm))
print("")


while True:
    try:
        print("1. Add Income/Expense")
        print("2. Delete Income/expense")
        print("3. View Income/expense") 
        print("4. Financial Sumary")
        print("5. Exit")
        choice1 = int(input("Select a function: "))

        if choice1 == 1:
            while True:
                print("1. Add income: ")
                print("2. Add expense: ")
                print("3. Go back")
                choice2 = int(input("Select a function and enter its number: "))
                if choice2 == 1:
                    name = input("Enter the name of the income to add: ")
                    amount = float(input("Enter the amount: "))
                    incm.add_income(name, amount)
                elif choice2 == 2:
                    name = input("Enter the name of the expense to add: ")
                    amount = float(input("Enter the amount: "))
                    ex.add_expense(name, amount)
                elif choice2 == 3:
                    print("Returning to Home.")
                    break
                else: 
                    print("Select a valid function.")
        elif choice1 == 2:
            while True: 
                print("1. Delete Income: ")
                print("2. Delete Expense: ")
                print("3 Go Back")
                choice2 =  int(input("Select a function and enter its number: "))
                if choice2 == 1:
                    name = input("Enter the name of the income to delete: ")
                    incm.delete_income(name)
                elif choice2 == 2:
                    name = input("Enter the name of the expense to delete: ")
                    ex.delete_expense(name)
                elif choice2 == 3:
                    print("Returning to Home.")
                    break
                else: 
                    print("Select a valid function.")
        elif choice1 == 3:
            while True:
                print("1. View Income")
                print("2. View Expense")
                print("3. Go Back")
                choice2 = int(input("Select a function and enter its number: "))
                if choice2 == 1:
                    incm.view_income()
                elif choice2 == 2:
                    ex.view_expense()
                elif choice2 == 3:
                    print("Returning to Home")
                    break
                else: 
                    print("Select a valid function.")
        elif choice1 == 4:
            while True:
                print("1. View Balance")
                print("2. Average Expense")
                print("3. Go Back")
                choice2 = int(input("Select a function and enter its number: "))
                if choice2 == 1:
                    total_income = calc.total_income()
                    total_expense = calc.total_expense()
                    Balance = total_income - total_expense
                    print("--------Financial Summary-------")
                    print(f"Total Income: {total_income: .2f}")
                    print(f"Total Expense: {total_expense: .2f}")
                    print(f"Remaining Balance: {Balance: .2f}")
                elif choice2 == 2:
                    avg_exp = calc.average_expense()
                    print(f"Average Expense: {avg_exp: .4f}")
                elif choice2 == 3:
                    print("Returning to Home")
                    break
                else: 
                    print("Select a valid function.")
        elif choice1 == 5:
            print("Exiting the Application.")
            break
        else:
            print("Select a valid function.")
    except ValueError:
        print("Enter in a valid format.")
            

#testing git desktop and github connection
