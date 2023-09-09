import MathOperation as mo
import numpy as np
import math

def flatten(figure,transformation, translation,rotation):
    projectionMatrix = createProjectiveMatrix(transformation[0],transformation[1],transformation[2])
    cameraMatrix = createCameraMatrix(translation,rotation)
    np.linalg.inv(cameraMatrix)
    transformationMatrix= np.matmul(projectionMatrix,cameraMatrix)
    figure4d=mo.asHomogenous(figure)
    figure2d= np.ones((len(figure4d),2)) 
    depth = np.ones(len(figure4d))
    for i in range (len(figure4d)):
        vec = np.matmul(transformationMatrix, figure4d[i])
        figure4d[i] = vec / vec[3]
        figure2d[i][0] = figure4d[i][0]
        figure2d[i][1] = figure4d[i][1]
        depth[i] = figure4d[i][2]
    return figure2d, depth

def align(coordinates):
    offset = [250,250]
    for x in coordinates:
        x[0]=(x[0]*50+offset[0])
        x[1]=(x[1]*50+offset[1])
    return coordinates

def createProjectiveMatrix(fov,znear,zfar):
    width = 100
    height= 100
    aspect=height/width
    Matrix=[(((1/(aspect*math.tan(fov/2)))),(0),(0),(0)),
            ((0),(1/math.tan(fov/2)),(0),(0)),
            ((0),(0),-((zfar+znear)/(zfar-znear)),((-2*zfar*znear)/(zfar-znear))),
            ((0),(0),(-1),(0)),
    ]
    return Matrix

def createCameraMatrix(translation,rotation):
    Matrix=[((1),(0),(0),(translation[0])),
            ((0),(1),(0),(translation[1])),
            ((0),(0),(1),(translation[2])),
            ((0),(0),(0),(1)),
    ]
    return createRotationMatrix(Matrix,rotation)

def createRotationMatrix(Matrix,rotation):
    Xaxis=[((1),(0),(0),(0)),
            ((0),(math.cos(rotation[0])),(-math.sin(rotation[0])),(0)),
            ((0),(math.sin(rotation[0])),(math.cos(rotation[0])),(0)),
            ((0),(0),(0),(1)),
    ]
    
    Yaxis=[((math.cos(rotation[1])),(0),(math.sin(rotation[1])),0),
            ((0),(1),(0),(0)),
            ((-math.sin(rotation[1])),(0),(math.cos(rotation[1])),0),
            ((0),(0),(0),(1)),
    ]
    Zaxis=[((math.cos(rotation[2])),(-math.sin(rotation[2])),(0),0),
            ((math.sin(rotation[2])),(math.cos(rotation[2])),(0),0),
            ((0),(0),(1),(0)),
            ((0),(0),(0),(1)),
    ]

    MatrixCamera=np.matmul(Xaxis,Matrix)
    MatrixCamera=np.matmul(Yaxis,MatrixCamera)
    MatrixCamera=np.matmul(Zaxis,MatrixCamera)
    return MatrixCamera
    