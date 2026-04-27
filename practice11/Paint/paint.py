import pygame
import math

pygame.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

drawing = False
mode = "brush"
start_pos = None
prev_pos = None

color = (255, 0, 0)

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 0, 0),
    (255, 165, 0),
    (128, 0, 128)
]

font = pygame.font.SysFont(None, 24)

clear_rect = pygame.Rect(WIDTH - 110, 5, 100, 30)


def right_triangle(s, e):
    x1, y1 = s
    x2, y2 = e
    pygame.draw.polygon(canvas, color, [(x1, y1), (x1, y2), (x2, y2)])


def equilateral_triangle(s, e):
    x1, y1 = s
    x2, y2 = e
    side = abs(x2 - x1)
    h = int(math.sqrt(3) / 2 * side)
    pygame.draw.polygon(canvas, color, [(x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - h)])


def rhombus(s, e):
    x1, y1 = s
    x2, y2 = e
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    pygame.draw.polygon(canvas, color, [(cx, y1), (x2, cy), (cx, y2), (x1, cy)])


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            if clear_rect.collidepoint(pos):
                canvas.fill((255, 255, 255))
                continue

            drawing = True
            start_pos = pos
            prev_pos = pos

            x, y = pos
            if y < 40:
                idx = x // 40
                if idx < len(colors):
                    color = colors[idx]

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            prev_pos = None
            end_pos = event.pos

            if mode == "rect":
                x1, y1 = start_pos
                x2, y2 = end_pos
                rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
                pygame.draw.rect(canvas, color, rect)

            if mode == "circle":
                x1, y1 = start_pos
                x2, y2 = end_pos
                radius = int(((x2-x1)**2 + (y2-y1)**2) ** 0.5)
                pygame.draw.circle(canvas, color, start_pos, radius)

            if mode == "square":
                x1, y1 = start_pos
                x2, y2 = end_pos
                size = min(abs(x2-x1), abs(y2-y1))
                pygame.draw.rect(canvas, color, (x1, y1, size, size))

            if mode == "right_triangle":
                right_triangle(start_pos, end_pos)

            if mode == "equilateral":
                equilateral_triangle(start_pos, end_pos)

            if mode == "rhombus":
                rhombus(start_pos, end_pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "brush"
            if event.key == pygame.K_2:
                mode = "rect"
            if event.key == pygame.K_3:
                mode = "circle"
            if event.key == pygame.K_4:
                mode = "eraser"
            if event.key == pygame.K_5:
                mode = "square"
            if event.key == pygame.K_6:
                mode = "right_triangle"
            if event.key == pygame.K_7:
                mode = "equilateral"
            if event.key == pygame.K_8:
                mode = "rhombus"

    if drawing and mode == "brush":
        current = pygame.mouse.get_pos()
        if prev_pos is not None:
            pygame.draw.line(canvas, color, prev_pos, current, 5)
        prev_pos = current

    if drawing and mode == "eraser":
        pygame.draw.circle(canvas, (255, 255, 255), pygame.mouse.get_pos(), 10)

    screen.blit(canvas, (0, 0))

    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (i * 40, 0, 40, 40))

    pygame.draw.rect(screen, (200, 200, 200), clear_rect)
    clear_text = font.render("CLEAR", True, (0, 0, 0))
    screen.blit(clear_text, (WIDTH - 95, 10))

    text = font.render(f"Mode: {mode}", True, (0, 0, 0))
    screen.blit(text, (10, 45))

    pygame.display.update()
    clock.tick(60)

pygame.quit()