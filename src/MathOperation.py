import math
import numpy as np

maxDistance = 750

def asHomogenous(figure3d):
    figure4d= np.ones((len(figure3d),4))
    for i in range(len(figure3d)):
        figure4d[i][0]=figure3d[i][0]
        figure4d[i][1]=figure3d[i][1]
        figure4d[i][2]=figure3d[i][2]
        figure4d[i][3]=1
    return figure4d

def checkDistance(pointA,pointB,depthA,depthB):
    if(depthA<1 or depthB<1):
        return False
    distance=math.sqrt((pointA[0]-pointB[0])*(pointA[0]-pointB[0])+(pointA[1]-pointB[1])*(pointA[1]-pointB[1]))
    if(distance<maxDistance):
        return True
    return False