# Магические методы - dunder методы (начинается и заканчивается "__")

class Car:
    def __init__(self, model, year, wheels):
        self.model = model
        self.year = year
        self.wheels = wheels

    def info(self):
        print(f"Бренд машины - {self.model}, год выпуска - {self.year}")
    # Магические методы для арифметических действий
    def __str__(self): # str == print (str - выводит информацию о классе (str == info, print))
        return f"Бренд машины - {self.model}, год выпуска - {self.year} кол-во колес - {self.wheels} , "

    def __add__(self, other): # операция сложения == ("+")
        new_year = self.year + other.year
        return Car(self.model, new_year, self.wheels)

    def __sub__(self, other): # операция вычитания (-)
        new_wheels = self.wheels - other.wheels
        return Car(self.model, self.year, new_wheels)

    def __mul__(self, other): #  операция умножения (*)
        new_wheels = self.wheels * other.wheels
        return Car(self.model, self.year, new_wheels)

    def __floordiv__(self, other):  # операция целочисленного деления (//)
        new_wheels = self.wheels // other.wheels
        return Car(self.model, self.year, new_wheels)
    
    def __truediv__(self, other):  # операция целочисленного деления (//)
        new_wheels = self.wheels / other.wheels
        return Car(self.model, self.year, new_wheels)
    
    # Магические методы для операторов сравнения

    def __gt__(self, other): # больше чем (">")
        return self.year > other.year 

    def __lt__(self, other): # меньше чем ("<") - less than
        return self.year > other.year

    def __eq__(self, other): # равно ("==") - equals
        return self.year == other.year

    def __ne__(self, other): # не равно ("!=") - not equals
        return self.year != other.year

    def __ge__(self, other): # больше или равно (">=")
        return self.year >= other.year

    def __le__(self, other): # меньше или равно ("<=")
        return self.year <= other.year
    
    def __call__(self, new_model): # Метод __call__ автоматически вызывается, когда к объекту обращаются как к функции
        self.model = new_model
    # electriccar("Niva") - __call__ (Вызывается таким образом)



car1 = Car("BMW - f90", 2021, 4)
car2 = Car("Mersedes - benz", 2023, 4)
print(car1) # Если вызвать без магического метода выйдет путь
# car.info()

# Арифметические действия
print(car1 + car2) # __add__
print(car1 - car2) # __sub__
print(car1 * car2) # __mul__
print(car1 // car2) # __floordiv__
print(car1 / car2) # __truediv__

# Операторы сравнения
print(car1 > car2)
print(car1 < car2)
print(car1 == car2)
print(car1 != car2)
print(car1 >= car2)
print(car1 <= car2)

class ElectricCar(Car):
    def __init__(self, model, year,wheels , battery):
        Car.__init__(self, model, year, wheels)
        self.battery = battery

    def __str__(self):
        return super().__str__() + f"Заряд батареи {self.battery}"

electriccar = ElectricCar("Avalon", 2020, 4, 1000)
print(electriccar)
electriccar.info()
electriccar("Niva") # __call__ 
print(electriccar)


from lesson_5.folder.abstract import Person
print("Hello World")
print("Hello World")
print("Hello World")
