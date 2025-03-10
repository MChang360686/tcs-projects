import random

d6 = [1, 2, 3, 4, 5, 6]
d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Party:

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
        

def roll_d6():
    return random.choice(d6)

def roll_d10():
    return random.choice(d10)

def game():
    p = Party(10, 10, 10, 100, 4)

    while p.oxen > 0:
        d10 = roll_d10()
        match(d10):
            case 1:
                print("a wild animal appears")
                if p.get_ammo() < 1:
                    p.oxen -= 1
                else:
                    p.set_ammo(-1)
            case 2:
                print("You find some food")
                p.set_food(2)
            case 3:
                print("You buy more supplies")
                p.set_ammo(5)
                p.set_food(5)
            case _:
                print("nothing happens")

    print("Game is over, you ran out of oxen.")

game()