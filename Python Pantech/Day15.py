"""
Matplotlib:
    -It is one of the popular packages used for data visualization.
    -It is a cross-platform library for making 2D plots from data in arrays.
    -It's written in python & make use of Numpy
    -It provides an object-oriented API.
    -Matplotlib packages are available in the form of pacakges on the std python package repositories.
    -It can be installed on windows and linux using pip package installer.
    -Matplotlib can be installed using the follwing command:<pip3 install matplotlib>
    -It is a visualization library available for 2D plots of arrays.
"""
"""
Matplotlib-PYPLOTAPI:
    -A new untitled notebook with .ipynb extension is displayed.
    -Matplotlib.pyplot is a collection of command style functions that make matplotlib work like matlab.
    -Pyplot functions are used for making some changes in the figure.
    -A function creates a figure,plots lines in the plotting area and decorates the plots.
    -Several kinds of plots are:line,bar,scatter,histogram,pie,barh,boxPlot,Hist,Hist2D,plot,polar
"""
"""
Matplotlib-PYLAB module:
    -Pylab is a procedural interface to the Matplotlib-object oriented plotting library.
    -Matplotlib is the whole package and matplotlib.pyplot is a module in matplotlib.
    -Pylab is a module and it gets installed alongside matplotlib.
"""
from matplotlib import pyplot as plt
x=[5,2,9,4,7]
y=[10,5,8,4,2]
# plt.plot(x,y)
# plt.show()

# plt.bar(x,y)
# plt.show()

# plt.scatter(x,y)
# plt.show()


# import numpy as np
# import math
# i=np.arange(0,math.pi*2,0.5)
# j=np.sin(i)
# plt.plot(i,j)
# plt.xlabel("angle")
# plt.ylabel("sine")
# plt.title('sine wave')
# plt.show()

# from numpy import *
# from pylab import *
# x=linspace(-3,3,30)
# y=x**2
# # plot(x,y)
# # plot(x,y,'r.')
# # plot(x,y,'b-')
# plot(x,y,'g--')
# show()

from pylab import *
i=linspace(-3,3,30)
plot(x,sin(x))
plot(x,cos(x),'r-')
plot(x,-sin(x),'g--')
show()