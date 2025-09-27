import random

map = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

chores = ['take out trash', 'make bed', 'put dishes away', 'wash dishes', 'clean room', 'defrost meat']
player_stats = {'str': 0, 'agi': 0, 'dex': 0, 'con': 0}

def d6():
    return random.randint(1, 6)
    
def move(current_position, destination):
    if map[current_position][destination] == 1:
        return True
    else:
        return False
        
def skill_check(stat):
    bonus = player_stats[stat]
    if d6() + bonus >= 3:
        return True
    else:
        return False
    
def help():
    print('''
          Goal: do your chores before mom gets back.

          
          
          ''')
        
def game():
    
    for _ in range(5):
        choice = input('Enter a stat to allot a point to (str, agi, dex, con): ')
        player_stats[choice] += 1
        
    time = 60 * int(input('enter a difficulty level (1-3)'))
    current_position = 0
    
    while time > 0:
        cmd = input('Choose an action(move, chore, list, help): ')
    