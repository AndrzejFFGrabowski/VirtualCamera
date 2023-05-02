import pygame
import MathOperation as mo
import BlockOperation as bo

def drawBackground(surface):
    screen_color = (250, 250, 250)
    surface.fill(screen_color)
    pygame.display.flip()

def drawFigures(figures,surface):
    for figure in figures:
        drawFigure(figure,surface)

def drawFigure(figure,surface):
    line_color=(0,0,0)
    figure2d=bo.flatten(figure)
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


def reDraw(camera,coordinates,screen):
    drawBackground(screen)
    drawFigure(coordinates,screen)
        #bo.alignCamera(camera,coordinates),screen)


def firstDraw(camera,coordinates,screen):
    drawBackground(screen)
    drawFigure(bo.alignCamera(camera,coordinates),screen)