import matplotlib.pyplot as plt
import numpy as np 


class Plotter:
    
    def __init__ (self) : 
        pass

    def __del__ (self) :
        pass

    def linePlot(self, xVals, yVals, xLabel, yLabel, newTitle, gridEnable):
        """Creates a line graph of xVals vs yVals"""
        
        fig, ax = plt.subplots()
        ax.plot(xVals, yVals)
        ax.set(xlabel = xLabel, ylabel = yLabel, title = newTitle)
        if gridEnable == 1:
            ax.grid()  

        plt.show() 

    def twoLinePlot(self, xValsOne, yValsOne, xValsTwo, yValsTwo, xLabel, yLabel, newTitle, gridEnable):
        """Creates a line graph of xValsOne vs yValsOne and xValsTwo vs yValsTwo on same plot"""
        
        fig, ax = plt.subplots()
        ax.plot(xValsOne, yValsOne)
        ax.plot(xValsTwo, yValsTwo)
        ax.set(xlabel = xLabel, ylabel = yLabel, title = newTitle)
        if gridEnable == 1:
            ax.grid()  

        plt.show() 

    def barChart(self, xVals, yVals, xLabel, yLabel, newTitle):
        """Creates a bar graph using x and y values"""

        fig, ax = plt.subplots()
        ax.bar(xVals,yVals)
        ax.set(xlabel = xLabel, ylabel = yLabel, title = newTitle)

        plt.show()

    def pieChart(self, data, newLabels, explode, newTitle):
        """Creates a pie chart of data with labels newLabes and title newTitle"""
        """Explode will seperate that potion away from the center"""
        """Ensure sum(data) >= 1, else black spaces will appear in chart"""

        fig, ax = plt.subplots()
        ax.pie(data, labels = newLabels, explode = explode)
        ax.set(title = newTitle)
        plt.show()
