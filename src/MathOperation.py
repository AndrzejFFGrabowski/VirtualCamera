import math

def point3Dto2D(point3D):
    point2D=[float((point3D[0]+1)/(point3D[2]+1)),float((point3D[1]+1)/(point3D[2]+1))]
    #print(point2D)
    return point2D

def moveCoordinates(coordinates,x,y,z):
    for j in coordinates:
        for i in j:
            i[0]=i[0]+x
            i[1]=i[1]+y
            i[2]=i[2]+z
    return coordinates

def section(point3D,d):
    #d=700
    if(((point3D[2]/d)+1)==0):
        print("index 2 div/0")
    point2D=[float((point3D[0])/((point3D[2]/d)+1)),float((point3D[1])/((point3D[2]/d)+1))]
    #return point2D
    return canvas(point2D[0],point2D[1])


def canvas(x, y):
    Vw=400
    Vh=400
    Cw=500
    Ch=500
    return (x * Cw/Vw, y * Ch/Vh)
