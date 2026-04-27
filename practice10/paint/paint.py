import pygame

pygame.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

drawing = False
mode = "brush"
color = (255, 0, 0)

start_pos = None
prev_pos = None

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 0, 0)
]

font = pygame.font.SysFont(None, 24)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            prev_pos = event.pos

            x, y = event.pos
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
                rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(canvas, color, rect)

            if mode == "circle":
                x1, y1 = start_pos
                x2, y2 = end_pos
                radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                pygame.draw.circle(canvas, color, start_pos, radius)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "brush"
            if event.key == pygame.K_2:
                mode = "rect"
            if event.key == pygame.K_3:
                mode = "circle"
            if event.key == pygame.K_4:
                mode = "eraser"

    if drawing and mode == "brush":
        current_pos = pygame.mouse.get_pos()

        if prev_pos is not None:
            pygame.draw.line(canvas, color, prev_pos, current_pos, 5)

        prev_pos = current_pos

    if drawing and mode == "eraser":
        pygame.draw.circle(canvas, (255, 255, 255), pygame.mouse.get_pos(), 10)

    screen.blit(canvas, (0, 0))

    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (i * 40, 0, 40, 40))

    text = font.render(f"Mode: {mode}", True, (0, 0, 0))
    screen.blit(text, (10, 45))

    pygame.display.update()
    clock.tick(60)

pygame.quit()