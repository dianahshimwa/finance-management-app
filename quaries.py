#!/usr/bin/python3

def addExpense(mydb):
    name = input("Enter expense source: ")
    amount = input("Enter amount: ")
    try:
        amount = int(amount)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
        cursor = mydb.cursor()
        query = """INSERT INTO expenses (name, amount) VALUES (%s, %s)"""
        cursor.execute(query, (name, amount))
        mydb.commit()
        print("Expense recorded successfully.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
    except Exception as e:
        print(f"Error recording expense: {e}")
