import psycopg2
import csv
from config import DB_CONFIG


# ПОДКЛЮЧЕНИЕ

def get_connection():
    return psycopg2.connect(**DB_CONFIG)


# 1. СОЗДАТЬ ТАБЛИЦУ

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id    SERIAL       PRIMARY KEY,
            name  VARCHAR(100) NOT NULL,
            phone VARCHAR(20)  NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Таблица создана!")


# 2. ДОБАВИТЬ ИЗ CSV

def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)        # читает CSV как словарь
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s);",
                (row['name'], row['phone'])
            )
    conn.commit()
    cur.close()
    conn.close()
    print("Контакты из CSV добавлены!")


# 3. ДОБАВИТЬ ВРУЧНУЮ

def insert_from_console():
    name  = input("Имя: ")
    phone = input("Телефон: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s);",
        (name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Контакт {name} добавлен!")


# 4. ПОКАЗАТЬ ВСЕ

def show_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone FROM phonebook ORDER BY name;")
    rows = cur.fetchall()
    print("\n── Все контакты ──")
    for row in rows:
        print(f"  {row[0]}. {row[1]} — {row[2]}")
    cur.close()
    conn.close()


# 5. ПОИСК ПО ИМЕНИ

def search_by_name():
    name = input("Введи имя для поиска: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, phone FROM phonebook WHERE name ILIKE %s;",
        (f"%{name}%",)   # ILIKE = поиск без учёта регистра
    )
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"  {row[0]}. {row[1]} — {row[2]}")
    else:
        print("Не найдено!")
    cur.close()
    conn.close()


# 6. ОБНОВИТЬ КОНТАКТ

def update_contact():
    name     = input("Имя контакта которого обновить: ")
    new_phone = input("Новый номер: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s;",
        (new_phone, name)
    )
    conn.commit()
    print(f"Обновлено строк: {cur.rowcount}")
    cur.close()
    conn.close()


# 7. УДАЛИТЬ КОНТАКТ

def delete_contact():
    print("Удалить по: 1-имени  2-телефону")
    choice = input("Выбор: ")
    conn = get_connection()
    cur = conn.cursor()
    if choice == "1":
        name = input("Имя: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s;", (name,))
    elif choice == "2":
        phone = input("Телефон: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
    conn.commit()
    print(f"Удалено строк: {cur.rowcount}")
    cur.close()
    conn.close()


#Поиск по телефону
def search_by_phone():
    phone = input("Введи номер или префикс: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, phone FROM phonebook WHERE phone LIKE %s;",
        (f"{phone}%",)
    )
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"  {row[0]}. {row[1]} — {row[2]}")
    else:
        print("Не найдено!")
    cur.close()
    conn.close()
    
# МЕНЮ

def menu():
    create_table()
    while True:
        print("""
── PhoneBook ──
1. Загрузить из CSV
2. Добавить вручную
3. Показать все
4. Поиск по имени
5. Обновить контакт
6. Удалить контакт
7. Поиск по телефону
0. Выход
        """)
        choice = input("Выбор: ")
        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            show_all()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            search_by_phone()
        elif choice == "0":
            print("Выход!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()
