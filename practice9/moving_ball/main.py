import pygame
from ball import Ball

pygame.init()

width, height = 650, 450
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

ball = Ball(width // 2, height // 2)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move(-ball.step, 0, width, height)
            elif event.key == pygame.K_RIGHT:
                ball.move(ball.step, 0, width, height)
            elif event.key == pygame.K_UP:
                ball.move(0, -ball.step, width, height)
            elif event.key == pygame.K_DOWN:
                ball.move(0, ball.step, width, height)

    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()