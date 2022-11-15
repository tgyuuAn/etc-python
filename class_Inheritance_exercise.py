#부모 클래스 car
class car:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.speed = 0
        self.max_speed = None
        self.weight = None
    
    def upSpeed(self, v):
        print(f"{self.name} 의 가속 후 속도 : {min(self.max_speed, self.speed +v)}")
        self.speed = min(self.max_speed, self.speed +v)
    
    def downSpeed(self, v):
        print(f"{self.name} 의 감속 후 속도 : {max(0, self.speed -v)}")
        self.speed = max(0, self.speed -v)
        
#car를 상속받은 자식 클래스 truck
class truck(car):
    def __init__(self,name,color):
        super().__init__(name,color)
        self.max_speed = 100
        self.max_load = 2000
        self.weight =  5000
        self.load = 0
        
    def __str__(self):
        return f"분류 : {self.name}, 중량 : {self.weight}, 최대 속도 : {self.max_speed}, 최대 적재량 : {self.max_load}"
        
    def upLoad(self,load):
        print(f"{self.name} 의 상차 후 적재량 : {min(self.max_load, self.load+load)}")
        self.load = min(self.max_load, self.load+load)
        
    def downLoad(self,load):
        print(f"{self.name} 의 하차 후 적재량 : {max(0, self.load-load)}")
        self.load = max(0, self.load-load)
        
#car를 상속받은 자식 클래스 sedan
class sedan(car):
    def __init__(self,name,color):
        super().__init__(name,color)
        self.num_seat = 5
        self.max_speed = 250
        self.weight = 2000
        
    def __str__(self):
        return f"분류 : {self.name}, 중량 : {self.weight}, 최대 속도 : {self.max_speed}, 좌석 수 : {self.num_seat}"

car1 = truck("봉고","파랑")
car2 = sedan("소나타","검정")

print(car1)
print(car2)
print()

car1.upSpeed(300)
car2.upSpeed(300)
print()

car1.downSpeed(200)
car2.downSpeed(200)
print()

car1.upLoad(3000)
car1.downLoad(1000)
print()