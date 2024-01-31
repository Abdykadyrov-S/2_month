class SmartPhone():
    def __init__(self, sim_cards, battery):
        self.__sim_cards = sim_cards
        self._battery = battery

    @property
    def sim_cards(self):
        return self.__sim_cards

    @sim_cards.setter
    def sim_cards(self, new_sim_cards):
        self.__sim_cards = new_sim_cards

    def __info_smartphone(self):
        print(f"Ваши сим карты {self.sim_cards} , ваш объём батареи {self._battery}")

    @property
    def info_smartphone(self):
        return self.__info_smartphone
    
mi = SmartPhone(["MegaCom", "O!"], 3000)
mi.info_smartphone()


def test(value):
    def order():
        print("Hello World")
        value()
        print("End")
    return order

@test
def hi():
    print("Hi")

hi()



# Множественное наследование

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def info(self):
        print(f"Бренд машины - {self.model}, год выпуска - {self.year}")

class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.battery = battery

    def drive(self):
        print(f"{self.model}, едет на электричестве")
    

class FuelCar(Car):
    def __init__(self, model, year, fuel_bank):
        Car.__init__(self, model, year)
        self.fuel_bank = fuel_bank

    def drive(self):
        print(f"{self.model}, едет на Топливо!")

class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, fuel_bank, battery,):
        FuelCar.__init__(self, model, fuel_bank)
        ElectricCar.__init__(self, model, battery)

    def drive(self):
        print(f"{self.model}, едет на Топливо! и на электричечтве")

tesla = ElectricCar("Tesla Model X", 2022, 150000)
tesla.info()
tesla.drive()

audi = FuelCar("Rs-8", 2018, 15)
audi.info()
audi.drive()

toyota = HybridCar("Avalon", 2023, 100000, 10)
toyota.info()
toyota.drive()