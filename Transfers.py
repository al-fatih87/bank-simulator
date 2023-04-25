import DatabaseConnection
import locale

locale.setlocale(locale.LC_MONETARY, 'en_NG')

# We create bank account by adding new records into the Customers table

trigger = DatabaseConnection.sql.connect(host=DatabaseConnection.host, user=DatabaseConnection.user,
                                         password=DatabaseConnection.password, database="Customers")
trigger_handle = trigger.cursor()


def cash_transfer():
    sender_acc_input = input("Please enter your account Number: \n")
    transfer_amount = input("Enter transfer amount: \n")
    con_transfer_amount = float(transfer_amount)
    verify_tx_amount = locale.currency(con_transfer_amount, grouping=True)
    receiver_acc_num = input("Enter receiver's account number: \n")

    # We verify receiver's account details
    try:
        verify_receiver = "SELECT Name FROM Customers WHERE Account_Number = %s"
        receiver_name_value = (str(receiver_acc_num),)
        trigger_handle.execute(verify_receiver, receiver_name_value)
        name_display_tpl = trigger_handle.fetchone()
        name_display = name_display_tpl[0]
        print(f"You are sending {verify_tx_amount} to {name_display} ({receiver_acc_num}). \n"
              f" Do you confirm this to be correct? Yes/No")
        verify_response = input("")
        if verify_response.lower() == "yes":

            # We debit sender's account
            # first, we get account balance of sender
            try:
                sender_balance_query = "SELECT Balance FROM Customers WHERE Account_Number = %s"
                sender_bal_value = (str(sender_acc_input),)  # convert the input to string
                trigger_handle.execute(sender_balance_query, sender_bal_value)
                sender_acc_bal_tpl = trigger_handle.fetchone()
                sender_acc_bal = sender_acc_bal_tpl[0]
            except Exception as ex:
                print("Failed to carry out operation")
                print(ex)

            # 1. We convert the string tuple to float for calculation
            sender_old_bal = float(sender_acc_bal)
            sender_new_bal = sender_old_bal - con_transfer_amount
            if sender_new_bal < 1:
                print("Sorry, you do not have sufficient funds to carry out this transaction."
                      "Kindly fund your account and try again.")
                quit()
            else:
                # We update receiver's record on database with new balance
                try:
                    update_query = "UPDATE Customers SET Balance = %s WHERE Account_Number = %s"
                    sender_new_bal_value = (str(sender_new_bal), str(sender_acc_input))  # convert the input to string
                    trigger_handle.execute(update_query, sender_new_bal_value)
                    trigger.commit()
                except Exception as ex:
                    print("Failed to carry out operation")
                    print(ex)

            # 2. We credit receiver's account with the imputed amount
            try:
                receiver_balance_query = "SELECT Balance FROM Customers WHERE Account_Number = %s"
                receiver_bal_value = (str(receiver_acc_num),)  # convert the input to string
                trigger_handle.execute(receiver_balance_query, receiver_bal_value)
                acc_bal_tpl = trigger_handle.fetchone()
                acc_bal = acc_bal_tpl[0]
            except Exception as ex:
                print("Failed to carry out operation")
                print(ex)

            # 2. We convert the string tuple to float for calculation
            old_bal = float(acc_bal)
            new_bal = old_bal + con_transfer_amount

            # We update receiver's record on database with new balance
            try:
                update_query = "UPDATE Customers SET Balance = %s WHERE Account_Number = %s"
                new_bal_value = (str(new_bal), str(receiver_acc_num))  # convert the input to string
                trigger_handle.execute(update_query, new_bal_value)
                trigger.commit()
            except Exception as ex:
                print("Failed to carry out operation")
                print(ex)

            print("Transaction successful! Money has been sent.")
            print("===============================================\n")
        else:
            print("Transaction Cancelled."
                  "Thanks for banking with us.")
    except Exception as ex:
        print("Operation failed.")
        print(ex)


