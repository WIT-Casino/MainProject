import random
def craps():
    # print("Welcome to Craps, enter R to roll for Player 1")
    userinput = "r"
    if (userinput == "R") or (userinput == "r"):
        dice = random.randint(1,6)
        dice2 = random.randint(1,6)
        # print("Dice 1: ", dice)
        # print("Dice 2: ", dice2)
    else:
        print("Input not recognized, try again")
    dicesum1 = dice + dice2
    # print("Enter R to roll for Player 2")
    userinput2 = "r"
    if (userinput2 == "R") or (userinput2 == "r"):
        dice3 = random.randint(1,6)
        dice4 = random.randint(1,6)
        # print("Dice 1: ", dice3)
        # print("Dice 2: ", dice4)
    else:
        print("Input not recognized, try again")
    dicesum2 = dice3 + dice4
    if dicesum1 > dicesum2:
        return 0
    elif dicesum2 > dicesum1:
        return 1
    elif dicesum1 == dicesum2:
        craps()


def main():
    craps()

if __name__ == "__main__":
    main()

