# plottask.py
# This program reads displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes.
# Author: Ciaran Moran

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4,1)                              # x-axis values, range is 0 to 4 in steps of 1
                                                  # y-axis:                                              
y1  =  x                                          # f(x)=x 
y2  =  x**2                                       # g(x)=x^2
y3  =  x**3                                       # h(x)=x^3

# Variables for plot 
xy1_Colour = 'red'
xy2_Colour = 'green'
xy3_Colour = 'blue'

xy1_linestype = 'dashed'
xy2_linestype = 'dashed'
xy3_linestype = 'dashed'

xy1_label = 'f(x)=x'
xy2_label = 'g(x)=x^2'
xy3_label = 'h(x)=x^3'

xAxisLabel = 'x - axis'
yAxisLabel = 'y - axis'
xAxisFontSize = 12
yAxisFontSize = 12

plotAreaColour = "lightgrey"

ax = plt.axes()


def customPlot(ax = None):
   # declare plot series characteristics
    plt.plot(x, y1, color = xy1_Colour, linestyle = xy1_linestype, label = xy1_label)
    plt.plot(x, y2, color = xy2_Colour, linestyle = xy2_linestype, label = xy2_label)
    plt.plot(x, y3, color = xy3_Colour, linestyle = xy3_linestype, label = xy3_label)

    ## declare axis labels
    plt.xlabel(xAxisLabel, fontsize = xAxisFontSize)
    plt.ylabel(yAxisLabel, fontsize = yAxisFontSize)

    # plot legend and grid 
    plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",mode="expand", borderaxespad=0, ncol=3, fontsize = 14)
    plt.grid(True,which="both", linestyle='--')

    # set plot area colour
    ax = plt.axes()
    ax.set_facecolor(plotAreaColour)

    return plt


def writePlot(writePlot):
    plt.savefig('plottask.png')
    plt.show()
    

myPlot = customPlot()
writePlot(myPlot)
































# np.arrange :  https://realpython.com/how-to-use-numpy-arange/
# plt.plot : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# title format: https://stackoverflow.com/questions/18962063/matplotlib-setting-title-bold-while-using-times-new-roman
# legend format : https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot#:~:text=To%20place%20the%20legend%20outside,left%20corner%20of%20the%20legend.&text=A%20more%20versatile%20approach%20is,placed%2C%20using%20the%20bbox_to_anchor%20argument.
# grid format: https://moonbooks.org/Articles/How-to-add-a-grid-on-a-figure-in-matplotlib-/
# background colour format: https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color
# save file to directiory : https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory
# axis problem solves:  https://stackoverflow.com/questions/55186273/warning-adding-an-axes-using-the-same-arguments-and-custom-plot-function