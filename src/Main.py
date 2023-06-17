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
    transformation=[45,4,1000,1,110,600]
    pygame.init()
    base_size = (XPIX, YPIX)
    current_size = (XPIX*10, YPIX*10)
    screen = pygame.display.set_mode(current_size)
    pygame.display.set_caption('Camera')
    dr.reDraw(cameraCoordinates,coordinates,screen,700,transformation)
    #screen = pygame.display.set_mode((450,450))
    run(cameraCoordinates,coordinates,screen,transformation)

def run(cameraCoordinates,coordinates,screen,transformation):
    running = True
    pygame.display.update()
    d=700
    while running:
        event = pygame.event.poll()
        d=li.keyListener(cameraCoordinates,coordinates,screen,d,transformation)

def main():
    coordinates = Readfile.getCoordinates()
    print(coordinates)
    cameraCoordinatesT=(150.0,150.0,0)
    projectionMAtrix=()
    cameraCoordinates=list(cameraCoordinatesT)
    start(coordinates,cameraCoordinates)

main()
