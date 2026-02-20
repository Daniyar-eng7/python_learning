class Animal:                # Родительский класс
    def __init__(self, name):
        self.name = name

    def speak(self):         # Общий метод
        print(f"{self.name} издает звук")

class Dog(Animal):            # Дочерний класс (наследует от Animal)
    def speak(self):          # Переопределяем метод
        print(f"{self.name} говорит Гав!")

class Cat(Animal):            # Ещё один дочерний класс
    def speak(self):
        print(f"{self.name} говорит Мяу!")

# Использование
dog = Dog("Бобик")
dog.speak()        # Бобик говорит Гав!

cat = Cat("Мурка")
cat.speak()        # Мурка говорит Мяу!

