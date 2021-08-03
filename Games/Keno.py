import random
hi = []
board = (range(1,80))
keno = random.sample(board,10)


for i in range (10):
    temp = int(input('Enter pick one at a time(1-80): '))
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