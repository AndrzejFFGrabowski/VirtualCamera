import MathOperation as mo
import numpy as np

def flatten(figure3d,d):
    figure2d= np.ones((len(figure3d),2)) 
    for i in range (len(figure3d)):
        figure2d[i]=mo.section(figure3d[i],d)
    return figure2d

def alignCamera(camera,coordinates):
    copy=coordinates
    for tmp in copy:
        for i in range(len(coordinates)):
            for j in range(3):
                tmp[i,j]+=camera[j]
    return copy