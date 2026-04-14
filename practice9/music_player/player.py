import pygame
import os

class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0

    def play(self):
        try:
            path = self.playlist[self.index]
            if not os.path.exists(path):
                print("Файл не найден:", path)
                return

            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            print("Играет:", path)

        except Exception as e:
            print("Ошибка воспроизведения:", e)

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.play()

    def get_current(self):
        return self.playlist[self.index]