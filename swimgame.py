import random

class Swimmer:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
        
pool = [[], []]

def build_pool():
    for i in range(21):
        pool[0].append(' ')
        pool[1].append(' ')

def print_pool():
    for lane in pool:
        print(lane)
        
def d6():
    return random.randint(1, 6)
    
def game():
    build_pool()
    pool[0][0] = 'a'
    pool[1][0] = 'b'
    player_index = 0
    cpu_index = 0
    player_name = input('Please enter a name: ')
    player = Swimmer(player_name)
    
    while True:
        print_pool()
        input("Hit enter to roll die ")
        player_roll = d6()
        pool[0][player_index] = ' '
        player_index += player_roll
        
        cpu_roll = d6()
        pool[1][cpu_index] = ' '
        cpu_index += cpu_roll
        
        if player_index >= 20:
            print(f'{player.get_name()} wins!')
            break
        elif cpu_index >= 20:
            print('CPU wins!')
            break
        else:
            pool[0][player_index] = 'a'
            pool[1][cpu_index] = 'b'

game()