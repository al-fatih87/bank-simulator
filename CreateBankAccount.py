import DatabaseConnection
import random
from main import ussd_dail

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

ussd_dail()