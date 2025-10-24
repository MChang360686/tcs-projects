import random
import math

money = 2000
stock = {'wood': 0, 'steel': 0, 'cement': 0, 'gravel': 0}
materials_owned = {'wood': 0, 'steel': 0, 'cement': 0, 'gravel': 0}
blueprints = ['sidewalk', 'foundation', 'house']

def d6():
    return random.randint(1, 6)
    
def d100():
    return random.randint(1, 100)

def offer():
    return random.randint(500, 40000)

def has_materials(project_name):
    if project_name == 'sidewalk':
        if materials_owned['gravel'] >= 5 and materials_owned['cement'] >= 5:
            return True
        else:
            False
    elif project_name == 'foundation':
        if materials_owned['gravel'] >= 5 and materials_owned['cement'] >= 5 and materials_owned['steel'] >= 5:
            return True
        else:
            False
    elif project_name == 'house':
        if materials_owned['gravel'] >= 5 and materials_owned['cement'] >= 5 and materials_owned['steel'] >= 3 and materials_owned['wood'] >= 20:
            return True
        else:
            False
    
def shop():
    for item in stock:
        stock[item] = d100()
    print(stock)
    while True:
        cmd = input('Enter a product to purchase')
        if cmd in stock.keys():
            amt = int(input('Enter an amount to purchase'))
            if stock[cmd] <= amt:
                materials_owned[cmd] = stock[cmd]
                stock[cmd] = 0
            else:
                stock[cmd] -= amt
                materials_owned[cmd] = amt
        else:
            print('invalid item')

def build():
    print(blueprints)
    cmd = input("Please enter the name of what you want to build: ")
    if cmd in blueprints:
        if cmd == 'sidewalk' and has_materials(cmd):
            materials_owned['gravel'] -= 5
            materials_owned['cement'] -= 5
        elif cmd == 'foundation' and has_materials(cmd):
            materials_owned['gravel'] -= 5
            materials_owned['cement'] -= 5
            materials_owned['steel'] -= 5
        elif cmd == 'house' and has_materials(cmd):
            materials_owned['gravel'] -= 5
            materials_owned['cement'] -= 5
            materials_owned['steel'] -= 3
            materials_owned['wood'] -= 20
    else:
        print('Invalid blueprint name')



