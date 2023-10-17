class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    human = Person("Oleg", 40)
    print(human.name)