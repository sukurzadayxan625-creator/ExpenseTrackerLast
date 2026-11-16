import csv
from expense import getAllExpenses

def totalExpenses():
    expenses = getAllExpenses()

    total = 0

    for e in expenses:
        total += e["amount"]

        return total