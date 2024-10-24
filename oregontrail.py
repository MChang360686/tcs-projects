import random

d6 = [1, 2, 3, 4, 5, 6]
d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
events = []

class Party:

    def __init__(self, food, ammunition, tools, money, oxen):
        self.food = food
        self.ammunition = ammunition
        self.tools = tools
        self.money = money
        self.oxen = oxen
        self.ration = 'filling'
        self.pace = 'steady'

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
        

def roll_d6():
    return random.choice(d6)

def roll_d10():
    return random.choice(d10)

def choose_background(party_obj):
    print("bucolic, baker, banker, blacksmith")
    bg = input("Please choose a background")
    match(bg):
        case 'bucolic':
            party_obj.set_oxen(2)
        case 'baker':
            party_obj.set_food(200)
        case 'banker':
            party_obj.set_money(500)
        case 'blacksmith':
            party_obj.set_tools(15)


def event():
    d10 = roll_d10()

    match(d10):
        case 1:
            print("a wild animal appears")
        case 2:
            print("a wild animal appears")
        case 3:
            print("a wild animal appears")
        case 4:
            print("a wild animal appears")
        case 5:
            print("a wild animal appears")
        case 6:
            print("a wild animal appears")
        case 7:
            print("a wild animal appears")
        case 8:
            print("a wild animal appears")
        case 9:
            print("a wild animal appears")
        case 10:
            print("a wild animal appears")
        case _:
            print("a wild animal appears")

def game():
    pass