def showbalance(balance):
    print("The currect balance is $" + str(balance))

def deposit(balance):
    amount = input("Enter amount to Deposit: ")
    newbalance = float(amount) + float(balance)
    return newbalance

def withdraw(balance):
    amount = input("Enter amount to Withdraw: ")
    if float(amount) > float(balance):
        print("Insufficient Funds")
        return balance
    else:
        return (float(balance) - float(amount))

def logout(name):
    print("Goodbye " + name + "!")

