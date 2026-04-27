import pygame
from datetime import datetime

def save_canvas(surface):
    name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pygame.image.save(surface, f"save_{name}.png")

def flood_fill(surface, x, y, target, repl):
    if target == repl:
        return
    w,h=surface.get_size()
    stack=[(x,y)]

    while stack:
        cx,cy=stack.pop()
        if cx<0 or cy<0 or cx>=w or cy>=h:
            continue
        if surface.get_at((cx,cy))[:3]!=target:
            continue
        surface.set_at((cx,cy),repl)
        stack+=[(cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)]

def set_brush_size(key,current):
    if key==pygame.K_1:return 2
    if key==pygame.K_2:return 5
    if key==pygame.K_3:return 10
    return current