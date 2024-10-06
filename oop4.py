class ToyFactory:
    def __init__(self, name):
        self.name = name

    def buy_materials(self):
        print('Произведена закупка для изготовления')

    def creation_toys(self):
        print('Произведена основная часть работы')

    def paint(self):
        print('Произведена покраска')

    def produce_toys(self, toy_type, name):
        if toy_type == 'Doll':
            self.buy_materials()
            self.creation_toys()
            self.paint()

            toy = Doll(name)
            return toy

        elif toy_type == 'Robot':
            self.buy_materials()
            self.creation_toys()
            self.paint()

            toy = Robot(name)
            return toy

        else:
            raise ValueError ("Неизвестный тип")

class Toy:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'Name: {self.name}')
        print(f'Type: {self.self_type}')

class Robot(Toy):
    def __init__(self, name):
        super().__init__(name)
        self.self_type = 'Robot'

class Doll(Toy):
    def __init__(self, name):
        super().__init__(name)
        self.self_type = ('Doll')

factory = ToyFactory('Fabric')

toy = factory.produce_toys('Doll', 'Elena')
print()
toy.show()

print()

toy2 = factory.produce_toys('Robot', 'Optimus Prime')
print()
toy2.show()
