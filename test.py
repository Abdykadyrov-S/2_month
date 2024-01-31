
class Constryktor: 
    def __init__(self,floor,place, room): 
        self.floor = floor
        self.place = place 
        self.room = room
        
    def __str__(self,): 
        return f"ваш дом в {self.place} c {self.floor} этожами и {self.room} комнатами "
    def build(self, build_floor):
        self.build_floor = build_floor
        if self.floor == self.build_floor: 
            print("ваш дом был успешно построе ")
        elif self.floor != self.build_floor:
            print("ваш дом ешо строется ")
         
        
  
rty = Constryktor(4,"osh",3)
print(rty)
rty.build(2)  