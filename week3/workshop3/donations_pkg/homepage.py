def show_homepage():
    print("     === DonateMe Homepage ===     ")
    print("--------------------------------------")
    print("| 1. Login       | 2. Register        |")
    print("--------------------------------------")
    print("| 3. Donate      | 4. Show Donations  |")
    print("--------------------------------------")
    print("|             5. Exit                 |")
    print("--------------------------------------")


#show_homepage()

def donate(username):
    
    donation_flt = float(input("Enter amount to donate :"))
    donation = (username + " Donated : $" + str(donation_flt))
    print("\nThank you for your Donation!")
    return donation

def show_donations(donations):

    print("\n--- All Donations ---")
    if not donations:
        print("Currently there are no donations")
    else:
        for items in donations:
            print(items)
        

