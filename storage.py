import json

DATA_FILE = "DATA/expenses.json"

def loadExpenses():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            expenses = json.load(file)

            return expenses

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError("JSON file is corrupted.")

    def saveExpenses(expenses):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, ensure_ascii=False)