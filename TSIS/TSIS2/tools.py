import pygame
import math

def draw_pencil(surface, start, end, color, size):
    pygame.draw.line(surface, color, start, end, size)

def draw_line(surface, start, end, color, size):
    pygame.draw.line(surface, color, start, end, size)

def draw_rect(surface, start, end, color, size):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2),
                       abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(surface, color, rect, size)

def draw_circle(surface, start, end, color, size):
    radius = int(math.dist(start, end))
    pygame.draw.circle(surface, color, start, radius, size)

def draw_square(surface, start, end, color, size):
    x1, y1 = start
    x2, y2 = end
    side = max(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, side, side)
    pygame.draw.rect(surface, color, rect, size)

def draw_right_triangle(surface, start, end, color, size):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(surface, color, [(x1,y1),(x1,y2),(x2,y2)], size)

def draw_equilateral_triangle(surface, start, end, color, size):
    x1, y1 = start
    x2, _ = end
    side = abs(x2 - x1)
    h = int(math.sqrt(3)/2 * side)
    pygame.draw.polygon(surface, color, [(x1,y1),(x2,y1),((x1+x2)//2,y1-h)], size)

def draw_rhombus(surface, start, end, color, size):
    x1,y1=start
    x2,y2=end
    cx,cy=(x1+x2)//2,(y1+y2)//2
    pygame.draw.polygon(surface,color,[(cx,y1),(x2,cy),(cx,y2),(x1,cy)],size)

def erase(surface, start, end, size):
    pygame.draw.line(surface, (255,255,255), start, end, size)

def draw_text(surface, font, text, pos, color):
    surface.blit(font.render(text,True,color),pos)

def draw_text_preview(surface, font, text, pos, color):
    surface.blit(font.render(text,True,color),pos)