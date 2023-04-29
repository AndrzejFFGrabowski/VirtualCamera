import pygame 
import Draw as dr

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
        coordinates=mo.moveCoordinates(coordinates,-1,0)
#        update(cameraCoordinates,coordinates,surface)


def update(cameraCoordinates,coordinates,surface):
    coordinates[0]=coordinates[0]+cameraCoordinates[0]
    coordinates[1]=coordinates[1]+cameraCoordinates[1]
    dr.drawFigure(coordinates,surface)
    pygame.display.update()