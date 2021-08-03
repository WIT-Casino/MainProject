import random
from plotter import Plotter
import time

class Simulation:
    def __init__ (self) : 
        pass

    def __del__ (self) :
        pass

    def simOnePlayerOneGame(self, player, game):
        currentOdds = .25 + player.luck * .02 + player.skill * .04
        random.seed(time.time())
        totalEarnings = 0
        winnings = 0
        bet = random(1,25)
        losses = 0
        if random.random() < currentOdds:
            winnings = winnings + bet
        else:
            losses = losses + bet

        winnings = winnings - losses

    def simOnePlayerNGames(self, player, winrate, numberOfGames):
        # player = [skill, luck, cheat]
        
        currentOdds = winrate + player[1] * .01 + player[2] * .04 + player[0] * .02
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


def main():
    sim  = Simulation()
    sim.simOnePlayerNGames([10,0,0],.35,100)

if __name__ == '__main__':
    main()
        