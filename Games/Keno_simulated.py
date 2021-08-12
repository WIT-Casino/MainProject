def Keno():

    board = (range(1,80))
    sim = random.sample(board,10)
    keno = random.sample(board,10)

    print('Computer picks: ',keno)
    print ('Your picks: ', sim)
    print('__________________________________________________________')

    def intersection(sim, keno):
       return(set(sim).intersection(keno))
       
    if len(intersection(sim,keno)) ==0:
        return 0
    else:
        return 1
