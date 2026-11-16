from expense import*
from validation import *
from report import *

def showMenu():
    print("= " * 40)
    print("\n\n Welcome to Expense Tracker\n\n")
    print("= " * 40)
    print()


    print("""
    1. Add Expense
    2. View All Expenses
    3. Edit Expenses
    4. Delete Expense
    5. Search Expense
    6. Total Expenses
    7. Show Category
    8. Export to CSV
    
    0. Exit
    """)
    print("= " * 40)

def main():
    while True:
        showMenu()
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                title = input("Enter expense title: ")
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")

                expense = addExpense(title, amount, category)
                print("Expense added successfully!")
                print("Expense ID:", expense["id"])

        except:
            print("Invalid input. Please try again.")

