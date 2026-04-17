# Practice 7 — Pygame Games

## Установка и запуск

```bash
# 1. Создать виртуальное окружение
python3 -m venv venv

# 2. Активировать
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Установить зависимости
pip install -r requirements.txt
```

## Задания

### 3.1 Mickey's Clock
```bash
cd mickeys_clock
python main.py
```
Часы с руками Микки Мауса. Правая рука = минуты, левая = секунды.
Если нет `images/mickey_hand.png` — используются запасные стрелки.

### 3.2 Music Player
```bash
cd music_player
# Добавьте .mp3 или .wav файлы в папку music/
python main.py
```
Управление: P=Play, S=Stop, N=Next, B=Back, ↑↓=Громкость, Q=Выход

### 3.3 Moving Ball
```bash
cd moving_ball
python main.py
```
Стрелки = движение на 20px. Мяч не выходит за границы.
