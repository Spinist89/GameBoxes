import time
from random import randint

import pygame


class RectangleSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._time_left = time.time() + randint(0, 0)
        self.image = pygame.image.load('ящик.bmp')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 8, self.image.get_height() // 8))
        self.rect = self.image.get_rect(center=(randint(80, 1700), -80))

    def update(self):
        if self._time_left < time.time():
            if self.rect.y < 680:
                self.rect.y += 1
            else:
                self.rect.y = -80
                self.rect.x = randint(80, 1700)
                self._time_left = time.time() + randint(0, 8)
