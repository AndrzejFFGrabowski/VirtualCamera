import MathOperation as mo
import numpy as np

def flatten(figure3d):
    figure2d= np.ones((8,2)) 
    for i in range (8):
        figure2d[i]=mo.section(figure3d[i])
        print (i, " is ",figure2d[i])
    return figure2d
