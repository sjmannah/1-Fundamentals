print("Welcome to Golden State Warriors Trivia!")

while True:
    user_name = input("Please enter your name to get started: ")

    print(f"Hello {user_name} Thanks for Playing!")
    yn = input("Are you ready to start? Y/N ")
    if not (yn == "Y"):
        print("OK let's play another time!")
        break

    score = 0

    print("Question 1.....")
    def askQuestion(answer):
        choice = input(">")
        if (choice == answer):
            print("Correct!") 
            global score
            score = score + 1 
        else:
            print(f"Unfortunately the correct answer is {answer} ")

    print("Who is the leading scorer for the Golden State Warriors?")
    print("Is it...\nA. Stephen Curry\nB. Wilt Chaimberlain\nC. Klay Thompson\nD. Rick Barry")
    askQuestion("A")

    print("\nQuestion 2.....")

    print("What year did the Warriors win their first championship?")
    print("Is it...\nA. 1950\nB. 1947\nC. 1999\nD. 2015")
    askQuestion("B")

    print("\nQuestion 3.....")

    print("What year did the Warriors first play at the Chase Center in San Francisco?")
    print("Is it...\nA. 1990\nB. 2021\nC. 2020\nD. 2019")
    askQuestion("D")

    print("\nQuestion 4.....")

    print("In the 2015 playoffs, Steph Curry broke the record for most three-pointers in a single postseason. Whose record did he break??")
    print("Is it...\nA. Reggie Miller \nB. Ray Allen \nC. Michael Jordan\nD. LeBron James")
    askQuestion("A")

    print("\nQuestion 5.....")

    print("What Golden State Warrior was named MVP of the 1975 NBA Finals?")
    print("Is it...\nA. Clifford Ray \nB. Rick Barry \nC. Nate Thurmond\nD. Keith Wilkes")
    askQuestion("B")

    print("\nQuestion 6.....")

    print("in 2016, the Warriors went 73-9 to set a new NBA record, which team's record did they beat?")
    print("Is it...\nA. Los Angeles Lakers \nB. Boston Celtics \nC. NEw York Knicks \nD. Chicago Bulls")
    askQuestion("D")

    print("\nQuestion 7.....")

    print("in 2015, who won NBA finals MVP for the Warriors?")
    print("Is it...\nA. Andre Igoudala \nB. Stephen Curry \nC. Kevin Durant \nD. Draymond Green")
    askQuestion("A")

    print("\nQuestion 8.....")

    print("In what year did the Warriors Franchise first move to San Francisco")
    print("Is it...\nA. 2019 \nB. 1947 \nC. 1962 \nD. 1975")
    askQuestion("C")

    print(f"\nYou answered {score} out of 8 questions right! Congrats\n Thanks for playing!")





