import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

car = pygame.Rect(220, 600, 60, 100)

lines = []
coins = []

line_timer = 0
coin_timer = 0

score = 0
speed = 5

font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.x > 0:
        car.x -= 6
    if keys[pygame.K_RIGHT] and car.x < WIDTH - car.width:
        car.x += 6

    line_timer += 1
    if line_timer > 30:
        lines.append(pygame.Rect(WIDTH // 2 - 10, -50, 20, 50))
        line_timer = 0

    for line in lines[:]:
        line.y += speed
        if line.y > HEIGHT:
            lines.remove(line)
        pygame.draw.rect(screen, (255, 255, 255), line)

    coin_timer += 1
    if coin_timer > 40:
        x = random.randint(30, WIDTH - 30)
        coins.append(pygame.Rect(x, -20, 20, 20))
        coin_timer = 0

    for coin in coins[:]:
        coin.y += speed

        if coin.colliderect(car):
            coins.remove(coin)
            score += 1

        elif coin.y > HEIGHT:
            coins.remove(coin)

        pygame.draw.circle(screen, (255, 215, 0), coin.center, 10)

    pygame.draw.rect(screen, (0, 120, 255), car)

    text = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(text, (WIDTH - 160, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()