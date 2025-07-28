SAVR – Command-Line Financial Management Tool

SAVR is a Python-based command-line application designed to help small-scale entrepreneurs manage their finances more effectively. The application allows users to track income, expenses, set budgets, and monitor savings goals — all through a simple terminal interface.

Features

Add and manage income sources
Record and categorize expenses
Set budget limits for different categories
Define savings goals and monitor progress
View a comprehensive financial summary (income, expenses, budget, savings, net balance)
Intuitive text-based user interface
Stores data using a MySQL database
Tech Stack

Python 3
MySQL
python-dotenv for managing environment variables
Git and GitHub for version control and collaboration
Setup Instructions

1. Clone the Repository
git clone https://github.com/dianahshimwa/finance-management-app.git
cd finance-management-app
2. Configure Environment Variables
Create a .env file in the root directory of the project and add the following:

DATABASE=alu_finance_tracking  
HOST=localhost  
DB_USER=root  
DB_PASSWORD=your_mysql_password
Replace your_mysql_password with your actual MySQL root password.

3. Install Dependencies
Make sure Python 3 and pip are installed. Then, run:

pip install mysql-connector-python python-dotenv
4. Start the MySQL Server
Ensure your MySQL server is running locally. Then, create the database (if it doesn't already exist):

CREATE DATABASE alu_finance_tracking;
The required tables will be created automatically when you run the application.

5. Run the Application
python app.py
How to Use

Once launched, the application displays a menu with the following options:

Add Income
Add Expense
Set Budget
Set Savings Goal
View Financial Summary
Exit
Enter the number corresponding to the action you want to perform, then follow the on-screen prompts.

Contributors

Name	                     GitHub Username / Contact
Kabera Samuel	             [KaberaSamuel]
David Shumbusho	             [Shumbusho43]
Dianah Shimwa Gasasira       [dianahshimwa]
Cyuzuzo Terance	             [terancebana]
Elijah Kabatsi	             [elijahkabatsi]
David Katete	             [dkatate]
Given Edward	             [givenedward]

License

This project was developed for educational purposes at African Leadership University (ALU) as part of Peer Learning Days. No official license has been applied.