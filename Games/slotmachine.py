import random
def slots():
    attempts = 0
    while attempts < 5:
        slot1 = random.randint(1,10)
        slot2 = random.randint(1,10)
        slot3 = random.randint(1,10)
        print('\033[91m'+"YOUR ROLL:")
        print('\033[0m'+'---------------------')
        print("[",slot1,"]","[",slot2,"]","[",slot3,"]")
        print('---------------------')
        combo12 = 0
        combo23 = 0
        combo13 = 0
        combo123 = 0

        if slot1 == slot2:
            combo12 = True
        elif slot2 == slot3:
            combo23 = True
        elif slot1 == slot3:
            combo13 = True
        elif slot1 == slot2 == slot3:
            combo123 = True
        
        if combo12 == True or combo23 == True or combo13 == True:
            print("Two Matching Slots, You win 2x multiplier!")
            print('---------------------')
        elif combo123 == True:
            print("Three Matching Slots, You win 10x multiplier!")
            print('---------------------')
        else:
            print("Better Luck Next Time, Try Again!")
            print('---------------------')
        attempts += 1
