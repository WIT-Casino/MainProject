import random
import time
import sys

try:
    sys.path.append(".")
    from CasinoBackEnd.plotter import Plotter
    
        
except ModuleNotFoundError:
    sys.path.append("..")
    from CasinoBackEnd.plotter import Plotter

from Games.blackjack import blackjack
from Games.Keno import Keno
from Games.Roulette_sim import Roulette
from Games.slotmachine import slots
from Games.craps import craps
from CasinoBackEnd.gamedata import GamePrefixID



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
        plot.show_graphs()


    def simRealGame(self, gameType):
        random.seed(time.time())

        earningList = list([])
        earningList.clear()
        winningList = list([])
        winningList.clear()        
        lossesList = list([])
        lossesList.clear()
        numGameList = list([])
        numGameList.clear()
        #monthList = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        monthList = list([])
        

        
        for i in range(12):
            totalWin = 0
            totalLoss = 0
            totalEarnings = 0
            gameOutCome = 0
            numberOfGames = random.randint(50,100)
            for j in range(numberOfGames):
                bet = 1 + random.random()*24
                if gameType == GamePrefixID.BlackJack:
                    gameOutCome = blackjack()
                elif gameType == GamePrefixID.Craps:
                    gameOutCome = craps()
                elif gameType == GamePrefixID.Roulette:
                    gameOutCome = Roulette()
                elif gameType == GamePrefixID.Slots:
                    gameOutCome = slots()
                elif gameType == GamePrefixID.Keno:
                    gameOutCome = Keno()
        
                if gameOutCome == 1:
                    totalWin = totalWin + bet
                    #winningList.append(totalWin)
                    totalEarnings = totalEarnings + bet
                    #earningList.append(totalEarnings)
                    #lossesList.append(totalLoss)
                else:
                    totalLoss = totalLoss + bet
                    #lossesList.append(totalLoss)
                    #winningList.append(totalWin)
                    totalEarnings = totalEarnings - bet
                    #earningList.append(totalEarnings)
            
            earningList.append(totalEarnings)
            lossesList.append(totalLoss)
            winningList.append(totalWin)
            numGameList.append(numberOfGames)
            monthList.append(i)

        plot = Plotter()

        plot.barChart(monthList, numGameList, "Month","Number of Games Player","Popularity")
        #plot.linePlot(monthList, winningList, "Game Number","Total Earnings ($)","Earnings",1)
        plot.twoLinePlot(monthList, winningList, monthList, lossesList, "Game Number","Total ($)","Win Loss Graph",1)
        plot.show_graphs()


# def main():
#     sim  = Simulation()
#     sim.simRealGame(3)

# if __name__ == '__main__':
#     main()