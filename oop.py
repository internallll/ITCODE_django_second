class TownCar:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self ):
        print(f'{self.name} поехала со скоростью: {self.speed} km/h')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')

class SportCar:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self ):
        print(f'{self.name} поехала со скоростью: {self.speed} km/h')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')

class WorkCar:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self ):
        print(f'{self.name} поехала со скоростью: {self.speed} km/h')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')

class PoliceCar:
    def __init__(self, speed, color, name, is_police = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self ):
        print(f'{self.name} поехала со скоростью: {self.speed} km/h')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')

vaz2114 = TownCar(100, 'white', 'Chetyrka')
vaz2114.go()
vaz2114.stop()
vaz2114.turn('налево')

print()

DPS = PoliceCar(120, 'white-blue', 'Camry')
DPS.go()