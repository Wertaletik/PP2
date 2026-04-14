import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont(None, 28)

playlist = ["practice9/music_player/music/track1.wav", "practice9/music_player/music/track2.wav"]
player = MusicPlayer(playlist)

running = True
while running:
    screen.fill((30, 30, 30))
    song = list(player.get_current().split("/"))[3][:-4]
    text = font.render(f"Track: {song}", True, (255, 255, 255))
    screen.blit(text, (20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()