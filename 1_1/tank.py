class Tank:
    count=0
    def __init__(self, x, y, model="Т-14 Армата", ammo=100):
        Tank.count+=1
        self.model=model
        self.hp=100
        self.xp=0
        self.ammo=ammo
        self.fuel=100
        self.x=x
        self.y=y
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0

    def fire(self):
        if self.ammo>0:
            self.ammo-=1
            print("Стреляю")

    def forvard(self):
        if self.fuel>0:
            self.y+=-1
            self.fuel-=1
    def backward(self):
        if self.fuel>0:
            self.y+=1
            self.fuel-=1
    def left(self):
        if self.fuel>0:
            self.x+=-1
            self.fuel-=1
    def right(self):
        if self.fuel>0:
            self.x+=1
            self.fuel-=1
    def __str__(self):
        return (f"Модель:{self.model}, Здоровье:{self.hp}, "
              f"Опыт:{self.xp}, Патроны:{self.ammo}, "
              f"Координаты:({self.x},{self.y})")



