import random

def Roulette():
    
    playerIn = ()
    red =[1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36]
    black = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35]
    green = 0
    even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
    player= 0

    print('***Options to Bet From***')
    print('   ~~~~~~~~~~~~~~~~~~~')
    print('Red = 1')
    print('Black = 2')
    print('Green (Zero) = 3')
    print('Odd = 4')
    print('Even = 5')
    print('Number = 6')
    print('____________________________________________________________')
    print('Enter number that corrisponds with bet, then press enter')
    print('____________________________________________________________')
    player = int(input('Place your bet, 1-6: '))
    print('____________________________________________________________')
    
    if player == 6:
        playerIn =int(input('Enter Number to bet: '))
    
    print('You Bet option:',player)
    
    spin = random.randint(0,36)
    print('Landed on: ',spin)
    print('____________________________________________________________')


    if player==1:
        if spin in red:
            print('You won')
        else:
            print('You Lost')
             
    elif player==2:
        if spin in black:
            print('You won')
        else:
            print('You Lost')
    
    elif player==3:
        if spin == green:
            print('You won')
        else:
            print('You Lost')
             
    elif player==4:
        if spin in odd:
            print('You won')
        else:
            print('You Lost')
            
    elif player==5:
        if spin in even:
            print('You won')
        else :
            print('You Lost')
             
    elif player==6:
        if spin == playerIn:
            print('You won')
        else:
            print('You Lost')
    else:
        print('invalid bet')
