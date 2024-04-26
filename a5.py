# start with some $$
flSavings = 5555.55
flCheckings = 1111.11

# Welcome UI Message
print("^.^ " * 21)
print (" " * 30 + "Welcome to the ATM" )
print("^.^ " * 21)
# create a loop for the program
while (True):

    #Show the menu options
    print("Choose an option:")
    print("1 - Deposit ")
    print("2 - Withdraw")
    # Ask the user for their choice
    strMenu = input("what do you want to do?")

    if (strMenu == "1"):
        print("You want to make a deposit.")
        # ask for account
        acc_type = input("Enter 'S' for Savings or 'C' for Checking: ")
        # ask for amount
        amount = float(input("Enter the amount to deposit: "))
        if acc_type.upper() == 'S':
            flSavings += amount
            print(f"Deposit successful. Updated Savings Account Balance: ${flSavings:.2f}")
        elif acc_type.upper() == 'C':
            flCheckings += amount
            print(f"Deposit successful. Updated Checking Account Balance: ${flCheckings:.2f}")
        else:
            print("Invalid account type.")

    elif (strMenu == "2"):
        print("You want to make a withdrawal.")
        # ask for account
        acc_type = input("Enter 'S' for Savings or 'C' for Checking: ")
        # ask for amount
        amount = float(input("Enter the amount to withdrawal: "))
        if acc_type.upper() == 'S':
            flSavings -= amount
            print(f"Withdrawal successful. Updated Savings Account Balance:" . ljust(25,".") +  f"${flSavings:.2f}" .rjust(21,"."))
        elif acc_type.upper() == 'C':
            flCheckings -= amount
            print(f"Withdrawal successful. Updated Checking Account Balance: ${flCheckings:.2f}")
        else:
            print("Invalid account type.")



    else:
        print ("Sorry - that's not a valid choice")

    print("")
    strMore = input("Would you like another transaction?")

    if (strMore != "yes"):
        break