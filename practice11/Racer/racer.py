import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

car_img = pygame.image.load(r"C:\Study\PP2\practice11\Racer\images\mycar.png")
enemy_img = pygame.image.load(r"C:\Study\PP2\practice11\Racer\images\elsecar.png")

car_img = pygame.transform.scale(car_img, (60, 100))
enemy_img = pygame.transform.scale(enemy_img, (60, 100))

car = pygame.Rect(220, 600, 60, 100)
enemy = pygame.Rect(random.randint(0, WIDTH - 60), -120, 60, 100)

lines = []
coins = []

line_timer = 0
coin_timer = 0

score = 0
enemy_speed = 5

font = pygame.font.SysFont(None, 36)

def spawn_coin():
    x = random.randint(30, WIDTH - 30)
    weight = random.choice([1, 2, 3])
    return pygame.Rect(x, -20, 20, 20), weight

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
    if line_timer > 20:
        lines.append(pygame.Rect(WIDTH // 2 - 5, -50, 10, 50))
        line_timer = 0

    for line in lines[:]:
        line.y += enemy_speed
        if line.y > HEIGHT:
            lines.remove(line)
        pygame.draw.rect(screen, (255, 255, 255), line)

    coin_timer += 1
    if coin_timer > 40:
        coins.append(spawn_coin())
        coin_timer = 0

    for coin in coins[:]:
        rect, weight = coin
        rect.y += enemy_speed

        if rect.colliderect(car):
            score += weight
            coins.remove(coin)

        elif rect.y > HEIGHT:
            coins.remove(coin)

        pygame.draw.circle(screen, (255, 215, 0), rect.center, 10)

    enemy.y += enemy_speed

    if enemy.y > HEIGHT:
        enemy.y = -120
        enemy.x = random.randint(0, WIDTH - enemy.width)

    # COLLISION -> GAME OVER
    if car.colliderect(enemy):
        running = False

    screen.blit(car_img, (car.x, car.y))
    screen.blit(enemy_img, (enemy.x, enemy.y))

    text = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()