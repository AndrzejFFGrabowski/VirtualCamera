import Readfile
import Draw as dr
import Listener as li
import pygame
import MathOperation as mo
import os
from win32api import GetSystemMetrics

XPIX, YPIX = 50, 50
Width = GetSystemMetrics(0)
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (Width/2-300, 100)

def start(coordinates,cameraCoordinates):
    pygame.init()
    base_size = (XPIX, YPIX)
    current_size = (XPIX*9, YPIX*9)
    screen = pygame.display.set_mode(current_size)
    pygame.display.set_caption('Camera')
    dr.firstDraw(cameraCoordinates,coordinates,screen)
    #screen = pygame.display.set_mode((450,450))
    run(cameraCoordinates,coordinates,screen)

def run(cameraCoordinates,coordinates,screen):
    running = True
    pygame.display.update()
    while running:
        event = pygame.event.poll()
        li.keyListener(cameraCoordinates,coordinates,screen)

def main():
    coordinates = Readfile.getCoordinates()
    print(coordinates)
    cameraCoordinatesT=(250.0,250.0,0)
    cameraCoordinates=list(cameraCoordinatesT)
    start(coordinates,cameraCoordinates)

main()
