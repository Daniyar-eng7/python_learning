"""
Хранит положение мяча и содержит логику движения с проверкой границ.
"""


class Ball:
    """
      - левая граница:  x - radius >= 0  →  x >= radius
      - правая граница: x + radius <= W  →  x <= W - radius
      - верхняя:        y - radius >= 0  →  y >= radius
      - нижняя:         y + radius <= H  →  y <= H - radius
    """

    RADIUS = 25          # радиус мяча (50x50 → radius=25)
    STEP   = 20          # пикселей за одно нажатие клавиши
    COLOR  = (220, 40, 40)    # красный
    BORDER_COLOR = (160, 20, 20)  # тёмно-красный контур

    def __init__(self, screen_width, screen_height):
        """Создаём мяч по центру экрана."""
        self.screen_width  = screen_width
        self.screen_height = screen_height
        # Центр экрана
        self.x = screen_width  // 2
        self.y = screen_height // 2

    def move(self, dx, dy):
        """
        dx > 0 → вправо,  dx < 0 → влево
        dy > 0 → вниз,    dy < 0 → вверх
        """
        new_x = self.x + dx
        new_y = self.y + dy

        # Проверяем горизонтальные границы
        if self.RADIUS <= new_x <= self.screen_width - self.RADIUS:
            self.x = new_x

        # Проверяем вертикальные границы
        if self.RADIUS <= new_y <= self.screen_height - self.RADIUS:
            self.y = new_y

    def draw(self, screen):
        """
        Рисует мяч на экране.
        Сначала заливаем кружок цветом, потом рисуем контур поверх.
        """
        import pygame
        # Основной кружок
        pygame.draw.circle(screen, self.COLOR, (self.x, self.y), self.RADIUS)
        # Контур (border_radius=2 делает обводку)
        pygame.draw.circle(screen, self.BORDER_COLOR, (self.x, self.y), self.RADIUS, 3)
        # Блик (маленький белый кружок для объёма)
        pygame.draw.circle(screen, (255, 150, 150),
                           (self.x - self.RADIUS // 3, self.y - self.RADIUS // 3),
                           self.RADIUS // 5)
