import random
def blackjack():

    dealercard = 0
    print("-----------------")
    print('\033[91m'+"Dealing Dealer Hand: ")
    print('\033[0m'+"-----------------")
    while dealercard < 17:
        cardchoice2 = random.randint(1,52)
        if cardchoice2 <= 13: #Spades
            if cardchoice2 < 11 and cardchoice2 != 1:
                print(cardchoice2, "of Spades")
                dealercard = dealercard + cardchoice2
            elif cardchoice2 == 1:
                print("Ace of Spades")
                dealercard = dealercard + 1
            elif cardchoice2 == 11:
                print("Jack of Spades")
                dealercard = dealercard + 10
            elif cardchoice2 == 12:
                print("Queen of Spades")
                dealercard = dealercard + 10
            elif cardchoice2 == 13:
                print("King of Spades")
                dealercard = dealercard + 10
        elif cardchoice2 >= 14 and cardchoice2 <= 26: #Hearts
            if cardchoice2 > 14 and cardchoice2 < 24:
                print((cardchoice2-14), "of Hearts")
                dealercard = dealercard + (cardchoice2-14)
            elif cardchoice2 == 14:
                print("Ace of Hearts")
                dealercard = dealercard + 1
            elif cardchoice2 == 24:
                print("Jack of Hearts")
                dealercard = dealercard + 10
            elif cardchoice2 == 25:
                print("Queen of Hearts")
                dealercard = dealercard + 10
            elif cardchoice2 == 26:
                print("King of Hearts")
                dealercard = dealercard + 10
        elif cardchoice2 <= 39 and cardchoice2 > 26: #Diamonds
            if cardchoice2 > 27 and cardchoice2 < 37:
                print((cardchoice2-26), "of Diamonds")
                dealercard = dealercard + (cardchoice2-26)
            elif cardchoice2 == 27:
                print("Ace of Diamonds")
                dealercard = dealercard + 1
            elif cardchoice2 == 37:
                print ("Jack of Diamonds")
                dealercard = dealercard + 10
            elif cardchoice2 == 38:
                print ("Queen of Diamonds")
                dealercard = dealercard + 10
            elif cardchoice2 == 39:
                print ("King of Diamonds")
                dealercard = dealercard + 10
        elif cardchoice2 <= 52 and cardchoice2 > 39: #clubs
            if cardchoice2 == 40:
                print("Ace of Clubs")
                dealercard = dealercard + 1
            elif cardchoice2 > 40 and cardchoice2 < 50:
                print((cardchoice2-39), "of Clubs")
                dealercard = dealercard + (cardchoice2-39)
            elif cardchoice2 == 50:
                print ("Jack of Clubs")
                dealercard = dealercard + 10
            elif cardchoice2 == 51:
                print ("Queen of Clubs")
                dealercard = dealercard + 10
            elif cardchoice2 == 52:
                print ("King of Clubs")
                dealercard = dealercard + 10
        print("Current dealer hand value: " , dealercard, "\n -----------------")


    playercard = 0
    print('\033[91m'+"Dealing Player Hand: ")
    print('\033[0m'+"-----------------")
    while playercard < 17:
        cardchoice = random.randint(1,52)
        if cardchoice <= 13: #Spades
            if cardchoice < 11 and cardchoice != 1:
                print(cardchoice, "of Spades")
                playercard = playercard + cardchoice
            elif cardchoice == 1:
                print("Ace of Spades")
                playercard = playercard + 1
            elif cardchoice == 11:
                print("Jack of Spades")
                playercard = playercard + 10
            elif cardchoice == 12:
                print("Queen of Spades")
                playercard = playercard + 10
            elif cardchoice == 13:
                print("King of Spades")
                playercard = playercard + 10
        elif cardchoice >= 14 and cardchoice <= 26: #Hearts
            if cardchoice > 14 and cardchoice < 24:
                print((cardchoice-14), "of Hearts")
                playercard = playercard + (cardchoice-14)
            elif cardchoice == 14:
                print("Ace of Hearts")
                playercard = playercard + 1
            elif cardchoice == 24:
                print("Jack of Hearts")
                playercard = playercard + 10
            elif cardchoice == 25:
                print("Queen of Hearts")
                playercard = playercard + 10
            elif cardchoice == 26:
                print("King of Hearts")
                playercard = playercard + 10
        elif cardchoice <= 39 and cardchoice > 26: #Diamonds
            if cardchoice > 27 and cardchoice < 37:
                print((cardchoice-26), "of Diamonds")
                playercard = playercard + (cardchoice-26)
            elif cardchoice == 27:
                print("Ace of Diamonds")
                playercard = playercard + 1
            elif cardchoice == 37:
                print ("Jack of Diamonds")
                playercard = playercard + 10
            elif cardchoice == 38:
                print ("Queen of Diamonds")
                playercard = playercard + 10
            elif cardchoice == 39:
                print ("King of Diamonds")
                playercard = playercard + 10
        elif cardchoice <= 52 and cardchoice > 39: #clubs
            if cardchoice == 40:
                print("Ace of Clubs")
                playercard = playercard + 1
            elif cardchoice > 40 and cardchoice < 50:
                print((cardchoice-39), "of Clubs")
                playercard = playercard + (cardchoice-39)
            elif cardchoice == 50:
                print ("Jack of Clubs")
                playercard = playercard + 10
            elif cardchoice == 51:
                print ("Queen of Clubs")
                playercard = playercard + 10
            elif cardchoice == 52:
                print ("King of Clubs")
                playercard = playercard + 10
        print("Current player hand value: " , playercard, "\n -----------------")

    if playercard > 21 and dealercard < 21:
        return 0
    elif dealercard > 21 and playercard < 21:
        return 1
    elif dealercard == playercard:
        blackjack()
    elif playercard > dealercard:
        return 1
    elif dealercard > playercard:
        return 0


