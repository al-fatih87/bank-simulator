from mysql import connector as sql
import random
import locale

# Database login
host = "localhost"
user = "root"
password = ""

# We connect to MySql Server


def sql_connect():
    try:
        db = sql.connect(host=host, user=user, password=password)
        print("Connection to database was Successfully!")
    except Exception as ex:
        print("Failed to connect")
        print(ex)
        print("Please check that your xampp is up and running and that MySQL service is running")

    print("===============================================\n")


# We create a database


def create_db():
    try:
        db = sql.connect(host=host, user=user, password=password)
        db_handler = db.cursor()
        db_handler.execute("CREATE DATABASE Customers")
    except Exception as ex:
        print(f"Could not create database.")
        print(ex)


# Creating customer tables in customers database
def create_table():
    try:
        db_cus_handler = sql.connect(host=host, user=user, password=password, database="Customers")
        cus_cus_handler = db_cus_handler.cursor()
        cus_cus_handler.execute("CREATE TABLE customers (Phone VARCHAR(11) PRIMARY KEY, Name VARCHAR(50), "
                                "Account_Number VARCHAR(10), Balance FLOAT)")
        print("Table has been created successfully!")
    except Exception as ex:
        print("Could not create the named table...")
        print(ex)


# Connecting to the customer database
def customer_dbconnect():
    try:
        db_cus = sql.connect(host=host, user=user, password=password, database="Customers")
        print("Connection to Customers database was Successfully!")
    except Exception as ex:
        print("Sorry, We could not connect to the defined database.")
        print(ex)
    print("===============================================\n")

    print("What would you like to do next? \n")


# We connect into the Customers table in the bank database

trigger = DatabaseConnection.sql.connect(host=DatabaseConnection.host, user=DatabaseConnection.user,
                                         password=DatabaseConnection.password, database="Customers")
trigger_handle = trigger.cursor()


# Function to create bank account
def create_account():
    full_name = input("Enter Full Name: \n")
    phone_number = input("Enter Phone Number: \n")
    account_number = random.randint(1234567890, 9999999999)
    account_balance = 1000

    acc_field = "INSERT INTO customers (Phone, Name, Account_Number, Balance) VALUES (%s, %s, %s, %s)"
    acc_details = (str(phone_number), str(full_name), str(account_number), str(account_balance))  # convert to string
    try:
        trigger_handle.execute(acc_field, acc_details)
        trigger.commit()
        print(trigger_handle.rowcount, "Process completed!")
        print("===============================================")
        print("Congratulations! Your account was successfully created.")
        print(f"Your account number is: {account_number} \n"
              f"And your account name is: {full_name} \n"
              f"Thanks for choosing XBZ Bank.")
    except Exception as ex:
        print("Account creation failed")
        print(ex)
    print("===============================================\n")
    print("What would you like to do next? \n")

# Account Balance

# We create bank account by adding new records into the Customers table

trigger = sql.connect(host=host, user=user, password=password, database="Customers")
trigger_handle = trigger.cursor()

locale.setlocale(locale.LC_MONETARY, 'en_NG')

def account_bal_retrieval():
    cus_input = input("Enter account Number: \n")
    # we select account balance from the user input
    try:
        acc_balance = "SELECT Balance FROM Customers WHERE Account_Number = %s"
        bal_value = (str(cus_input),)  # convert the input to string
        trigger_handle.execute(acc_balance, bal_value)
        acc_bal_tpl = trigger_handle.fetchone()
        acc_bal = acc_bal_tpl[0]
        acc_bal_currency = locale.currency(acc_bal, grouping=True)
    except Exception as ex:
        print("Failed to carry out operation")
        print(ex)

    #   we select account name from the user input
    acc_name = "SELECT Name FROM Customers WHERE Account_Number = %s"
    name_value = (str(cus_input),)
    trigger_handle.execute(acc_name, name_value)
    name_display_tpl = trigger_handle.fetchone()
    name_display = name_display_tpl[0]

    print(f"Dear {name_display},\n"
          f"your account balance is:\n"
          f" {acc_bal_currency}")
    print("===============================================\n")
    print("What would you like to do next? \n")


# Bank initialization


def ussd_dail():
    user_action = input("Please select option (corresponding figure: \n"
                        "1: Check Account Balance\n"
                        "2: Deposit\n"
                        "3: Transfer\n"
                        "4: Create Account\n"
                        "5: Quit\n")

    if user_action == "1":
        account_bal_retrieval()
    elif user_action == "2":
        cash_deposit()
    elif user_action == "3":
        cash_transfer()
    elif user_action == "4":
        create_account()
    elif user_action == "5":
        print("Thank you for banking with us.")
        quit()
    else:
        print("That input was not recognised. Please try again later")
        quit()


print("====================================================")
print("Welcome to XBZ Bank, your owned home banking system.")
print("====================================================\n")
qus = input("Do you have a database setup already? Yes or No\n")

if qus.lower() == "no":
    print("setting up database...")
    print("===============================================\n")
    DatabaseConnection.sql_connect()
    try:
        DatabaseConnection.create_db()
    except Exception as ex:
        print("Failed to create database")
        print(ex)
    try:
        DatabaseConnection.create_table()
    except Exception as ex:
        print("Failed to create table")
        print(ex)
    try:
        DatabaseConnection.customer_dbconnect()
    except Exception as ex:
        print("Failed to connect to customer table")
        print(ex)
    print("Customer database and relevant table has been created successfully.")
else:
    ussd_dail()

