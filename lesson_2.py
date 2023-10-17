class Transport: # Чертеж - Абстракитный класс
    wheels = 4 # Атрипбут класса
    # __init__(self) - конструктор
    # self - сам объект
    # self.model - Атрибут объекта
    def __init__(self, model, year, color): 
        self.model = model
        self.year = year
        self.color = color
    
    def info(self):
        print(f"Бренд машины - {self.model}, год выпуска - {self.year}, цвет - {self.color}")


class Car(Transport):
    def __init__(self, model, year, color, penalties = 2000):
        Transport.__init__(self, model, year, color) # Первый сполсоб (Напрямую к классу)
        # super().__init__(model, year, color) # Второй способ (с помощью метода super)
        self.penalties = penalties

lexus = Car("600", 2023, "White")
lexus.info()
print(lexus.penalties)


class Animal:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

        
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)
    def speak(self):
        print("Woof")

class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)
    def speak(self):
        print("Meow")

class Cow(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)
    def speak(self):
        print("Moo")

dog = Dog("Ak-tosh", "Alabai", 1)
cat = Cat("Muska", "swinks", 3)
cow = Cow("Tamara", "Angust", 5)
dog.speak()
cat.speak()
cow.speak()


def speak_dog():
    print("Gaf")

def speak_cat():
    print("Meow")

def speak():
    print("Moo")

speak_dog()
speak_cat()
speak()

num = 5
num = 7
print(num)