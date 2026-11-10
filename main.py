import expense as ex
import incomes as incm
import calculations as calc
print("Imported files: ", ex.__file__,", ",incm.__file__)
print("Available functions:", dir(ex),"\n", dir(incm))
print("")
#add expense
#name expense
#add amount

while True:
    print("Welcome!, Please select a number to add an expense")
    print("1. Add Expense")
    print("2. Delete Expense")  
    print("3. View Expense")
    print("4. Add Income")
    print("5. View Income")
    print("6. Delete Income")
    print("7. Balance")
    print("8. Exit")
    try:
        choice = int(input("Enter your choice (1-8): "))
        if choice == 1:
            name = input("Enter the name of the expense: ")
            amount = float(input("Enter the amount of the expense:"))
            ex.add_expense(name, amount)
        elif choice == 2:
            name = input("Enter the name of the expense to delete: ")
            ex.delete_expense(name)
        elif choice == 3:
            ex.view_expense()
        elif choice == 4:
            name = input("Enter the name of the income: ")
            amount = float(input("Enter the amount of the income:"))
            incm.add_income(name, amount)
        elif choice == 5:
            incm.view_income()
        elif choice == 6:
            name = input("Enter the name of the income to delete: ")
            incm.delete_income(name)
        elif choice == 7:
            Balance = calc.remaining_balance()
            print(f"Remaining Balance:₹{Balance: .2f}")
        elif choice == 8:    
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Select a valid function and enter a number only b/w 1 and 8.")
    except ValueError:
        print("Select in valid format")
#testing git desktop and github connection
