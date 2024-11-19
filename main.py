# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы
# (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
#
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и
# возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.


# 1

import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Какой-то общий звук животного"

    def eat(self):
        return f"{self.name} кушает."

# 2

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Чирик-курлык"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Рык или чмоканье"

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return "Шшшипит"

# 3

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")

# 4

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def list_animals(self):
        for animal in self.animals:
            print(f"Животное: {animal.name}, Возраст: {animal.age}")

    def list_staff(self):
        for staff_member in self.staff:
            print(f"Сотрудник: {staff_member.name}, Роль: {staff_member.__class__.__name__}")


# 5

class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."

class Veterinarian(Staff):
    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."


# 6


class ZooPersistent(Zoo):
    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)



# Создаем животных
bird = Bird(name="Попугай", age=2, wing_span=0.5)
mammal = Mammal(name="Лев", age=5, fur_color="Золотистый")
reptile = Reptile(name="Змея", age=3, scale_type="Гладкая")

# Полиморфизм
animal_sound([bird, mammal, reptile])

# Создаем сотрудников
keeper = ZooKeeper(name="Джон")
vet = Veterinarian(name="Анна")

# Создаем зоопарк
zoo = ZooPersistent(name="Мой Зоопарк")
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Список животных и сотрудников
zoo.list_animals()
zoo.list_staff()

# Сохранение и загрузка зоопарка
zoo.save_to_file("zoo_data.pkl")
loaded_zoo = ZooPersistent.load_from_file("zoo_data.pkl")
loaded_zoo.list_animals()
loaded_zoo.list_staff()

