import Readfile
import Draw as dr
import Listener as li
import pygame
import MathOperation as mo
import os
from win32api import GetSystemMetrics
import BlockOperation as bo

XPIX, YPIX = 50, 50
Width = GetSystemMetrics(0)
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (Width/2-300, 100)

def start(coordinates,cameraCoordinates):
    transformation=[150,1,0.01,1000000,110,600]
    pygame.init()
    base_size = (XPIX, YPIX)
    current_size = (XPIX*10, YPIX*10)
    screen = pygame.display.set_mode(current_size)
    pygame.display.set_caption('Camera')
    dr.reDraw(cameraCoordinates,coordinates,screen,transformation,[0,0,300],[0,0,0])
    #screen = pygame.display.set_mode((450,450))
    run(cameraCoordinates,coordinates,screen,transformation)

def run(cameraCoordinates,coordinates,screen,transformation):
    running = True
    pygame.display.update()
    translation=[0,0,300]
    rotation=[0,0,0]
    while running:
        event = pygame.event.poll()
        translation,rotation=li.keyListener(cameraCoordinates,coordinates,screen,transformation,translation,rotation)

def main():
    coordinates = Readfile.getCoordinates()
    #print(coordinates)
    cameraCoordinatesT=(150.0,150.0,0)
    cameraCoordinates=list(cameraCoordinatesT)
    start(coordinates,cameraCoordinates)

main()
