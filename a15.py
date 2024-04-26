import time
class bankAccount:
    def __init__(self, strName, intBalance):
        self.name = strName
        self.balance = intBalance
    def withdraw(self,flAmount):
        if self.balance >= flAmount:
            self.balance -= flAmount
            print("You have withdrawn ${0:.2f} from {1}".format(flAmount,self.name))
        else:
            print("You are broke.")
        sleepClear(1)
    def deposit(self,flAmount):
        self.balance += flAmount
        print("You have deposited ${0:.2f} into {1}".format(flAmount, self.name))
        sleepClear(1)
    def ckBalance(self):
        print("You have ${0:.2f} in {1}.".format(self.balance, self.name))
        sleepClear(1)

class savingsAcct(bankAccount):
    def __init__(self,strName, intBalance):
        super().__init__(strName, intBalance)
        print("You have created savings account: {0}".format(self.name))

class checkingAcct(bankAccount):
    def __init__(self,strName, intBalance):
        super().__init__(strName, intBalance)

    def writeCheck(self,flAmount):
        if self.balance >= flAmount:
            self.balance -= flAmount
            print("You have written a check for ${0:.2f} from {1}".format(flAmount, self.name))
        else:
            print("You don't have sufficient funds to write this check.")
        sleepClear(1)

def sleepClear(flTime):
    time.sleep(flTime)
    print("\n"*30)

def mainMenu():
    print("$"*80)
    print("$$","  Moseley Bank  ".center(74),"$$")
    print("$"*80)
    print("What do you want to do?")
    print("1. Deposit Money")
    print("2. Withdraw")
    print("3. Write a Check")
    print("4. Check Balance")
    print("5. Add an Account")
    strTmp = input("Enter Choice Here:")
    return strTmp

def showAccounts(lisAccounts):
    intIndex = 1
    for account in lisAccounts:
        str1 = str(intIndex).ljust(5)
        str2 = str(account.name).ljust(30,".")
        str3 = "${0:.2f}".format(account.balance).rjust(20,".")
        print(str1+str2+str3)
        intIndex += 1
    pressEnter()

def pressEnter():
    input("\nPress Enter/Return to continue...")
    print("\n"*5)

def createAccount(lisAccounts):
    strAccountType = input("Do you want a (1) Checking or (2) Savings account? ")
    strAcctName = input("What should the account be called? ")
    if strAccountType == "1":
        lisAccounts.append(checkingAcct(strAcctName, 50))
    elif strAccountType == "2":
        lisAccounts.append(savingsAcct(strAcctName, 50))
    else:
        print("That is not a valid choice.")
    showAccounts(lisAccounts)
    return lisAccounts

def makeDeposit(lisAccounts):
    showAccounts(lisAccounts)
    strAccount = input("Which Account?")
    strAmount = input("How Much?")
    if strAccount.isnumeric() and int(strAccount) <= len(lisAccounts):
        intIndex = int(strAccount) - 1
        lisAccounts[intIndex].deposit(float(strAmount))



lisAccounts = []
lisAccounts.append(savingsAcct("Main Savings",30))
lisAccounts.append(checkingAcct("Main Checking", 305))

while True:
    strMenu = mainMenu()
    if strMenu == "1":
        print("Make a deposit")
        makeDeposit(lisAccounts)
    elif strMenu == "2":
        print("Make a withdrawal")
    elif strMenu == "3":
        print("Write a Check")
        showAccounts(lisAccounts)
        try:
            strChoice = input("Which account do you want? ")
            flAmount = float(input("How much is the check for? "))
            intChoice = int(strChoice) - 1
            lisAccounts[intChoice].writeCheck(flAmount)
        except:
            print("Something went wrong.  Try again.")

    elif strMenu == "4":
        print("Check Balances")
        showAccounts(lisAccounts)
    elif strMenu == "5":
        print("Add an Account")
        lisAccounts = createAccount(lisAccounts)
    else:
        print("invalid entry")
        pressEnter()
