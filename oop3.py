import random

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, Person):
        damage_index = random.randint(0, len(self.damage)-1)
        if (Person.armor <= 0):
            Person.health -= self.damage[damage_index]
            print(f'{self.name} нанес {self.damage[damage_index]} урона {Person.name} по здоровью')
        elif (Person.armor < self.damage[damage_index]):
            Person.health -= self.damage[damage_index] - Person.armor
            Person.armor = 0
            print(f'{self.name} нанес {self.damage[damage_index]} урона {Person.name} по здоровью')
        else:
            Person.armor -= self.damage[damage_index]
            print(f'{self.name} нанес {self.damage[damage_index]} урона {Person.name} по броне')


    def attack(self, Person):
        self._calculate_damage(Person)


class Player(Person):
   def __init__(self,name, health, damage, armor):
       super().__init__(name, health,damage, armor)


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


pl = Player('Ruslan',100, [1,24,5,3,87,5,8],100) #список дамага это как бы возможность сделать крит, ульту и тд и тп, думаю так поинтереснее
en = Enemy('Goblin', 100, [3,5,6,7,45,8], 100)


def menu():
    print('Добро пожаловать на СМЕРТЕЛЬНУЮ БИТВУ')
    print('1. Начать бой!')
    print('2. Выход')
    n = input()
    return n

def battle(n, player, enemy):
    fl = True
    while(fl):
        if (n == '1'):
            player.attack(enemy)
            enemy.attack(player)
            if player.health < 0:
                print(f'Победил {enemy.name}!')
                fl = False
            elif (enemy.health <= 0):
                print(f'Победил {player.name}!')
                fl = False

        elif (n == '2'):
            return 0
        else:
            print('Некорректный ввод, попробуйте еще раз')
            return battle(menu(), pl, en)
    return 0

battle(menu(), pl, en)





