import random
import math

class Player:
    def __init__(self, stre, end, agi, dex, spd, luck):
        self.stre = stre
        self.end = end
        self.agi = agi
        self.dex = dex
        self.spd = spd
        self.luck = luck
        self.main_arm = ""
        self.side_arm = ""
        
    def get_stre(self):
        return self.stre
        
    def set_stre(self, amt):
        self.stre += amt
        
    def get_end(self):
        return self.end
        
    def set_end(self, amt):
        self.end += amt
        
    def get_agi(self):
        return self.agi
        
    def set_agi(self, amt):
        self.agi += amt
        
    def get_dex(self):
        return self.dex
        
    def set_dex(self, amt):
        self.dex += amt
        
    def get_spd(self):
        return self.spd
        
    def set_spd(self, amt):
        self.spd += amt
        
    def get_luck(self):
        return self.luck
        
    def set_luck(self, amt):
        self.luck += amt
        
class Weapon:
    def __init__(self, name, dmg, rng):
        self.name = name
        self.dmg = dmg
        self.rng = rng
        
    def get_name(self):
        return self.name
        
    def get_dmg(self):
        return self.dmg
        
    def get_rng(self):
        return self.rng
        
class Zombie:
    def __init__(self, zombie_type, spd, hp, dmg):
        self.zombie_type = zombie_type
        self.spd = spd
        self.hp = hp
        self.dmg = dmg
        
    def get_type(self):
        return self.zombie_type
        
    def get_spd(self):
        return self.spd
        
    def get_hp(self):
        return self.hp
        
    def get_dmg(self):
        return self.dmg
        
def d100():
    return random.randint(1, 100)
    
def d6():
    return random.randint(1, 6)
    
def make_zombie(num_zombies):
    types = {1: 'normal', 2: 'fast', 3: 'fat', 4: 'armed', 5: 'fat + armed', 6: 'fast + fat', 7: 'police', 8: 'military'}
    