import MathOperation as mo
import numpy as np

def flatten(figure3d):
    figure2d= np.ones((len(figure3d),2)) 
    for i in range (len(figure3d)):
        figure2d[i]=mo.section(figure3d[i])
    return figure2d

def alignCamera(camera,coordinates):
    copy=coordinates
    for i in range(len(coordinates)):
        for j in range(3):
            copy[i,j]+=camera[j]
    return copy