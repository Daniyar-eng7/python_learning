"""
Mickey's Clock Application
===========================
Отображает текущее время (минуты и секунды) с помощью изображений рук Микки Мауса.

Правая рука = минутная стрелка
Левая рука  = секундная стрелка

Как работает:
  1. Загружаем изображение руки (или создаём запасную стрелку)
  2. Каждую секунду читаем системное время
  3. Вычисляем угол поворота для минут и секунд
  4. Используем pygame.transform.rotate() для поворота
  5. Рисуем обе руки поверх циферблата
"""

import pygame
import datetime
import math
import os
from clock import get_hand_angle, draw_hand


def create_fallback_hand(width, height, color):

    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    # Рисуем стрелку: кончик вверху, основание внизу
    points = [
        (width // 2, 0),              # кончик стрелки (вверх)
        (width // 2 + 6, height // 3),  # правый край
        (width // 2 + 3, height),     # правое основание
        (width // 2 - 3, height),     # левое основание
        (width // 2 - 6, height // 3),  # левый край
    ]
    pygame.draw.polygon(surf, color, points)
    pygame.draw.polygon(surf, (30, 30, 30), points, 2)  # контур
    return surf


def main():
    pygame.init()

    # ── Настройки окна ──────────────────────────────────────────────
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    clock = pygame.time.Clock()

    CENTER = (WIDTH // 2, HEIGHT // 2)  # центр циферблата

    # ── Загрузка изображения руки ────────────────────────────────────
    hand_path = os.path.join(os.path.dirname(__file__), "images", "mickey_hand.png")

    if os.path.exists(hand_path):
        # Загружаем настоящее изображение руки Микки Мауса
        hand_image_raw = pygame.image.load(hand_path).convert_alpha()
        # Масштабируем до нужного размера
        hand_image = pygame.transform.scale(hand_image_raw, (100, 350))
        print("Изображение руки загружено!")
    else:
        # Создаём запасные стрелки
        print("mickey_hand.png не найден — используем запасные стрелки")
        hand_image = None  # будет создана ниже

    # Создаём две разные стрелки (для минут и секунд)
    # Если есть изображение — используем его для обеих
    if hand_image:
        minute_hand = hand_image
        second_hand = hand_image
    else:
        # Минутная рука — длиннее и темнее
        minute_hand = create_fallback_hand(20, 140, (50, 50, 80))
        # Секундная рука — длиннее и красная
        second_hand = create_fallback_hand(14, 160, (200, 40, 40))

    # ── Шрифт для отображения времени ───────────────────────────────
    font_large = pygame.font.SysFont("Arial", 56, bold=True)
    font_small = pygame.font.SysFont("Arial", 22)

    # ── Главный цикл ─────────────────────────────────────────────────
    running = True
    while running:

        # 1. Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 2. Читаем текущее время
        now = datetime.datetime.now()
        minutes = now.minute           # 0–59
        seconds = now.second           # 0–59
        # Добавляем миллисекунды для плавного движения
        seconds_smooth = seconds + now.microsecond / 1_000_000

        # 3. Вычисляем углы поворота
        # get_hand_angle(value, max_value) → угол в градусах
        minute_angle = get_hand_angle(minutes, 60)          # 60 минут = полный круг
        second_angle = get_hand_angle(seconds_smooth, 60)   # 60 секунд = полный круг

        # 4. Рисуем фон
        screen.fill((245, 240, 220))  # кремовый фон

        # Рисуем циферблат (круг)
        pygame.draw.circle(screen, (255, 255, 255), CENTER, 220)
        pygame.draw.circle(screen, (100, 80, 60), CENTER, 220, 6)

        # Рисуем отметки часов (12 отметок)
        for i in range(60):
            angle_rad = math.radians(i * 6 - 90)  # 6° на деление, -90 чтобы начать сверху
            if i % 5 == 0:
                # Крупные отметки для часов
                inner_r, outer_r = 195, 215
                thick = 4
                color = (80, 60, 40)
            else:
                # Мелкие отметки для минут
                inner_r, outer_r = 205, 215
                thick = 2
                color = (150, 130, 110)
            x1 = CENTER[0] + int(inner_r * math.cos(angle_rad))
            y1 = CENTER[1] + int(inner_r * math.sin(angle_rad))
            x2 = CENTER[0] + int(outer_r * math.cos(angle_rad))
            y2 = CENTER[1] + int(outer_r * math.sin(angle_rad))
            pygame.draw.line(screen, color, (x1, y1), (x2, y2), thick)

        # 5. Рисуем стрелки (сначала минутную — она "под" секундной)
        draw_hand(screen, minute_hand, minute_angle, CENTER)
        draw_hand(screen, second_hand, second_angle, CENTER)

        # Центральная точка (поверх стрелок)
        pygame.draw.circle(screen, (60, 40, 30), CENTER, 12)
        pygame.draw.circle(screen, (200, 160, 80), CENTER, 7)

        # 6. Отображаем цифровое время
        time_str = f"{minutes:02d}:{seconds:02d}"
        time_surf = font_large.render(time_str, True, (60, 40, 30))
        screen.blit(time_surf, (WIDTH // 2 - time_surf.get_width() // 2, HEIGHT - 90))

        # Подпись
        hint = font_small.render("Правая рука = минуты  |  Левая рука = секунды", True, (120, 100, 80))
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 45))

        # 7. Показываем кадр
        pygame.display.flip()
        clock.tick(60)  # 60 FPS для плавного движения секундной стрелки

    pygame.quit()


if __name__ == "__main__":
    main()
