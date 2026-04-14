import pygame
from clock import MickeyClock

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

mickey = MickeyClock(screen)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey.update()

    pygame.display.flip()
    clock.tick(1) 

pygame.quit()