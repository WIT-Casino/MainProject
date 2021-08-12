import random

import time

try:
    from plotter import Plotter
    
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CasinoBackEnd.plotter import Plotter

class Simulation:
    def __init__ (self) : 
        pass

    def __del__ (self) :
        pass

    def simOnePlayerOneGame(self, player, winrate):
        currentOdds = winrate + player[0] * .015 + player[1] * .005 + player[2] * .03 
        random.seed(time.time())
        totalEarnings = 0
        winnings = 0
        bet =  1 + random.random() *24
        losses = 0
        if random.random() < currentOdds:
            winnings = winnings + bet
        else:
            losses = losses + bet

        winnings = winnings - losses

    def simOnePlayerNGames(self, player, winrate, numberOfGames):
        # player = [skill, luck, cheat]
                # base win rate + playerskill   + player luck     + player cheat
        currentOdds = winrate + player[0] * .015 + player[1] * .005 + player[2] * .03 
        random.seed(time.time())

        earningList = list([])
        earningList.clear()
        winningList = list([])
        winningList.clear()        
        lossesList = list([])
        lossesList.clear()
        iterList = list([])
        iterList.clear()

        totalWin = 0
        totalLoss = 0
        totalEarnings = 0
        
        for i in range(numberOfGames):
            bet = 1 + random.random()*24
            iterList.append(i+1)
            if random.random() < currentOdds:
                totalWin = totalWin + bet
                winningList.append(totalWin)
                totalEarnings = totalEarnings + bet
                earningList.append(totalEarnings)
                lossesList.append(totalLoss)
            else:
                totalLoss = totalLoss + bet
                lossesList.append(totalLoss)
                winningList.append(totalWin)
                totalEarnings = totalEarnings - bet
                earningList.append(totalEarnings)

        plot = Plotter()

        plot.linePlot(iterList, earningList, "Game Number","Total Earnings ($)","Earnings",1)
        plot.twoLinePlot(iterList, winningList, iterList, lossesList, "Game Number","Total ($)","Win Loss Graph",1)


# def main():
#     sim  = Simulation()
#     sim.simOnePlayerNGames([10,10,10],.25,100)

# if __name__ == '__main__':
#     main()