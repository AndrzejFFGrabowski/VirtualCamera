import MathOperation as mo
import numpy as np

def flatten(figure3d,d,transformation):
    transformationValues=[45,4,3,1,100,10]
    projectionMatrix = createProjectiveMatrix(transformation[0],transformation[1],transformation[2],transformation[3],transformation[4],transformation[5])
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

def projectMatrix(projectionMatrix,coordinates):
    copy=coordinates
    for block in copy:
        for coordinate in block:
            coordinate=np.matmul(projectionMatrix,coordinate)
    return copy


def createProjectiveMatrix(bottom,top,far,near,left,right):
    width = 100
    height= 100
    z = 500
    Matrix=[((width/(right-left)),(0),(0),((-left*width)/(right-left))),
            ((),(height/(bottom-top)),(),((-top*height/bottom-top))),
            ((),(),(z/(far-near)),(-near*z/(far-near))),
            ((),(),(),(1)),
    ]
    return Matrix

