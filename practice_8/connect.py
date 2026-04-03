import psycopg2
from config import DB_CONFIG

try:
    conn = psycopg2.connect(**DB_CONFIG)  # ** разворачивает словарь в аргументы
    print("Подключение успешно!")
    conn.close()
except Exception as e:
    print(f"Ошибка подключения: {e}")


## 3. `contacts.csv` — тестовые данные
'''
name,phone
Alice,+77011234567
Bob,+77029876543
Charlie,+77031112233
Diana,+77045556677


'''
