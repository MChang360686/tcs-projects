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
    return random.randint(1, 10)
        
def river():
    diff = ['slow', 'fast', 'rapid']
    river_difficulty = random.randint(0, 2)
    depth = random.randint(1, 15)

    print('You approach a ' + diff[river_difficulty] + ' river.  It is ' + str(depth) + ' feet deep. What do you want to do? ')
    print('1. Ford the river')
    print('2. Caulk your wagon')
    print('3. Wait for a ferry')
    action = int(input('4. Wait '))

    if action == 1:
        if depth >= 3:
            if d10() <= 4:
                return True
            else:
                return False
        else:
            if d10() <= 8:
                return True
            else:
                return False
    
    
        
