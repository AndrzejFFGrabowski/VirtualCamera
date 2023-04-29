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

def run(coordinates,cameraCoordinates):
    pygame.init()
    base_size = (XPIX, YPIX)
    current_size = (XPIX*9, YPIX*9)
    screen = pygame.display.set_mode(current_size)
    pygame.display.set_caption('Camera')
    dr.drawBackground(screen)
    dr.drawFigure(coordinates,screen)
    #screen = pygame.display.set_mode((450,450))
    running = True
    pygame.display.update()
    while running:
        event = pygame.event.poll()
        keyListener(cameraCoordinates,coordinates,screen)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            coordinates=mo.moveCoordinates(coordinates,0,-1,0)
            dr.drawBackground(screen)
            dr.drawFigure(coordinates,screen)
        elif pressed[pygame.K_DOWN]:
            dr.drawBackground(screen)
            coordinates=mo.moveCoordinates(coordinates,0,1,0)
            dr.drawFigure(coordinates,screen)
            print(coordinates)
        elif pressed[pygame.K_LEFT]:
            coordinates=mo.moveCoordinates(coordinates,-1,0,0)
            dr.drawBackground(screen)
            dr.drawFigure(coordinates,screen)
        elif pressed[pygame.K_RIGHT]:
            coordinates=mo.moveCoordinates(coordinates,+1,0,0)
            dr.drawBackground(screen)
            dr.drawFigure(coordinates,screen)
        elif pressed[pygame.K_a]:
            coordinates=mo.moveCoordinates(coordinates,0,0,-1)
            dr.drawBackground(screen)
            dr.drawFigure(coordinates,screen)
        elif pressed[pygame.K_d]:
            coordinates=mo.moveCoordinates(coordinates,0,0,1)
            dr.drawBackground(screen)
            dr.drawFigure(coordinates,screen)
        pygame.display.flip()
        pygame.display.update()

def keyListener(cameraCoordinates,coordinates,surface): 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        cameraCoordinates[0]=cameraCoordinates[0]+1
        cameraCoordinates[1]=cameraCoordinates[1]-1
        update(cameraCoordinates,coordinates,surface)
    elif pressed[pygame.K_DOWN]:
        cameraCoordinates[0]=cameraCoordinates[0]-1
        cameraCoordinates[1]=cameraCoordinates[1]+1
        update(cameraCoordinates,coordinates,surface)
    elif pressed[pygame.K_LEFT]:
        cameraCoordinates[0]=cameraCoordinates[0]-1
        cameraCoordinates[1]=cameraCoordinates[1]-1
        update(cameraCoordinates,coordinates,surface)
    elif pressed[pygame.K_RIGHT]:
        cameraCoordinates[0]=cameraCoordinates[0]+1
        cameraCoordinates[1]=cameraCoordinates[1]+1
        update(cameraCoordinates,coordinates,surface)

def update(cameraCoordinates,coordinates,surface):
    coordinates[0]=coordinates[0]+cameraCoordinates[0]
    coordinates[1]=coordinates[1]+cameraCoordinates[1]
    dr.drawFigure(coordinates,surface)
    pygame.display.update()

def main():
    coordinates = Readfile.getCoordinates()
    print(coordinates)
    cameraCoordinatesT=(0,0)
    cameraCoordinates=list(cameraCoordinatesT)
    run(coordinates,cameraCoordinates)
    


main()
