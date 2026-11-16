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
    