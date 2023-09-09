import pygame
import MathOperation as mo
import BlockOperation as bo
import Readfile as rf

screen_color = (250, 250, 250)
line_color=(0,0,0)

def drawBackground(surface):
    surface.fill(screen_color)
    pygame.display.flip()

def drawFigures(figure,surface,transformation, translation,rotation):
    for i in figure:
        drawFigure(i,surface,transformation, translation,rotation)

def drawFigure(figure,surface,transformation, translation,rotation):
    figure2d, depth=bo.flatten(figure,transformation, translation,rotation)
    figure2d=bo.align(figure2d)
    if(mo.checkDistance(figure2d[0],figure2d[1],depth[0],depth[1])):pygame.draw.line(surface,line_color,figure2d[0],figure2d[1])
    if(mo.checkDistance(figure2d[0],figure2d[2],depth[0],depth[2])):pygame.draw.line(surface,line_color,figure2d[0],figure2d[2])
    if(mo.checkDistance(figure2d[0],figure2d[6],depth[0],depth[6])):pygame.draw.line(surface,line_color,figure2d[0],figure2d[6])
    if(mo.checkDistance(figure2d[1],figure2d[3],depth[1],depth[3])):pygame.draw.line(surface,line_color,figure2d[1],figure2d[3])
    if(mo.checkDistance(figure2d[1],figure2d[7],depth[1],depth[7])):pygame.draw.line(surface,line_color,figure2d[1],figure2d[7])
    if(mo.checkDistance(figure2d[2],figure2d[3],depth[2],depth[3])):pygame.draw.line(surface,line_color,figure2d[2],figure2d[3])
    if(mo.checkDistance(figure2d[2],figure2d[4],depth[2],depth[4])):pygame.draw.line(surface,line_color,figure2d[2],figure2d[4])
    if(mo.checkDistance(figure2d[3],figure2d[5],depth[3],depth[5])):pygame.draw.line(surface,line_color,figure2d[3],figure2d[5])
    if(mo.checkDistance(figure2d[4],figure2d[5],depth[4],depth[5])):pygame.draw.line(surface,line_color,figure2d[4],figure2d[5])
    if(mo.checkDistance(figure2d[4],figure2d[6],depth[4],depth[6])):pygame.draw.line(surface,line_color,figure2d[4],figure2d[6])
    if(mo.checkDistance(figure2d[5],figure2d[7],depth[5],depth[7])):pygame.draw.line(surface,line_color,figure2d[5],figure2d[7])
    if(mo.checkDistance(figure2d[6],figure2d[7],depth[6],depth[7])):pygame.draw.line(surface,line_color,figure2d[6],figure2d[7])


def reDraw(camera,coordinates,screen,transformation, translation,rotation):
    drawBackground(screen)
    drawFigures(coordinates,screen,transformation, translation,rotation)