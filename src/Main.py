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

def start(coordinates):
    transformation=[150,0.01,1000000]
    pygame.init()
    current_size = (XPIX*10, YPIX*10)
    screen = pygame.display.set_mode(current_size)
    pygame.display.set_caption('Camera')
    dr.reDraw(coordinates,screen,transformation,[0,0,300],[0,0,0])
    run(coordinates,screen,transformation)

def run(coordinates,screen,transformation):
    running = True
    pygame.display.update()
    translation=[0,0,300]
    rotation=[0,0,0]
    while running:
        event = pygame.event.poll()
        translation,rotation=li.keyListener(coordinates,screen,transformation,translation,rotation)

def main():
    coordinates = Readfile.getCoordinates()
    start(coordinates)

main()
