"""
Moving Ball Game
=================
Красный мяч (50x50, радиус 25) на белом фоне.
Управление стрелками — каждое нажатие двигает мяч на 20 пикселей.
Мяч не может выйти за границы экрана.

Как работает управление:
  Используем KEYDOWN (не get_pressed!) потому что задание требует
  "каждое нажатие = 20px" — то есть один дискретный шаг, а не плавное движение.

Сравнение:
  KEYDOWN    → один шаг за нажатие (дискретно, как в условии)
  get_pressed → двигается пока держишь (плавно)
"""

import pygame
from ball import Ball


def draw_grid(screen, step=50):
    """Рисует лёгкую сетку — помогает видеть шаги движения."""
    W, H = screen.get_size()
    for x in range(0, W, step):
        pygame.draw.line(screen, (230, 230, 230), (x, 0), (x, H))
    for y in range(0, H, step):
        pygame.draw.line(screen, (230, 230, 230), (0, y), (W, y))


def main():
    pygame.init()

    # ── Настройки ─────────────────────────────────────────────────
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball — Arrow keys to move")
    clock = pygame.time.Clock()

    # ── Создаём мяч ───────────────────────────────────────────────
    ball = Ball(WIDTH, HEIGHT)

    # ── Шрифт для подсказок ───────────────────────────────────────
    font = pygame.font.SysFont("Arial", 18)

    # ── Счётчик шагов ─────────────────────────────────────────────
    steps = 0

    # ── Главный цикл ──────────────────────────────────────────────
    running = True
    while running:

        # 1. Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # KEYDOWN — срабатывает ОДИН РАЗ при нажатии клавиши
            # Это даёт дискретное движение: один шаг за нажатие
            if event.type == pygame.KEYDOWN:
                moved = True
                if event.key == pygame.K_UP:
                    ball.move(0, -Ball.STEP)        # вверх = уменьшаем y
                elif event.key == pygame.K_DOWN:
                    ball.move(0, +Ball.STEP)        # вниз = увеличиваем y
                elif event.key == pygame.K_LEFT:
                    ball.move(-Ball.STEP, 0)        # влево = уменьшаем x
                elif event.key == pygame.K_RIGHT:
                    ball.move(+Ball.STEP, 0)        # вправо = увеличиваем x
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    moved = False

                if moved:
                    steps += 1

        # 2. Рисуем
        screen.fill((255, 255, 255))  # белый фон

        # Лёгкая сетка для наглядности
        draw_grid(screen)

        # Мяч
        ball.draw(screen)

        # Информация
        pos_text  = font.render(f"Позиция: ({ball.x}, {ball.y})", True, (80, 80, 80))
        step_text = font.render(f"Шагов: {steps}", True, (80, 80, 80))
        hint_text = font.render("Стрелки — движение  |  ESC — выход", True, (160, 160, 160))

        screen.blit(pos_text,  (10, 10))
        screen.blit(step_text, (10, 35))
        screen.blit(hint_text, (WIDTH // 2 - hint_text.get_width() // 2, HEIGHT - 30))

        # 3. Показываем кадр
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
