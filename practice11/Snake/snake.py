import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLOCK = 20

snake = [(100, 100), (80, 100), (60, 100)]
direction = (BLOCK, 0)

font = pygame.font.SysFont(None, 28)

score = 0
speed = 8

food = None
bonus_food = None

food_timer = 0
bonus_timer = 0


def spawn_food():
    return {
        "pos": (random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK)),
        "timer": 999999
    }


def spawn_bonus():
    return {
        "pos": (random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK)),
        "timer": random.randint(120, 200)
    }


food = spawn_food()

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

    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False

    snake.insert(0, new_head)

    if food is None:
        food = spawn_food()

    if bonus_food is None:
        if random.randint(1, 80) == 1:
            bonus_food = spawn_bonus()

    # обычная еда (1 очко)
    if new_head == food["pos"]:
        score += 1
        food = spawn_food()
    else:
        snake.pop()

    # бонусная еда (3 очка)
    if bonus_food:
        bonus_food["timer"] -= 1

        if new_head == bonus_food["pos"]:
            score += 3
            bonus_food = None

        elif bonus_food["timer"] <= 0:
            bonus_food = None

    if new_head in snake[1:]:
        running = False

    # обычная еда (красная)
    pygame.draw.rect(screen, (255, 0, 0), (*food["pos"], BLOCK, BLOCK))

    # бонусная еда (жёлтая)
    if bonus_food:
        pygame.draw.rect(screen, (255, 215, 0), (*bonus_food["pos"], BLOCK, BLOCK))

    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, BLOCK, BLOCK))

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()