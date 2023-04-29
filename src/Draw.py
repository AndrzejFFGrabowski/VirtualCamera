import pygame
import MathOperation as mo

def drawBackground(surface):
    screen_color = (250, 250, 250)
    surface.fill(screen_color)
    pygame.display.flip()

def drawFigures(figures,surface):
    for figure in figures:
        drawFigure(figure,surface)

def drawFigure(figure,surface):
    line_color=(0,0,0)
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[0]),mo.point3Dto2D(figure[1]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[0]),mo.point3Dto2D(figure[2]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[0]),mo.point3Dto2D(figure[6]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[1]),mo.point3Dto2D(figure[3]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[1]),mo.point3Dto2D(figure[7]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[2]),mo.point3Dto2D(figure[3]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[2]),mo.point3Dto2D(figure[4]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[3]),mo.point3Dto2D(figure[5]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[4]),mo.point3Dto2D(figure[5]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[4]),mo.point3Dto2D(figure[6]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[5]),mo.point3Dto2D(figure[7]))
    pygame.draw.line(surface,line_color,mo.point3Dto2D(figure[6]),mo.point3Dto2D(figure[7]))