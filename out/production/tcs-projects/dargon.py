import random

map = [['', '', ''], ['', '', ''], ['', '', '']]

class Character:
    def __init__(self, str, health, agi, speed, dex):
        self.str = str
        self.health = health
        self.agi = agi
        self.speed = speed
        self.dex = dex
        x_pos = 1
        y_pos = 1

    def get_str(self):
        return self.str

    def get_health(self):
        return self.health

    def get_agi(self):
        return self.agi

    def get_speed(self):
        return self.speed

    def get_dex(self):
        return self.dex

    def set_health(self, amount):
        self.health = amount

    def set_str(self, amount):
        self.str = amount

    def set_agi(self, amount):
        self.agi = amount

    def set_speed(self, amount):
        self.speed = amount

    def set_dex(self, amount):
        self.dex = amount
        
    def move(self):
        direction = input("Please enter a direction")
        
        if direction == 'left' and x_pos > 0:
            map[y_pos][x_pos] = ''
            x_pos -= 1
            map[y_pos][x_pos] = 'P'
        elif direction == 'right' and x_pos < len(map[y_pos]) - 1:
            map[y_pos][x_pos] = ''
            x_pos += 1
            map[y_pos][x_pos] = 'P'
        elif direction == 'up' and y_pos > 0:
            map[y_pos][x_pos] = ''
            y_pos -= 1
            map[y_pos][x_pos] = 'P'
        elif direction == 'down' and y_pos < len(map) - 1:
            map[y_pos][x_pos] = ''
            y_pos += 1
            map[y_pos][x_pos] = 'P'
            


class Party:
    def __init__(self):
        self.members = []
        self.size = 0

    def add_member(self, member):
        self.members.append(member)
        self.size += 1

    def rem_member(self, member):
        self.members.remove(member)
        self.size -= 1


class Enemy(Character):
    def __init__(self, str, health, agi, speed, dex):
        super().__init__(str, health, agi, speed, dex)

    def get_spec(self):
        return self.spec

    def set_spec(self, spec):
        self.spec = spec


class Loot:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def set_name(self):
        choices = ["a coin", "two coins", "four coins", "eight coins", "sixteen coins"]
        self.name = random.choice(choices)

    def set_value(self):
        if self.name == "a coin":
            self.value = 1
        elif self.name == "two coins":
            self.value = 2
        elif self.name == "four coins":
            self.value = 4
        elif self.name == "eight coins":
            self.value = 8
        elif self.name == "sixteen coins":
            self.value = 16

def print_map():
    for row in map:
        print(row)
        
        
