# ООП - Объектно Ориентированое Програмирование
# DRY = Don`t repeat yourself == не повторяй себя

# class Car:
#     # model = "Mersedes" # атрибут/свойства/поля класса
#     # wheels = 4 # атрибут класса
#     # __init__ - Конструктор
#       self - сам объект
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color

#     def info(self):
#         print(f"Бренд машины - {self.model}, год выпуска - {self.year}, цвет - {self.color}")


# lexys = Car("es-350", 2023, "black")
# mersedes = Car("cls", 2020, "black")
# lexys.info()
# mersedes.info()
# print(mersedes.year)
# print(lexys.color)


# class Cow:
#     def make_sound(self):
#         print("Мууу!")

# cow = Cow()
# cow.make_sound()


# class Airplane:
#     def __init__(self, model, year, max_speed, capacity):
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.capacity = capacity
#         self.is_flying = False
#         self.odometer = 0

#     def take_off(self):
#         self.is_flying = True
#         print("Самалет поднимается в воздух")
    
#     def fly(self, distance):
#         if self.is_flying:
#             self.odometer += distance
#             print(f"Самолет прелетел {distance} км ")
#         else:
#             print("Сначалв выполните взлет")

#     def land(self):
#         self.is_flying = False
#         print("Самолет на земле")
    
    
#     def info_about_plane(self):
#         print(f"Модель - {self.model}")
#         print(f"год выпуска - {self.year}")
#         print(f"Максимальная скорость - {self.max_speed} км/ч")
#         print(f"вмещаемость - {self.capacity} человек")
#         print(f"пройденная дистанция - {self.odometer} км")

# plane = Airplane("AH-4", 1982, 1200, 250)
# plane.take_off()
# plane.fly(1000)
# plane.fly(2000)
# plane.land()
# plane.info_about_plane()


# booing = Airplane("747", 2000, 2000, 2)
# booing.take_off()
# booing.fly(70000)
# booing.land
# booing.info_about_plane()


class Test:
    test = None
print(Test.test)




class MyClass:
    def __init__(self):
        self.value = 42

obj = MyClass()
print(obj.value)








class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

obj = D()


#     def print_text(self):
#         print("Это родительский класс (Test)")

# class Test2(Test):
#     def print_text(self):
#         print("Это дочерний класс (Test2)")

# test = Test2()
# test.print_text()
        





