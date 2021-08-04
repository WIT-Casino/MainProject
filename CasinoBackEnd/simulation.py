from random import seed
from random import random

class Simulation:
    def __init__ (self) : 
        pass

    def __del__ (self) :
        pass

    def simOnePlayerOneGame(self, player, game):
        currentOdds = .25 + player.luck * .02 + player.skill * .04
        seed(currentOdds)
        totalEarnings = 0
        winnings = 0
        bet = random(1,25)
        losses = 0
        if random() < currentOdds:
            winnings = winnings + bet
        else:
            losses = losses + bet

        winnings = winnings - losses

    def simOnePlayerNGames(self, player, game, numberOfGames):
        
        if game == 1:
            currentOdds = .25 + player.luck * .02 + player.skill * .04
        elif game == 2:
            currentOdds = .40 + player.luck * .01 + player.skill * .02
        elif game == 3:
            currentOdds = .30 + player.luck * .015 + player.skill * .03

        seed(currentOdds)

        earningList = list(0)
        earningList.clear()
        winningList = list(0)
        winningList.clear()        
        losses = list(0)
        losses.clear()
        iterList = list(0)
        iterList.clear()

        totalWin = 0
        totalLoss = 0
        totalEarnings = 0
        
        for i in range(numberOfGames):
            bet = random(1,25)
            iterList.append(i+1)
            if random() < currentOdds:
                totalWin = totalWin + bet
                winningList.append(totalWin)
                totalEarnings = totalEarnings + bet
                earningList.append(totalEarnings)
            else:
                totalLoss = totalLoss + bet
                lossesList.append(totalLoss)
                totalEarnings = totalEarnings - bet
                earningList.append(totalEarnings)

        plot = Plotter()

        plot.linePlot(iterList, earningList, "Game Number","Total Earnings ($)","Earnings",1)
        plot.twoLinePlot(iterList, winningList, iterList, lossesList, "Game Number","Total ($)","Win Loss Graph",1)
        