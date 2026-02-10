import random

class NPC:
    def __init__(self, name=random.choice(['bob', 'rob', 'job'])):
        self.name = name
        self.player_class = random.choice(['b', 'f', 'w'])
        self.str = 10
        self.dex = 10
        self.con = 10
        self.int = 10
        self.wis = 10
        self.cha = 10
        self.hp = self.set_health()
        
    def set_health(self):
        if self.player_class == 'b':
            return self.con + 12
        elif self.player_class == 'f':
            return self.con + 10
        elif self.player_class == 'w':
            return self.con + 6
            
    def set_hp(self, amt):
        if self.hp - amt < 1:
            self.hp = 0
        else:
            self.hp -= amt
            
    def __str__(self):
        return f'Name: {self.name} str: {self.str} dex: {self.dex}'
        
n = NPC()
print(n.hp)