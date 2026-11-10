#this file is for calculations

import expense as ex
import incomes as incm

ex.expense
incm.incomes

def remaining_balance():
    total_income = sum(i['amount'] for i in incm.incomes)
    total_expense = sum(e['amount'] for e in ex.expense)
    Balance = total_income - total_expense

    return Balance
