import math

def point3Dto2D(point3D):
    point2D=[float((point3D[0]+1)/(point3D[2]+1)),float((point3D[1]+1)/(point3D[2]+1))]
    #print(point2D)
    return point2D

def moveCoordinates(coordinates,x,y,z):
    for i in coordinates:
        i[0]=i[0]+x
        i[1]=i[1]+y
        i[2]=i[2]+z
    return coordinates
