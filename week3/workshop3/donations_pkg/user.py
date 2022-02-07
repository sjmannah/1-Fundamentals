def login(database, username, usernameUP, password):

    if (username in database):
        if (database[username] == password):
            print("Welcome " + usernameUP , "\n")
            #print(username in database)
            #print(database[username])
            print("Logged in as: " + usernameUP)
            return username
        else:
            print("Incorrect password")
            return ""
    else:
        print("Username not found")
        return ""
 
def register(database, username, password):
    if (len(username) > 10):
        print("This Username is too long, please try again")
        return ""
    elif (len(password) < 5):
        print("This password is too short, please try again")
        return ""
    else:
        if (username in database):
            print("\nUsername already registered")
            return ""
        else:
            print("Username has been registered\n")
            return username
 



