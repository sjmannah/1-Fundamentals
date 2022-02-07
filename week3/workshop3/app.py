from donations_pkg.homepage import show_homepage
from donations_pkg.user import login
from donations_pkg.user import register
from donations_pkg.homepage import donate
from donations_pkg.homepage import show_donations
 
database = {"admin": "password123"}
donations = []
authorized_user = ""
user_print = ""

if authorized_user == "":
    print("You must be logged in to donate")
else:
    print("Logged in as: " + authorized_user)



while True:

    show_homepage()


    choice = input("Choose an Option: ")
    if choice == "1":
        usernameUP = input("\nEnter your username: ")
        username = usernameUP.lower()
        password = input("Enter your password: ")
        authorized_user = login(database, username, user_print, password)

        #print (authorized_user)
    elif choice == "2":
        user_print = input("\nEnter your username: ")
        username = user_print.lower()
        password = input("Enter your password: ")
        authorized_user = register(database, username, password)
        if authorized_user:
            database[authorized_user] = password

    elif choice == "3":
        if not authorized_user:
            print("\nYou are not logged in")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
            #print(donations)
    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("This is not a valid choice, please enter again ")
