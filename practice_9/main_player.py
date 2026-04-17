"""
Music Player with Keyboard Controller
=======================================
Интерактивный музыкальный плеер с управлением с клавиатуры.

Управление:
  P     — Play (воспроизвести/возобновить)
  S     — Stop (остановить)
  N     — Next track (следующий трек)
  B     — Back / Previous (предыдущий трек)
  ↑ / ↓ — Громче / Тише
  Q     — Quit (выход)

Как работает:
  - MusicPlayer (из player.py) управляет pygame.mixer.music
  - main.py отвечает за отрисовку UI и обработку клавиш
  - check_and_advance() вызывается каждый кадр — если трек кончился,
    автоматически включается следующий
"""

import pygame
import os
from player import MusicPlayer


def draw_ui(screen, player, fonts):
    """Рисует весь интерфейс плеера."""
    font_title, font_track, font_info, font_hint = fonts
    W, H = screen.get_size()

    # Фон
    screen.fill((20, 20, 35))

    # ── Декоративная рамка ────────────────────────────────────────
    pygame.draw.rect(screen, (60, 60, 100), (40, 40, W - 80, H - 80), 2, border_radius=16)

    # ── Заголовок ─────────────────────────────────────────────────
    title_surf = font_title.render("🎵 Music Player", True, (180, 160, 255))
    screen.blit(title_surf, (W // 2 - title_surf.get_width() // 2, 70))

    # ── Название трека ────────────────────────────────────────────
    track_name = player.get_current_track_name()
    # Обрезаем если слишком длинное
    if len(track_name) > 35:
        track_name = track_name[:32] + "..."

    track_surf = font_track.render(track_name, True, (255, 255, 255))
    screen.blit(track_surf, (W // 2 - track_surf.get_width() // 2, 160))

    # ── Номер трека ───────────────────────────────────────────────
    if player.playlist:
        track_num = f"Трек {player.current_index + 1} из {len(player.playlist)}"
    else:
        track_num = "Плейлист пуст — добавьте .mp3 файлы в папку music/"
    num_surf = font_info.render(track_num, True, (140, 140, 200))
    screen.blit(num_surf, (W // 2 - num_surf.get_width() // 2, 210))

    # ── Статус воспроизведения ────────────────────────────────────
    status = player.get_status()
    status_color = (100, 255, 120) if "Играет" in status else (255, 180, 60)
    status_surf = font_track.render(status, True, status_color)
    screen.blit(status_surf, (W // 2 - status_surf.get_width() // 2, 270))

    # ── Громкость — полоска ───────────────────────────────────────
    vol_text = font_info.render(f"Громкость: {int(player.volume * 100)}%", True, (180, 180, 220))
    screen.blit(vol_text, (W // 2 - vol_text.get_width() // 2, 340))

    bar_x, bar_y = W // 2 - 150, 370
    bar_w, bar_h = 300, 12
    pygame.draw.rect(screen, (60, 60, 90), (bar_x, bar_y, bar_w, bar_h), border_radius=6)
    fill_w = int(bar_w * player.volume)
    if fill_w > 0:
        pygame.draw.rect(screen, (120, 100, 220), (bar_x, bar_y, fill_w, bar_h), border_radius=6)
    pygame.draw.rect(screen, (100, 100, 160), (bar_x, bar_y, bar_w, bar_h), 1, border_radius=6)

    # ── Кнопки управления (визуальные) ───────────────────────────
    controls = [
        ("[B]", "Назад",    (W // 2 - 180, 430)),
        ("[P]", "Play",     (W // 2 - 60,  430)),
        ("[S]", "Stop",     (W // 2 + 60,  430)),
        ("[N]", "Вперёд",   (W // 2 + 180, 430)),
    ]
    for key, label, pos in controls:
        key_surf  = font_info.render(key,   True, (220, 200, 255))
        lab_surf  = font_hint.render(label, True, (140, 140, 180))
        screen.blit(key_surf,  (pos[0] - key_surf.get_width()  // 2, pos[1]))
        screen.blit(lab_surf,  (pos[0] - lab_surf.get_width()  // 2, pos[1] + 26))

    # ── Подсказки ─────────────────────────────────────────────────
    hints = [
        "↑ / ↓ — Громкость",
        "Q — Выход",
    ]
    for i, hint in enumerate(hints):
        h_surf = font_hint.render(hint, True, (100, 100, 140))
        screen.blit(h_surf, (W // 2 - h_surf.get_width() // 2, H - 90 + i * 24))


def main():
    pygame.init()
    pygame.mixer.init()

    # ── Окно ──────────────────────────────────────────────────────
    WIDTH, HEIGHT = 600, 550
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    clock_fps = pygame.time.Clock()

    # ── Шрифты ────────────────────────────────────────────────────
    font_title = pygame.font.SysFont("Arial", 36, bold=True)
    font_track = pygame.font.SysFont("Arial", 28)
    font_info  = pygame.font.SysFont("Arial", 20)
    font_hint  = pygame.font.SysFont("Arial", 16)
    fonts = (font_title, font_track, font_info, font_hint)

    # ── Музыкальный плеер ─────────────────────────────────────────
    music_folder = os.path.join(os.path.dirname(__file__), "music")
    os.makedirs(music_folder, exist_ok=True)
    player = MusicPlayer(music_folder)

    # ── Главный цикл ──────────────────────────────────────────────
    running = True
    while running:

        # 1. Обработка событий (KEYDOWN — срабатывает один раз при нажатии)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key in (pygame.K_b, pygame.K_LEFT):
                    player.prev_track()
                elif event.key == pygame.K_UP:
                    player.volume_up()
                elif event.key == pygame.K_DOWN:
                    player.volume_down()
                elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False

        # 2. Проверяем — не кончился ли трек (автопереход)
        player.check_and_advance()

        # 3. Рисуем интерфейс
        draw_ui(screen, player, fonts)

        # 4. Показываем кадр
        pygame.display.flip()
        clock_fps.tick(30)  # 30 FPS достаточно для плеера

    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == "__main__":
    main()
