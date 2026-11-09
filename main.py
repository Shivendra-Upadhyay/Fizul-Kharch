import expense as ex
print("Imported file: ", ex.__file__)
print("Available functions:", dir(ex))

#add expense
#name expense
#add amount

print("Welcome!, Please select a number to add an expense")
print("1. Add Expense")
print("2. Delete Expense")
print("3. View Expense")
print("4. Add Income")
print("5. View Income")
print("6. Delete Income")
print("7. Exit")

while True:
    choice = int(input("Enter your choice (1-7): "))
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
        ex.add_income(name, amount)
    elif choice == 5:
        ex.view_income()
    elif choice == 6:
        name = input("Enter the name of the income to delete: ")
        ex.delete_income(name)
    elif choice == 7:    
        print("Exiting the program. Goodbye!")
        break
    else: 
        print("Invalid choice. Please try again.")
#testing git desktop and github connection
