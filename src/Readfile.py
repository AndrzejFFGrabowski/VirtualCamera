import numpy as np
import pygame 

def getCoordinates():
    array = np.ones((8,8,3))
    myfile = open("data/figure050f2.txt", "r")
    #myfile  = open("data/figure1.txt", "r")
    i=0
    k=0
    for line in myfile:
        tmp=line.split()
        j=0
        for x in tmp:
            #print(x)
            array[k][i][j]=float(x)
            j = j+1
        i=i+1
        if(i==9):
            i=0
            k=k+1
    myfile.close()
    return array

def addImage(surface):
    imp = pygame.image.load("data/Axis1.png").convert()
    surface.blit(imp,(0,0))