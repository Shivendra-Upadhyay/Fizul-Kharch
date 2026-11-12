#this file is for calculations

import expense as ex
import incomes as incm

ex.expense
incm.incomes

def total_income():
    total_income = sum(i['amount'] for i in incm.incomes)
    return total_income

def total_expense():
    total_expense = sum(e['amount'] for e in ex.expense)
    return total_expense

def average_expense():
    if not ex.expense:
        print("No expense found")
        return 0
    total = total_expense()
    count = len(ex.expense)
    average = total / count
    return average

def average_income():
    if not incm.incomes:
        print("No incomes found")
        return 0
    total = total_income()
    count = len(incm.incomes)
    average = total / count
    return average
