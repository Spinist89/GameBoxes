import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.fon = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.bg_color = pygame.image.load('Склад.bmp')
        self.bg_color2 = pygame.transform.scale(self.bg_color,(self.screen_width, self.screen_height))