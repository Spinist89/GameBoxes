import sys
import pygame


from settings import Settings
from hero import Hero
from box import RectangleSprite

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ящики")
        self.hero = Hero(self)
        self.enemies = pygame.sprite.Group()
        self.all_mario = [RectangleSprite() for i in range(3)]
        self.enemies.add(self.all_mario)


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.hero.update()
            self._update_screen()
            # При каждом проходе цикла перерисовывается экран.

    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.hero.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.hero.moving_left = True
                elif event.key == pygame.K_UP:
                    self.hero.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.hero.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.hero.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.hero.moving_left = False
                elif event.key == pygame.K_UP:
                    self.hero.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.hero.moving_down = False
        # При каждом проходе цикла перерисовывается экран.

    def _update_screen(self):

        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.blit(self.settings.bg_color2, self.settings.fon)
        self.hero.blitme()
        for mario in self.all_mario:
            if mario.rect.collidepoint(self.hero.rect.center):
                mario.rect.y += 1
        self.enemies.draw(self.screen)
        self.enemies.update()
        # Отображение последнего прорисованного экрана.

        pygame.display.flip()


if __name__ == '__main__':
# Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()