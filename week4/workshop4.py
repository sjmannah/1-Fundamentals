class User:
    def __init__(self, name, pin, passowrd):
        self.name = name
        self.pin = pin
        self.password = passowrd

#bob = User("Bob", 1234, "password")

#print(bob.name, bob.pin, bob.password)

    def change_name(self, new_name):
        self.name = new_name
    
    def change_pin(self, new_pin):
        self.pin = new_pin
    
    def change_password(self, new_password):
        self.password = new_password

'''
bob = User("Bob", 1234, "password")
print(bob.name, bob.pin, bob.password)
bob.change_name("Steve")
bob.change_pin(4321)
bob.change_password("word")
print(bob.name, bob.pin, bob.password)
'''

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    
    def show_balance(self):
        print(self.name, "has an account balance of $" + str(self.balance))
    
    def withdraw(self, w_amount):
        self.w_amount = w_amount
        self.balance -= w_amount
        print(self.name, "has withdrawn $" + str(w_amount))
    
    def deposit(self, d_amount):
        self.d_amount = d_amount
        self.balance += d_amount
        print(self.name, "has deposited $" + str(d_amount))

    def transfer_money(self, t_amount, user):
        self.t_amount = t_amount
        
        print("\nYou are Transferring $" + str(t_amount) + " to", user.name)
        print("Authentication required")
        pin = input("Enter PIN ")
        if self.pin == int(pin):
            print("Transfer authorized")
            print("Transferring " + str(t_amount) + " to", user.name)
            self.balance -= t_amount
            user.balance += t_amount
            return True
        else:
            print("Invalid PIN. Transaction canceled")
            return False
    
    def request_money(self, amount, user):
        self.amount = amount
        
        print("\nYou are requesting $" + str(amount) + " From", user.name)
        print("User authentication is required...")
        pin = input(f"Enter {user.name} pin: ")
        password = input("Enter your password ")
        if (user.pin == int(pin)):
            if (self.password == password):
                #self.transfer_money(amount, user.name, user)
                user.balance -= amount
                self.balance += amount
                print(f"{user.name} sent $" + str(amount))
                return True
            else:
                print("Invalid password. Transaction canceled")
                return False
        else: 
            print("Invalid PIN. Transaction canceled")
            return False

        


    

user1 = BankUser("Bob", 1234, "password")
#print(buser.name, buser.pin, buser.password)
#buser.show_balance()
#buser.deposit(1000)
#buser.show_balance()
#buser.withdraw(500)
#buser.show_balance()
#buser.transfer_money(500, "Alice")
user2 = BankUser("Alice", 4321, "alicepassword")

user2.balance = 5000

user2.show_balance()
user1.show_balance()
user2.transfer_money(500, user1)
user2.show_balance()
user1.show_balance()
user2.request_money(250, user1)

user2.show_balance()
user1.show_balance()
  
