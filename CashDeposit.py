import DatabaseConnection

# We create bank account by adding new records into the Customers table

trigger = DatabaseConnection.sql.connect(host=DatabaseConnection.host, user=DatabaseConnection.user,
                                         password=DatabaseConnection.password, database="Customers")
trigger_handle = trigger.cursor()


def cash_deposit():
    cus_input = input("Enter account Number: \n")
    deposit = input("Enter deposit amount: \n")
    deposit_amount = float(deposit)
    # we select account balance from the user input
    try:
        acc_balance = "SELECT Balance FROM Customers WHERE Account_Number = %s"
        bal_value = (str(cus_input),)  # convert the input to string
        trigger_handle.execute(acc_balance, bal_value)
        acc_bal_tpl = trigger_handle.fetchone()
        acc_bal = acc_bal_tpl[0]
    except Exception as ex:
        print("Failed to carry out operation")
        print(ex)
    # We convert the string tuple to float/int for calculation
    old_bal = float(acc_bal)
    new_bal = old_bal + deposit_amount

    # We update record on database
    try:
        acc_balance = "UPDATE Customers SET Balance = %s WHERE Account_Number = %s"
        bal_value = (str(new_bal), str(cus_input))  # convert the input to string
        trigger_handle.execute(acc_balance, bal_value)
        trigger.commit()
    except Exception as ex:
        print("Failed to carry out operation")
        print(ex)
    print("Cash deposit successful! Account balance has been updated.")
    print("===============================================\n")
    print("What would you like to do next? \n")


