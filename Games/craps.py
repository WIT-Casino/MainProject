import random
def craps():
    print("Welcome to Craps, enter R to roll for Player 1")
    userinput = input()
    if (userinput == "R") or (userinput == "r"):
        dice = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("Dice 1: ", dice)
        print("Dice 2: ", dice2)
    else:
        print("Input not recognized, try again")
    dicesum1 = dice + dice2
    print("Enter R to roll for Player 2")
    userinput2 = input()
    if (userinput2 == "R") or (userinput2 == "r"):
        dice3 = random.randint(1,6)
        dice4 = random.randint(1,6)
        print("Dice 1: ", dice3)
        print("Dice 2: ", dice4)
    else:
        print("Input not recognized, try again")
    dicesum2 = dice3 + dice4
    if dicesum1 > dicesum2:
        print("Player 1 wins!")
    elif dicesum2 > dicesum1:
        print("Player 2 wins!")
    elif dicesum1 == dicesum2:
        print("Tie!")

# craps()
