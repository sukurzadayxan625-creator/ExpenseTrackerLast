import uuid
from datetime import date
from storage import saveExpenses, loadExpenses
from validation import *
from expections import expensesNotFound

def addExpense(title, amount, category):
    expenses = loadExpenses()

    expense = {
        "id": str(uuid.uuid4())[:8],
        "title": validateTitle(title),
        "amount": validateAmout(amount),
        "category": validateCategory(category),
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    saveExpenses(expenses)

    return expense

def getAllExpenses():
    return loadExpenses()


def searchExpenses(expenseID):
    expenses = loadExpenses()
    for e in expenses:
        if e["id"] == expenseID:
            return e
        expensesNotFound()

def updateExpense(title, amount, category, expenseID):
    expenses = loadExpenses()

    for e in expenses:
        if e["id"] == expenseID:
            e["title"] = validateTitle(title)
            e["amount"] = validateAmout(amount)
            e["category"] = validateCategory(category)
            e["date"] = date.today().isoformat()
            saveExpenses(expenses)

            return e
        
    expensesNotFound()

def deleteExpense(expenseID):
    expenses = loadExpenses()

    for  e in enumerate(expenses):
        if e["id"] == expenseID:
            del expenses[i]
            saveExpenses(expenses)
            return e

    expensesNotFound()