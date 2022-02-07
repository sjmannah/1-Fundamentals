import random

def guess_random_number(tries, start, stop, num):
    #num  = random.randint(start, stop)
    guesses = []
    while tries > 0:
        print(f"Number of Tries left: {tries}")
        guess = int(input(f"Guess a number between {start} and {stop} :"))
        if guess in guesses:
            print("You have already guessed this number")
            continue

        guesses.append(guess)

        #print(guesses)
        if guess < start or guess > stop:
            print(f"This Guess is incorrect! Please enter a number in the range of {start} to {stop}")
            tries -= 1
            continue

        if num == guess:
            print("You guessed the correct number!\n")
            break
        elif num > guess:
            print("Guess Higher!")
        else:
            print("Guess Lower!")
            
        tries -= 1
    
    if tries == 0:
        print(f"You have failed to guess the number {num}\n")
    #print(f"You failed to guess the number {num}")

def guess_random_num_linear(tries, start, stop, num):
    #num  = random.randint(start, stop)
    print(f"The number for the program to guess is {num}")
    for x in range(start, stop):
        print(f"Number of tries left is {tries}")
        print(f"The program is guessing ... {x}")
        tries -= 1
        
        if num == x:
            
            print("The program has guessed the correct number!\n")
            return  True
            
        elif tries == 0:
            print("The program has failed to guess the correct number.\n")
            return False
        
def guess_random_num_binary(tries, start, stop, num):
    #num  = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop
    print(f"Random number to find: {num}")

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        #pivot_value = the_list[pivot]

        if pivot == num:
            return print(f"Found it {num}\n")
        if pivot > num:
            upper_bound = pivot - 1
            print("Guessing Lower")
            #print(pivot)
        elif pivot < num:
            lower_bound = pivot + 1
            print("Guessing Higher")
            #print(pivot)
        elif tries == 0:
            return print("The program has failed to guess the correct number.\n")
        tries -= 1

def askUser():
    while True:
        start = int(input("Enter a starting number: "))

        stop = int(input("Enter an ending number: "))
        tries = int(input("Enter number of tries: "))
        if start >= stop:
            print("Start number must be greater than stop number")
            continue
        else:
            return (tries, start, stop)



def gambling_game(start, stop):

    winnings = 10
    while winnings > 0:
        guess = input("\nWill the computer guess right or not? Y/N? ")
        num  = random.randint(start, stop)

        while True:
            bet = int(input(f"You have ${winnings} to bet, who much would you like to bet?"))
            if bet > winnings:
                print("You can only bet ${winnings} or less\n")
            else:
                break
        tries = (stop - start)/2
        win = guess_random_num_linear(tries, start, stop, num)
        #print(f"The computer won or lost {win}")

        if (win == True) and (guess =="Y"):
            winnings = (winnings-bet) + bet *2
        elif (win == False) and (guess == "N"):
            winnings = winnings + bet *2
        else:
            winnings = winnings - bet 
    
        strstop = input(f"\nYou have ${winnings}. Would you like to keep playing, Y/N? ")
        if strstop == "N":
            break

    #print(winnings)
    

    


(tries, start, stop) = askUser()

num  = random.randint(start, stop)

gambling_game(start, stop)
guess_random_number(tries, start, stop, num)
guess_random_num_linear(tries, start, stop, num)
guess_random_num_binary(tries, start, stop, num)