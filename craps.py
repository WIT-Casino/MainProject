def game():
    print("Welcome to Craps, enter R to roll")
    userinput = input()
    if (userinput == "R"):
        dice = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("Dice 1: ", dice)
        print("Dice 2: ", dice2)
    else:
        print("Input not recognized, try again")

