import pygame
import sys
from tools import *
from utils import save_canvas, flood_fill, set_brush_size

pygame.init()

# ---------------- WINDOW ----------------
WIDTH, HEIGHT = 1000, 700
UI_HEIGHT = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2 Paint")

canvas = pygame.Surface((WIDTH, HEIGHT - UI_HEIGHT))
canvas.fill((255, 255, 255))

overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

clock = pygame.time.Clock()

# ---------------- STATE ----------------
tool = "pencil"
color = (0, 0, 0)
brush_size = 2

prev_pos = None
start_pos = None
drawing_shape = False

# TEXT
text_input = ""
text_pos = None
typing = False
text_objects = []

font = pygame.font.SysFont("Arial", 24)

# ---------------- PALETTE ----------------
palette = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255)
]

palette_rects = []

# ---------------- LOOP ----------------
running = True

while running:
    screen.fill((220, 220, 220))
    overlay.fill((0, 0, 0, 0))

    # ---------------- PALETTE ----------------
    palette_rects = []
    x, y, size = 10, 10, 30

    for c in palette:
        rect = pygame.Rect(x, y, size, size)
        pygame.draw.rect(screen, c, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 1)
        palette_rects.append((rect, c))
        x += size + 5

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---------------- KEYBOARD ----------------
        if event.type == pygame.KEYDOWN:

            brush_size = set_brush_size(event.key, brush_size)

            if event.key == pygame.K_p:
                tool = "pencil"
            elif event.key == pygame.K_l:
                tool = "line"
            elif event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_y:
                tool = "right_triangle"
            elif event.key == pygame.K_u:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_h:
                tool = "rhombus"
            elif event.key == pygame.K_f:
                tool = "fill"
            elif event.key == pygame.K_t:
                tool = "text"

            # clear canvas
            if event.key == pygame.K_n:
                canvas.fill((255, 255, 255))

            # save
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas(canvas)

            # TEXT INPUT
            if tool == "text" and typing:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    text_objects.append((text_input, text_pos))
                    typing = False

                elif event.key == pygame.K_ESCAPE:
                    typing = False

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

        # ---------------- MOUSE DOWN ----------------
        if event.type == pygame.MOUSEBUTTONDOWN:

            for rect, c in palette_rects:
                if rect.collidepoint(event.pos):
                    color = c
                    break

            if event.pos[1] < UI_HEIGHT:
                continue

            mx, my = event.pos
            my -= UI_HEIGHT

            start_pos = (mx, my)
            drawing_shape = True

            if tool == "pencil":
                prev_pos = start_pos

            elif tool == "eraser":
                prev_pos = start_pos

            elif tool == "fill":
                x, y = start_pos
                target = canvas.get_at((x, y))[:3]
                flood_fill(canvas, x, y, target, color)

            elif tool == "text":
                text_pos = start_pos
                text_input = ""
                typing = True

        # ---------------- MOUSE UP ----------------
        if event.type == pygame.MOUSEBUTTONUP:

            mx, my = event.pos
            my -= UI_HEIGHT
            end_pos = (mx, my)

            if tool == "line":
                draw_line(canvas, start_pos, end_pos, color, brush_size)

            elif tool == "rect":
                draw_rect(canvas, start_pos, end_pos, color, brush_size)

            elif tool == "circle":
                draw_circle(canvas, start_pos, end_pos, color, brush_size)

            elif tool == "square":
                draw_square(canvas, start_pos, end_pos, color, brush_size)

            elif tool == "right_triangle":
                draw_right_triangle(canvas, start_pos, end_pos, color, brush_size)

            elif tool == "equilateral_triangle":
                draw_equilateral_triangle(canvas, start_pos, end_pos, color, brush_size)

            elif tool == "rhombus":
                draw_rhombus(canvas, start_pos, end_pos, color, brush_size)

            drawing_shape = False
            prev_pos = None

    # ---------------- DRAW ----------------

    mx, my = pygame.mouse.get_pos()
    my -= UI_HEIGHT
    mouse_pos = (mx, my)
    mouse_pressed = pygame.mouse.get_pressed()[0]

    # pencil
    if tool == "pencil" and mouse_pressed:
        if prev_pos:
            draw_pencil(canvas, prev_pos, mouse_pos, color, brush_size)
        prev_pos = mouse_pos

    # eraser
    if tool == "eraser" and mouse_pressed:
        if prev_pos:
            erase(canvas, prev_pos, mouse_pos, brush_size)
        prev_pos = mouse_pos

    # ---------------- TEXT COMMIT ----------------
    for txt, pos in text_objects:
        draw_text(canvas, font, txt, pos, color)

    # ---------------- PREVIEW ----------------
    if drawing_shape:

        if tool == "line":
            draw_line(overlay, start_pos, mouse_pos, color, brush_size)

        elif tool == "rect":
            draw_rect(overlay, start_pos, mouse_pos, color, brush_size)

        elif tool == "circle":
            draw_circle(overlay, start_pos, mouse_pos, color, brush_size)

        elif tool == "square":
            draw_square(overlay, start_pos, mouse_pos, color, brush_size)

        elif tool == "right_triangle":
            draw_right_triangle(overlay, start_pos, mouse_pos, color, brush_size)

        elif tool == "equilateral_triangle":
            draw_equilateral_triangle(overlay, start_pos, mouse_pos, color, brush_size)

        elif tool == "rhombus":
            draw_rhombus(overlay, start_pos, mouse_pos, color, brush_size)

    if typing:
        draw_text_preview(overlay, font, text_input, text_pos, color)

    # ---------------- RENDER ----------------
    screen.blit(canvas, (0, UI_HEIGHT))
    screen.blit(overlay, (0, UI_HEIGHT))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()