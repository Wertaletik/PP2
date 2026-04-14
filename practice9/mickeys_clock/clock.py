import pygame
import datetime

class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (403, 141)

        self.clock_img = pygame.image.load(r"C:\Study\PP2\practice9\mickeys_clock\images\Clock.jpg").convert()
        self.clock_img = pygame.transform.scale(self.clock_img, (800, 600))

        self.hand_img = pygame.image.load(r"C:\Study\PP2\practice9\mickeys_clock\images\mickey_hand.png").convert_alpha()

    def get_time_angles(self):
        now = datetime.datetime.now()

        sec = now.second
        minute = now.minute

        sec_angle = -(sec / 60) * 360
        min_angle = -(minute / 60) * 360

        return sec_angle, min_angle

    def draw_hand(self, image, angle):
        rotated = pygame.transform.rotate(image, angle)

        rect = rotated.get_rect()

        rect.center = (
            self.center[0],
            self.center[1] + image.get_height() // 2
        )

        self.screen.blit(rotated, rect)

    def update(self):
        self.screen.blit(self.clock_img, (0, 0))

        sec_angle, min_angle = self.get_time_angles()

        self.draw_hand(self.hand_img, min_angle)

        self.draw_hand(self.hand_img, sec_angle)