import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input("Pick a card or press Q to quit ")
    if choice == "Q":
        break
    elif (choice in diamonds):
        diamonds.remove(choice)
        hand.append(choice)
        print("Your Hand: ")
        print(hand)
        print("Remaining Cards:")
        print(diamonds)
    else:
        print("That was not a card in the deck")

if not diamonds:
    print("There are no more cards to pick")
