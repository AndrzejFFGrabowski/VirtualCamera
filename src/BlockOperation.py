import MathOperation as mo
import numpy as np
import math

def flatten(figure3d,d,transformation, ta, tb, tc):
    print("in flatten = ",figure3d)
    projectionMatrix = createProjectiveMatrix(transformation[0],transformation[1],transformation[2],transformation[3],transformation[4],transformation[5])
    cameraMatrix = createCameraMatrix(ta,tb,tc)
    transformationMatrix = np.matmul(cameraMatrix, projectionMatrix)
    figure4d=mo.asHomogenous(figure3d)
    figure2d= np.ones((len(figure4d),2)) 
    for i in range (len(figure4d)):
        vec = np.matmul(transformationMatrix, figure4d[i])
        figure4d[i] = vec / vec[3]
        figure2d[i][0] = figure4d[i][0]
        figure2d[i][1] = figure4d[i][1]
    print(figure4d)
    return figure2d

def alignCamera(camera,coordinates):
    copy=coordinates
    for tmp in copy:
        for i in range(len(coordinates)):
            for j in range(3):
                tmp[i,j]+=camera[j]
    return copy

def align(coordinates):
    offset = [250,250]
    for x in coordinates:
        x[0]=(x[0]*50+offset[0])
        x[1]=(x[1]*50+offset[1])
    return coordinates

def projectMatrix(projectionMatrix,coordinates):
    copy=coordinates
    for block in copy:
        for coordinate in block:
            coordinate=np.matmul(projectionMatrix,coordinate)
    return copy


def createProjectiveMatrix(fov,aspect,znear,zfar,left,right):
    width = 100
    height= 100
    aspect=height/width
    Matrix=[(((1/(aspect*math.tan(fov/2)))),(0),(0),(0)),
            ((0),(1/math.tan(fov/2)),(0),(0)),
            ((0),(0),-((zfar+znear)/(zfar-znear)),((-2*zfar*znear)/(zfar-znear))),
            ((0),(0),(-1),(0)),
    ]
    return Matrix

def createCameraMatrix(ta,tb,tc):
    Matrix=[((1),(0),(0),(ta)),
            ((0),(1),(0),(tb)),
            ((0),(0),(1),(tc)),
            ((0),(0),(0),(1)),
    ]
    
    return Matrix

