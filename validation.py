from expections import *

Caterogies = [
    "Food",
    "Shopping",
    "Entertainment",
    "Health",
    "Entertainment",
    "other"
]
def validateTitle(title):
    title = title.strip()

    if not title:
        invalidExpense("Title cannot be empty.")

        return title



def validateAmout(amout):
    try:
        amout = float(amout)
    except ValueError:
        invalidExpense("Amount must be a number.")
        if amout <= 0:
            invalidExpense("Amount must be greater than zero.")
    return amout
def validateCategory(category):
    if category not in Caterogies:
        invalidExpense("Invalid category.")
        
    return category