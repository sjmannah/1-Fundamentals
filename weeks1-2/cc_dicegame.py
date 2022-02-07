import random

HIGH_SCORE = 0
     
def dice_game():
    global HIGH_SCORE
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    print("\nYou roll a...", + roll1)
    print("You roll a...", + roll2)
    total = roll1 + roll2
    print("\nYou rolled a total of:", + total)
    if (total > HIGH_SCORE):
        
        HIGH_SCORE = total
        print("\nNew High Score!")

while True:
    print("Current high score", + HIGH_SCORE)
    print("1) Roll Dice\n2) Leave Game")
    choice  = input("Enter your choice:")
    if (choice == "1"):
        dice_game()
    elif (choice == "2"):
        print("Goodbye!")
        break
    