import random

d6 = [1, 2, 3, 4, 5, 6]
d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

class Character:

    def __init__(self, sta, str, agi, int, cha):
        self.sta = sta
        self.str = str
        self.agi = agi
        self.int = int
        self.cha = cha

    def get_sta(self):
        return self.sta
    
    def set_sta(self, amt):
        self.sta = amt

    def get_str(self):
        return self.str

    def set_str(self, amt):
        self.str = amt 

    def get_agi(self):
        return self.agi

    def set_agi(self, amt):
        self.agi = amt

    def get_int(self):
        return self.int

    def set_int(self, amt):
        self.int = amt

    def get_cha(self):
        return self.cha
    
    def set_cha(self, amt):
        self.cha = amt

class Enemy:

    def __init__(self, type):
        match (type):
            case "goblin":
                self.sta = 2
                self.str = 3
                self.agi = 5
                self.int = 3
                self.cha = 1
            case "dragon":
                self.sta = 8
                self.str = 10
                self.agi = 6
                self.int = 4
                self.cha = 3
            case _:
                self.sta = get_d6()
                self.str = get_d6()
                self.agi = get_d6()
                self.int = get_d6()
                self.cha = get_d6()
            

    def get_sta(self):
        return self.sta
    
    def set_sta(self, amt):
        self.sta = amt

    def get_str(self):
        return self.str

    def set_str(self, amt):
        self.str = amt 

    def get_agi(self):
        return self.agi

    def set_agi(self, amt):
        self.agi = amt

    def get_int(self):
        return self.int

    def set_int(self, amt):
        self.int = amt

    def get_cha(self):
        return self.cha
    
    def set_cha(self, amt):
        self.cha = amt

def get_d6():
    return random.choice(d6)

def get_d20():
    return random.choice(d20)

goblin_bob = Enemy("goblin")    
print(goblin_bob.get_str())

dragon_alice = Enemy("dragon")
print(dragon_alice.get_str())