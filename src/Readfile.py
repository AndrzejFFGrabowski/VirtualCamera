import numpy as np

def getCoordinates():
    array = np.ones((8,3)) 
    myfile = open("data/figure050.txt", "r")
    i=0
    for line in myfile:
        tmp=line.split()
        j=0
        for x in tmp:
            print(x)
            array[i][j]=float(x)
            j = j+1
        i=i+1
    myfile.close()
    return array

