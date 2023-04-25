from mysql import connector as sql

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



