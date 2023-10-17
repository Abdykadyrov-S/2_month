# Декомпозиция - разделение кода по модулям

# from folder.calculator import sum as add # Мы можем переименновывать во время импортов (чтобы избежать конфликтов)

# print(add(9,3))

# from folder.calculator import sum, sub # точечный иморт

# print(sum(2,2))
# print(sub(5,2))

# import calc # иморт модуля

# print(calc.add(5,2))
# print(calc.sub(7,2))

# from calculator import * # Из модуля имортируем всё

# print(add(2,2))
# print(sub(5,2))
# print(__name__)


# from folder.abstract import Person

# class People(Person):
#     def __str__(self):
#         return f"имя - {self.name}" 


# people = People("Sema", 18)
# # print(people.name)
# print(people)

# Кастомные модули : abstrct, calculator
# Встроенные модули : random , math, datetime, time
# from random import randint

# a = randint(1,10)
# print(a)

# import time

# while True:
#     time.sleep(6)
#     print("loading...")

# Внешние модули:

# from termcolor import cprint

# cprint("Hello World!", color="blue", on_color="on_yellow", attrs=["bold", "underline"])
