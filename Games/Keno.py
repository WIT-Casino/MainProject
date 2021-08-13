import random

def Keno():
    hi = []
    board = (range(1,80))
    keno = random.sample(board,10)
    val = 80

    for i in range (10):
        check = 0
        while check == 0:
            temp = int(input('Enter pick one at a time(1-80): '))
            if temp >= 0 and temp <= 80:
                check = 1
            else:
                print("Out of range. Input again!")
        
        hi.append(temp)
        picks=set(hi)
            
    print('__________________________________________________________')
    print('Computer picks: ',keno)
    print('__________________________________________________________')
    print ('Your picks: ', hi)
    print('__________________________________________________________')

    def intersection(picks, keno):
        return (set(picks).intersection(keno))

    print ('Number of matches:',len(intersection(picks,keno)))
    print('__________________________________________________________')
    if len(intersection(picks,keno)) ==0:
        print('No Matches')
    else:
        print('Matches are:',intersection(picks,keno))

