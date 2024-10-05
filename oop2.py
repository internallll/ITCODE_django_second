class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self ):
        print(f'{self.name} едет со скоростью: {self.speed} km/h')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')
class TownCar(Car):
    def __init__(self,speed,color, name):
        super().__init__(speed, color, name)
class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


f = SportCar(220, 'white', 'Ferrarri')
f.go()
f.turn("налево")
