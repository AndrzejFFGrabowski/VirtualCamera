import numpy as np

def getCoordinates():
    array = np.ones((2,8,3))
    myfile = open("data/figure050f2.txt", "r")
    i=0
    k=0
    for line in myfile:
        tmp=line.split()
        j=0
        for x in tmp:
            print(x)
            array[k][i][j]=float(x)
            j = j+1
        i=i+1
        if(i==9):
            i=0
            k=k+1
    myfile.close()
    return array

