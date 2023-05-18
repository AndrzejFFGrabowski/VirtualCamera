import pygame 
import Draw as dr
import MathOperation as mo

def keyListener(camera,coordinates,screen,d):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        coordinates=mo.moveCoordinates(coordinates,0,-1,0)
        dr.reDraw(camera,coordinates,screen,d)
    elif pressed[pygame.K_DOWN]:
        coordinates=mo.moveCoordinates(coordinates,0,1,0)
        dr.reDraw(camera,coordinates,screen,d)
    elif pressed[pygame.K_LEFT]:
        coordinates=mo.moveCoordinates(coordinates,-1,0,0)
        dr.reDraw(camera,coordinates,screen,d)
    elif pressed[pygame.K_RIGHT]:
        coordinates=mo.moveCoordinates(coordinates,+1,0,0)
        dr.reDraw(camera,coordinates,screen,d)
    elif pressed[pygame.K_a]:
        coordinates=mo.moveCoordinates(coordinates,0,0,-1)
        dr.reDraw(camera,coordinates,screen,d)
    elif pressed[pygame.K_d]:
        coordinates=mo.moveCoordinates(coordinates,0,0,1)
        dr.reDraw(camera,coordinates,screen,d)
    elif pressed[pygame.K_z]:
        d=d-1
        dr.reDraw(camera,coordinates,screen,d)
    elif pressed[pygame.K_x]:
        d=d+1
        dr.reDraw(camera,coordinates,screen,d)
    elif pressed[pygame.K_q]:
        print('left')
    elif pressed[pygame.K_e]:
        print('right')
    pygame.display.flip()
    pygame.display.update()
    return d