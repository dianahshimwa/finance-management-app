def createTables(mydb):
    cursor = mydb.cursor()
    # Create the necessary tables for the personal finance application
    
    # income table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS income (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            amount INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )

    # expenses table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS expenses (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            amount INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )

    # budgets table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS budgets (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            category VARCHAR(100),
            amount INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )

    # savings goals table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS savings_goals (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            goal_name VARCHAR(100),
            target_amount INT,
            target_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )

    mydb.commit()
    cursor.close()


def addIncome(mydb):
    name = input("Enter income source: ")
    amount = input("Enter amount: ")
    try:
        amount = int(amount)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
        cursor = mydb.cursor()
        query = """INSERT INTO income (name, amount) VALUES (%s, %s)"""
        cursor.execute(query, (name, amount))
        mydb.commit()
        print("Income recorded successfully.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
    except Exception as e:
        print(f"Error recording income: {e}")



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


def setSavingsGoal(mydb):
    goal_name = input("Enter savings goal name: ")
    target_amount = input("Enter target amount: ")
    target_date = input("Enter target date (YYYY-MM-DD): ")
    try:
        target_amount = int(target_amount)
        if target_amount <= 0:
            print("Target amount must be a positive number.")
            return
        cursor = mydb.cursor()
        query = """INSERT INTO savings_goals (goal_name, target_amount, target_date) 
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (goal_name, target_amount, target_date))
        mydb.commit()
        print("Savings goal set successfully.")
    except ValueError:
        print("Invalid amount or date. Please enter valid values.")
    except Exception as e:
        print(f"Error setting savings goal: {e}")

