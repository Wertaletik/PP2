import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLOCK = 20

snake = [(100, 100), (80, 100), (60, 100)]
direction = (BLOCK, 0)

def random_food():
    while True:
        pos = (random.randrange(0, WIDTH, BLOCK),
               random.randrange(0, HEIGHT, BLOCK))
        if pos not in snake:
            return pos

food = random_food()

score = 0
level = 1
speed = 8

font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = (-BLOCK, 0)
    if keys[pygame.K_RIGHT]:
        direction = (BLOCK, 0)
    if keys[pygame.K_UP]:
        direction = (0, -BLOCK)
    if keys[pygame.K_DOWN]:
        direction = (0, BLOCK)


    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])


    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False


    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = random_food()


        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    
    if new_head in snake[1:]:
        running = False

    
    pygame.draw.rect(screen, (255, 0, 0), (*food, BLOCK, BLOCK))

    
    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, BLOCK, BLOCK))

    
    text = font.render(f"Score: {score} Level: {level}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()