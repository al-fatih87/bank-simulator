import DatabaseConnection
import locale


# We create bank account by adding new records into the Customers table

trigger = DatabaseConnection.sql.connect(host=DatabaseConnection.host, user=DatabaseConnection.user,
                                         password=DatabaseConnection.password, database="Customers")
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
