"""
Отвечает за:
  - Загрузку списка треков из папки
  - Управление воспроизведением (play, stop, next, previous)
  - Хранение состояния (текущий трек, статус)
"""

import pygame
import os


class MusicPlayer:
    """
    Класс для управления музыкальным плеером.
    """

    SUPPORTED_FORMATS = ('.mp3', '.wav', '.ogg', '.flac')

    def __init__(self, music_folder):
        """
        music_folder — путь к папке с музыкальными файлами.
        Автоматически сканирует папку и строит плейлист.
        """
        self.music_folder = music_folder
        self.playlist = []          # список путей к файлам
        self.current_index = 0      # индекс текущего трека
        self.is_playing = False     # статус воспроизведения
        self.volume = 0.7           # громкость 0.0 – 1.0

        # Загружаем список треков
        self._scan_folder()

        # Устанавливаем начальную громкость
        pygame.mixer.music.set_volume(self.volume)

    def _scan_folder(self):
        """Сканирует папку и находит все поддерживаемые аудиофайлы."""
        if not os.path.exists(self.music_folder):
            print(f"Папка {self.music_folder} не найдена. Плейлист пуст.")
            return

        for filename in sorted(os.listdir(self.music_folder)):
            if filename.lower().endswith(self.SUPPORTED_FORMATS):
                full_path = os.path.join(self.music_folder, filename)
                self.playlist.append(full_path)

        print(f"Найдено треков: {len(self.playlist)}")

    def _load_current(self):
        """Загружает текущий трек в микшер (не воспроизводит)."""
        if not self.playlist:
            return False
        try:
            pygame.mixer.music.load(self.playlist[self.current_index])
            return True
        except pygame.error as e:
            print(f"Ошибка загрузки трека: {e}")
            return False

    def play(self):
        """Начать/возобновить воспроизведение."""
        if not self.playlist:
            print("Плейлист пуст!")
            return

        if self.is_playing:
            # Уже играет — ничего не делаем
            return

        if pygame.mixer.music.get_busy():
            # Трек на паузе — возобновляем
            pygame.mixer.music.unpause()
        else:
            # Загружаем и играем с начала
            if self._load_current():
                pygame.mixer.music.play()

        self.is_playing = True

    def stop(self):
        """Остановить воспроизведение и вернуться в начало трека."""
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        """Следующий трек. Если конец плейлиста — переходим на первый."""
        if not self.playlist:
            return
        self.stop()
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self._load_current()
        pygame.mixer.music.play()
        self.is_playing = True

    def prev_track(self):
        """Предыдущий трек. Если начало плейлиста — переходим на последний."""
        if not self.playlist:
            return
        self.stop()
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self._load_current()
        pygame.mixer.music.play()
        self.is_playing = True

    def volume_up(self):
        """Увеличить громкость на 10%."""
        self.volume = min(1.0, self.volume + 0.1)
        pygame.mixer.music.set_volume(self.volume)

    def volume_down(self):
        """Уменьшить громкость на 10%."""
        self.volume = max(0.0, self.volume - 0.1)
        pygame.mixer.music.set_volume(self.volume)

    def get_current_track_name(self):
        """Возвращает название текущего трека (без пути и расширения)."""
        if not self.playlist:
            return "Нет треков"
        filename = os.path.basename(self.playlist[self.current_index])
        name, _ = os.path.splitext(filename)
        return name

    def get_status(self):
        """Возвращает строку со статусом: ▶ Playing / ⏸ Paused / ⏹ Stopped."""
        if self.is_playing and pygame.mixer.music.get_busy():
            return "▶  Играет"
        elif self.is_playing:
            return "⏹  Стоп"
        else:
            return "⏹  Остановлен"

    def check_and_advance(self):
        """
        Вызывается каждый кадр.
        Если трек закончился естественным путём — автоматически ставим следующий.
        """
        if self.is_playing and not pygame.mixer.music.get_busy():
            self.next_track()
