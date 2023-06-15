import pygame 
import Draw as dr
import MathOperation as mo

def keyListener(camera,coordinates,screen,d,transformation):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        transformation[1]=transformation[1]+1
        #coordinates=mo.moveCoordinates(coordinates,0,-1,0)
        dr.reDraw(camera,coordinates,screen,d,transformation)
    elif pressed[pygame.K_DOWN]:
        transformation[0]=transformation[0]+1
        #coordinates=mo.moveCoordinates(coordinates,0,1,0)
        dr.reDraw(camera,coordinates,screen,d,transformation)
    elif pressed[pygame.K_LEFT]:
        transformation[4]=transformation[4]+1
        #coordinates=mo.moveCoordinates(coordinates,-1,0,0)
        dr.reDraw(camera,coordinates,screen,d,transformation)
    elif pressed[pygame.K_RIGHT]:
        transformation[5]=transformation[5]+1
        #coordinates=mo.moveCoordinates(coordinates,+1,0,0)
        dr.reDraw(camera,coordinates,screen,d,transformation)
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