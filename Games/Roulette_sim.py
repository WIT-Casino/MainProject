import random
def Roulette():
    """Roullette game"""
    
    bet = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,1000]
    i =1

    red =[1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36]
    black = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35]
    green = 0
    even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
    player= 0
    #print('____________________________________________________________')
    #print('Red=1, Black=2, Green=3, Odd=4, Even=5')
    player = random.randint(1,5)
   # print('____________________________________________________________')
    #print('you bet:',player)
    #print('____________________________________________________________')
    spin = random.randint(0,36)
    #print('Landed on: ',spin)
    #print('____________________________________________________________')
    ranBet= random.choice(bet)
    winnings = ranBet*2
   # winningsG = ranBet*35
    betR = ranBet
    if player==1:
        if spin in red:
            return 1
        else:
            return 0
            
    elif player==2:
        if spin in black:
            return 1
        else:
            return 0
    
    elif player==3:
        if spin == green:
            return 1
        else:
            return 0
            
    elif player==4:
        if spin in odd:
            return 1
        else:
            return 0
            
    elif player==5:
        if spin in even:
            return 1
        else :
            return 0
    #print('__________________________________________________________')    

