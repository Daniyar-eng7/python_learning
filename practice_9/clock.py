import pygame
import math


def get_hand_angle(value, max_value):
    """
      - 0 секунд/минут = рука смотрит вверх (0°)
      - 15 сек/мин     = рука смотрит вправо (90°)
      - 30 сек/мин     = рука смотрит вниз (180°)
      - 45 сек/мин     = рука смотрит влево (270°)
    """
    # Вычисляем долю от полного оборота
    fraction = value / max_value
    # Переводим в градусы (360° = полный оборот), минус — по часовой стрелке
    angle = -fraction * 360
    return angle


def draw_hand(screen, original_image, angle, center_pos):
    """
    Рисует руку Микки Мауса на экране.
    """
    # Получаем повёрнутое изображение (новая поверхность)
    rotated = pygame.transform.rotate(original_image, angle)
    
    # Вычисляем прямоугольник так, чтобы центр ротации совпал с центром циферблата
    rect = rotated.get_rect(center=center_pos)
    
    # Рисуем на экране
    screen.blit(rotated, rect)
