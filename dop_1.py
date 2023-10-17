# class CamelCase: # чертеж
#     # pass
#     def __init__(self, name):
#         self.__name = name
    
    

# a = CamelCase("ВерблюжийРегистр")



def first_dec(a):
    def write():
        print("Сообщение до запуска функции")
        a()
        print("Сообщение после запуска функции")
    return write

@first_dec
def say_hello():
    print("Hello World!")
say_hello()