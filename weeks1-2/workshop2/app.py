from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

while True:  
    name = input("Enter name to Register: ")
    if len(name) > 10:
        print("The maximum name length is 10 characters")
    elif len(name) < 1:
        print("The manimum name length is 1 character")
    else:
        break

while True:
    PIN = input("Enter PIN: ")  
    if len(PIN) == 4:
        break
    else:
        print("PIN must be 4 numbers") 

balance = 0
strbalance = str(balance)
print(name, "Has been registered with a starting balance of $" + strbalance)

while True:
    print("LOGIN")
    login_name = input("Enter name: ")
    login_pin = input("Enter PIN: ")
    if (login_name == name) & (login_pin == PIN):
        print("login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.showbalance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.showbalance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.showbalance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("That was not a valid option")
        continue





