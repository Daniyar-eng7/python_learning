from functools import reduce

# 1. map() and filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words   = ['hello', 'world', 'python', 'hi', 'cat']

# map - возвести в квадрат
squared = list(map(lambda x: x**2, numbers))
print('#1 map (квадрат):   ', squared)

# map - в верхний регистр
upper = list(map(str.upper, words))
print('#1 map (upper):     ', upper)

# filter - только чётные
evens = list(filter(lambda x: x % 2 == 0, numbers))
print('#1 filter (чётные): ', evens)

# filter - слова длиннее 4 букв
long_words = list(filter(lambda w: len(w) > 4, words))
print('#1 filter (слова):  ', long_words)

# map + filter вместе — чётные в квадрат
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print('#1 map+filter:      ', result)


# 2. reduce()


nums = [1, 2, 3, 4, 5]

# Сумма
total = reduce(lambda a, b: a + b, nums)
print('\n#2 reduce (сумма):        ', total)

# Произведение
product = reduce(lambda a, b: a * b, nums)
print('#2 reduce (произведение):', product)

# Максимум
maximum = reduce(lambda a, b: a if a > b else b, nums)
print('#2 reduce (максимум):    ', maximum)

# Минимум
minimum = reduce(lambda a, b: a if a < b else b, nums)
print('#2 reduce (минимум):     ', minimum)


# 3. enumerate() and zip()


fruits  = ['apple', 'banana', 'cherry']
names   = ['Alice', 'Bob', 'Charlie']
grades  = [85, 55, 92]
cities  = ['Almaty', 'Astana', 'Shymkent']

# enumerate - с нуля
print('\n#3 enumerate (с 0):')
for i, fruit in enumerate(fruits):
    print(f'   {i}: {fruit}')

# enumerate - с единицы
print('#3 enumerate (с 1):')
for i, fruit in enumerate(fruits, start=1):
    print(f'   {i}. {fruit}')

# zip - два списка
print('#3 zip (имя + оценка):')
for name, grade in zip(names, grades):
    print(f'   {name}: {grade}')

# zip - три списка
print('#3 zip (имя + оценка + город):')
for name, grade, city in zip(names, grades, cities):
    print(f'   {name} ({city}): {grade}')

# enumerate + zip вместе
print('#3 enumerate + zip:')
for i, (name, grade) in enumerate(zip(names, grades), start=1):
    status = 'сдал' if grade >= 60 else 'не сдал'
    print(f'   {i}. {name}: {grade} — {status}')


# 4. Type checking and conversions

x = 42
s = 'hello'
f = 3.14
l = [1, 2, 3]
b = True

# type()
print('\n#4 type():')
print('   type(42):      ', type(x))
print('   type("hello"): ', type(s))
print('   type(3.14):    ', type(f))
print('   type([]):      ', type(l))

# isinstance()
print('#4 isinstance():')
print('   isinstance(42, int):    ', isinstance(x, int))
print('   isinstance("hi", str):  ', isinstance(s, str))
print('   isinstance(3.14, float):', isinstance(f, float))
print('   isinstance(True, int):  ', isinstance(b, int))   # True! bool → int

# конвертация
print('#4 конвертации:')
print('   int("42"):     ', int('42'))
print('   float("3.14"): ', float('3.14'))
print('   str(42):       ', str(42))
print('   int(3.99):     ', int(3.99))    # обрезает, не округляет
print('   list("hello"): ', list('hello'))
print('   tuple([1,2,3]):', tuple([1, 2, 3]))

# безопасная конвертация
print('#4 безопасная конвертация:')

def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return f'Ошибка: "{value}" не число'

print('   safe_int("42"):  ', safe_int('42'))
print('   safe_int("abc"): ', safe_int('abc'))
print('   safe_int("3.14"):', safe_int('3.14'))
