import random

d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
car_num = [1, 2, 3, 4, 5, 6, 7]

class Character:
    def __init__(self, name, health, weapon, ammo_count, has_car) -> None:
        self.name = name
        self.health = health
        self.weapon = weapon
        self.ammo_count = ammo_count
        self.has_car = has_car

    def get_health(self):
        return self.health
    
    def set_health(self, amount):
        self.health += amount

    def get_ammo(self):
        return self.ammo_count
    
    def set_ammo(self, amount):
        self.ammo_count += amount

    def get_car(self):
        return self.has_car

  
class Enemy:
    def __init__(self, name, health, weapon) -> None:
        self.name = name
        self.health = health
        self.weapon = weapon

    def get_health(self):
        return self.health
    
    def set_health(self, amount):
        self.health += amount  


def spawn_enemies(name, character):
    number = random.choice(d20)
    if character.get_car() == True:
        number2 = random.choice(car_num)
        print(f"{number} {name} appear in front of you.  You run over {number2} {name} with your car, so only {number - number2} {name} remain")
        number -= number2
    else:
        print(f"{number} {name} appear in front of you")

    return number


def fight(num, character):
    ammo = character.get_ammo

    if ammo >= num:
        print(f"You expend {ammo - num + (random.choice(d20) * 2)} rounds")
    else:
        print(f"You only have {ammo} rounds and {num} enemies, so you run away")


def find_ammo(character):
    num = (random.choice(d20) * 2) + 1
    print(f"You find {num} bullets")
    character.set_ammo(num)
    

if __name__ == '__main__':
    """c = Character("Robert Jr.", 100, "AK-47", 60, False)
    print(c.get_health())
    c.set_health(-10)
    print(c.get_health())"""

    spawn_enemies(input("Please enter a name for an enemy "))
    
