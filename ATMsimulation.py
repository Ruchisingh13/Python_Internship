name = input("Enter Your Name: ")
print("Hello", name)

message = """
How may I help you sir/ma'am.

Please select any of these options:
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWAL.
"""

print(message)
task = int(input("Please Insert your Option:"))
available_amount = 5000

if task >= 1 and task <= 3:  # Check if task is between 1 and 3
    print("Welcome to your virtual bank!")

    # Check balance
    if task == 1:
        print("Your available balance is:", available_amount)

    # Deposit amount
    elif task == 2:
        deposit_amount = int(input("Please Enter Deposit Amount:"))

        if deposit_amount >= 500:
            available_amount += deposit_amount
            print("You have successfully deposited:", deposit_amount)
            print("Your available balance is:", available_amount)
        else:
            print("Please enter an amount more than 500 rupees!")

    # Withdrawal amount
    elif task == 3:
        withdrawal_amount = int(input("Please enter withdrawal amount:"))
        
        if withdrawal_amount <= available_amount:
            available_amount -= withdrawal_amount
            print("successfully withdrawl and  your current balance is:", available_amount)
        else:
            print("Not sufficient amount!")

else:
    print("Please choose a correct option between 1 and 3!")





