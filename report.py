import csv
from expense import getAllExpenses

def totalExpenses():
    expenses = getAllExpenses()

    total = 0

    for e in expenses:
        total += e["amount"]

        return total

    def exportToCSV():
        expenses = getAllExpenses()

        filePath = "data/expenses.csv"

        fieldNames = ["id", "title", "amount", "category", "date"]

        with open(filePath, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerows(expenses)

            return filePath