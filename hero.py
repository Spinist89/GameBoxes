import pygame

class Hero():
    """Класс для управления героем."""
    def __init__(self, ai_game):
        """Инициализирует героя и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение героя и получает прямоугольник.
        self.image = pygame.image.load('Чел паук.bmp')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        # Каждый новый герой появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
        elif self.moving_up:
            self.rect.y -= 1
        elif self.moving_down:
            self.rect.y += 1

    def blitme(self):
        """Рисует героя в текущей позиции."""
        self.screen.blit(self.image, self.rect)
