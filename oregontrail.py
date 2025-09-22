import random

class Player:

    def __init__(self, food, ammunition, tools, money, oxen):
        self.food = food
        self.ammunition = ammunition
        self.tools = tools
        self.money = money
        self.oxen = oxen

    def get_food(self):
        return self.food

    def set_food(self, amt):
        self.food += amt

    def get_ammo(self):
        return self.ammunition
    
    def set_ammo(self, amt):
        self.ammunition += amt
    
    def get_tools(self):
        return self.tools
    
    def set_tools(self, amt):
        self.tools += amt
 
def d10():
    random.randint(1, 10)
        
def river():
    diff = ['slow', 'fast', 'rapids']
    river_difficulty = random.randint(0, 2)

    
    
        
