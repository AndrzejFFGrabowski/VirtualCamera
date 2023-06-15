import pygame
import MathOperation as mo
import BlockOperation as bo

def drawBackground(surface):
    screen_color = (250, 250, 250)
    surface.fill(screen_color)
    pygame.display.flip()

def drawFigures(figure,surface,d,transformation):
    for i in figure:
        drawFigure(i,surface,d,transformation)

def drawFigure(figure,surface,d,transformation):
    line_color=(0,0,0)
    figure2d=bo.flatten(figure,d,transformation)
    pygame.draw.line(surface,line_color,figure2d[0],figure2d[1])
    pygame.draw.line(surface,line_color,figure2d[0],figure2d[2])
    pygame.draw.line(surface,line_color,figure2d[0],figure2d[6])
    pygame.draw.line(surface,line_color,figure2d[1],figure2d[3])
    pygame.draw.line(surface,line_color,figure2d[1],figure2d[7])
    pygame.draw.line(surface,line_color,figure2d[2],figure2d[3])
    pygame.draw.line(surface,line_color,figure2d[2],figure2d[4])
    pygame.draw.line(surface,line_color,figure2d[3],figure2d[5])
    pygame.draw.line(surface,line_color,figure2d[4],figure2d[5])
    pygame.draw.line(surface,line_color,figure2d[4],figure2d[6])
    pygame.draw.line(surface,line_color,figure2d[5],figure2d[7])
    pygame.draw.line(surface,line_color,figure2d[6],figure2d[7])


def reDraw(camera,coordinates,screen,d,transformation):
    drawBackground(screen)
    drawFigures(coordinates,screen,d,transformation)
        #bo.alignCamera(camera,coordinates),screen)


def firstDraw(camera,coordinates,screen,d):
    drawBackground(screen)
    drawFigures(bo.alignCamera(camera,coordinates),screen,d)