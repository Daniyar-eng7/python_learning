import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

# ─────────────────────────────────────────
# 1. ПОИСК ПО ПАТТЕРНУ (вызов функции)
# ─────────────────────────────────────────
def search_contacts():
    pattern = input("Введи часть имени или телефона: ")
    conn = get_connection()
    cur = conn.cursor()
    # SELECT вызывает ФУНКЦИЮ
    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    rows = cur.fetchall()
    if rows:
        for r in rows:
            print(f"  {r[0]}. {r[1]} — {r[2]}")
    else:
        print("Не найдено!")
    cur.close()
    conn.close()

# ─────────────────────────────────────────
# 2. UPSERT (вызов процедуры)
# ─────────────────────────────────────────
def upsert_contact():
    name  = input("Имя: ")
    phone = input("Телефон: ")
    conn = get_connection()
    cur = conn.cursor()
    # CALL вызывает ПРОЦЕДУРУ
    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
    conn.commit()
    print(f"[OK] Upsert: {name} — {phone}")
    cur.close()
    conn.close()

# ─────────────────────────────────────────
# 3. МАССОВАЯ ВСТАВКА (вызов процедуры)
# ─────────────────────────────────────────
def bulk_insert():
    contacts = []
    print("Вводи контакты (пустое имя = стоп):")
    while True:
        name = input("  Имя: ").strip()
        if not name:
            break
        phone = input("  Телефон: ").strip()
        contacts.append((name, phone))

    names  = [c[0] for c in contacts]  # ['Alice', 'Bob']
    phones = [c[1] for c in contacts]  # ['+7700', '12345']

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "CALL bulk_insert(%s::VARCHAR[], %s::VARCHAR[]);",
        (names, phones)
    )
    conn.commit()
    print("[OK] Массовая вставка выполнена!")
    cur.close()
    conn.close()

# ─────────────────────────────────────────
# 4. ПАГИНАЦИЯ (вызов функции)
# ─────────────────────────────────────────
def show_page():
    page      = int(input("Страница (1,2,3...): "))
    page_size = int(input("Контактов на странице: "))
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM get_contacts_paged(%s, %s);",
        (page_size, (page - 1) * page_size)
    )
    rows = cur.fetchall()
    print(f"\n── Страница {page} ──")
    if rows:
        for r in rows:
            print(f"  {r[0]}. {r[1]} — {r[2]}")
    else:
        print("Больше контактов нет!")
    cur.close()
    conn.close()

# ─────────────────────────────────────────
# 5. УДАЛЕНИЕ (вызов процедуры)
# ─────────────────────────────────────────
def delete_contact():
    print("Удалить по: 1-имени  2-телефону")
    choice = input("Выбор: ")
    conn = get_connection()
    cur = conn.cursor()
    if choice == "1":
        name = input("Имя: ")
        cur.execute("CALL delete_contact(%s, NULL);", (name,))
    elif choice == "2":
        phone = input("Телефон: ")
        cur.execute("CALL delete_contact(NULL, %s);", (phone,))
    conn.commit()
    print("[OK] Удалено!")
    cur.close()
    conn.close()

# ─────────────────────────────────────────
# МЕНЮ
# ─────────────────────────────────────────
def menu():
    while True:
        print("""
── PhoneBook Practice 8 ──
1. Поиск по паттерну
2. Добавить / обновить (upsert)
3. Массовая вставка
4. Показать страницу
5. Удалить контакт
0. Выход
        """)
        choice = input("Выбор: ")
        if choice == "1":
            search_contacts()
        elif choice == "2":
            upsert_contact()
        elif choice == "3":
            bulk_insert()
        elif choice == "4":
            show_page()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("Выход!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()