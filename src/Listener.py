import pygame 
import Draw as dr
import MathOperation as mo

translationV=0.5
rotationV=0.01

def keyListener(coordinates,screen,transformation,translation,rotation):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        translation[1] = translation[1] + translationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_DOWN]:
        translation[1] = translation[1] - translationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_LEFT]:
        translation[0] = translation[0] + translationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_RIGHT]:
        translation[0] = translation[0] - translationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_a]:
        translation[2] = translation[2] + translationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_d]:
        translation[2] = translation[2] - translationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_z]:
        rotation[0]=rotation[0]+rotationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_x]:
        rotation[0]=rotation[0]-rotationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_q]:
        rotation[1]=rotation[1]-rotationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_e]:
        rotation[1]=rotation[1]+rotationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_c]:
        rotation[2]=rotation[2]-rotationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    elif pressed[pygame.K_v]:
        rotation[2]=rotation[2]+rotationV
        dr.reDraw(coordinates,screen,transformation,translation,rotation)
    pygame.display.flip()
    pygame.display.update()
    return translation,rotation