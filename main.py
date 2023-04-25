import DatabaseConnection
import CreateBankAccount
import AccountBalance
import CashDeposit
import Transfers


def ussd_dail():
    user_action = input("Please select option (corresponding figure: \n"
                        "1: Check Account Balance\n"
                        "2: Deposit\n"
                        "3: Transfer\n"
                        "4: Create Account\n"
                        "5: Quit\n")

    if user_action == "1":
        AccountBalance.account_bal_retrieval()
    elif user_action == "2":
        CashDeposit.cash_deposit()
    elif user_action == "3":
        Transfers.cash_transfer()
    elif user_action == "4":
        CreateBankAccount.create_account()
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

