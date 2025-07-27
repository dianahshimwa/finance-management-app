def setBudget(mydb):
    category = input("Enter budget category (e.g. food, transport): ")
    amount = input("Enter budget amount: ")
    try:
        amount = int(amount)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
        cursor = mydb.cursor()
        query = """INSERT INTO budgets (category, amount) VALUES (%s, %s)"""
        cursor.execute(query, (category, amount))
        mydb.commit()
        print("Budget set successfully.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
    except Exception as e:
        print(f"Error setting budget: {e}")
