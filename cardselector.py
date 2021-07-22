import random
#def cardselector():
    #print("Type D to Draw a card")
    #userinput = input()
    #if (userinput == "D") or (userinput == "d"):
        #cardchoice = random.randomint(1,52)
        if cardchoice <= 13: #Spades
            if cardchoice < 11 and cardchoice != 1:
                print(cardchoice, " of Spades")
            elif cardchoice == 1:
                print("Ace of Spades")
            elif cardchoice == 11:
                print("Jack of Spades")
            elif cardchoice == 12:
                print("Queen of Spades")
            elif cardchoice == 13:
                print("King of Spades")
        elif cardchoice >= 14 and cardchoice <= 26: #Hearts
            if cardchoice > 14 and cardchoice < 24:
                print(cardchoice, " of Hearts")
            elif cardchoice == 14:
                print("Ace of Hearts")
            elif cardchoice == 24:
                print("Jack of Hearts")
            elif cardchoice == 25:
                print("Queen of Hearts")
            elif cardchoice == 26:
                print("King of Hearts")
        elif cardchoice <= 39 and cardchoice > 26: #Diamonds
        elif cardchoice <= 52 and cardchoice > 39: #clubs
