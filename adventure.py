import random

d6 = [1, 2, 3, 4, 5, 6]

class Character:

    def __init__(self, sta, str, agi, int, cha):
        self.sta = sta
        self.str = str
        self.agi = agi
        self.int = int
        self.cha = cha

    def get_str(self):
        return self.str

    def set_str(self, amt):
        self.str = amt    

def get_d6():
    return random.choice(d6)

bob = Character(3, 4, 5, 2, get_d6())