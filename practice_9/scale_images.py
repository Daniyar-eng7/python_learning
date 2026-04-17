import pygame
import os

def scale():
    pygame.init()
    # Загружаем твои картинки (проверь, что они в папке images!)
    hand = pygame.image.load("images/mickey_hand.png")
    body = pygame.image.load("images/mickey_body.png")

    # 1. Масштабируем руку (делаем её побольше, например, в 2 раза)
    w, h = hand.get_size()
    new_hand = pygame.transform.scale(hand, (w * 2, h * 2)) 
    
    # 2. Масштабируем тело (делаем его побольше, например, 300x300 пикселей)
    # Попробуй поменять эти цифры, если Микки всё ещё будет маленьким
    new_body = pygame.transform.scale(body, (300, 300))
    
    # 3. Сохраняем результат (перезаписываем файлы)
    pygame.image.save(new_hand, "images/mickey_hand.png")
    pygame.image.save(new_body, "images/mickey_body.png")
    print("Готово! Картинки в папке images обновлены.")

scale()