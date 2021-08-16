import matplotlib.pyplot as plt
import numpy as np 


class Plotter:
    
    def __init__ (self) : 
        pass

    def __del__ (self) :
        pass

    def show_graphs(self):
        plt.show()


    def linePlot(self, xVals, yVals, xLabel, yLabel, newTitle, gridEnable):
        """Creates a line graph of xVals vs yVals"""
        
        _, ax = plt.subplots()
        ax.plot(xVals, yVals)
        ax.set(xlabel = xLabel, ylabel = yLabel, title = newTitle)
        if gridEnable == 1:
            ax.grid()  
        plt.ticklabel_format(style = 'plain')
        

        

    def twoLinePlot(self, xValsOne, yValsOne, xValsTwo, yValsTwo, xLabel, yLabel, newTitle, gridEnable):
        """Creates a line graph of xValsOne vs yValsOne and xValsTwo vs yValsTwo on same plot"""
        
        _, ax = plt.subplots()
        ax.plot(xValsOne, yValsOne, label="Won Amount" )
        ax.plot(xValsTwo, yValsTwo, label="Loss Amount")
        ax.set(xlabel = xLabel, ylabel = yLabel, title = newTitle)
        if gridEnable == 1:
            ax.grid()  
        ax.legend(loc="upper left")
        plt.ticklabel_format(style = 'plain')
         

    def barChart(self, xVals, yVals, xLabel, yLabel, newTitle):
        """Creates a bar graph using x and y values"""

        _, ax = plt.subplots()
        ax.bar(xVals,yVals)
        ax.set(xlabel = xLabel, ylabel = yLabel, title = newTitle)

        

    def pieChart(self, data, newLabels, newTitle, explode=False):
        """Creates a pie chart of data with labels newLabes and title newTitle
            
            Explode will seperate that potion away from the center
            
            Ensure sum(data) >= 1, else black spaces will appear in chart"""

        if explode == False:
            explode = [0]*len(data)
        elif explode == True:
            explode = [0.1]*len(data)
        else:
            explode = explode
        def func(pct, allvalues):
            absolute = int(pct / 100.*np.sum(allvalues))
            return "{:.1f}%\n${:d} ".format(pct, absolute)
        _, ax = plt.subplots()
        ax.pie(data, labels = newLabels, explode = explode, autopct = lambda pct: func(pct, data))
        ax.set(title = newTitle)
        



