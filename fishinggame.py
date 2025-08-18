import random

class Fish:
    def __init__(self, length, weight, species):
        self.length = length
        self.weight = weight
        self.species = species
        
    def get_length(self):
        return self.length
    
    def get_weight(self):
        return self.weight

    def get_species(self):
        return self.species
    
class Player:
    def __init__(self):
        self.fish = []
        self.rod = 'old'
        self.line = 'cheap'
        self.bait = {}
        self.money = 0

    def set_rod(self, rod_quality):
        self.rod = rod_quality

    def set_line(self, line_quality):
        self.line = line_quality
        
def create_map():
    map = []
    for i in range(3):
        map.append([])
        for _ in range(3):
            map[i].append(0)
            
    return map

def print_map(map):
    for row in map:
        print(row)

def spawn_fish(map):
    num_fish = random.randint(1, 3)
    for i in range(num_fish):
        for j in range(len(map[i])):
            map[i][j] = Fish(random.randint(2, 8), random.randint(4, 25), random.choice["minnow", "pike"])
    
def shop(player, player_money):
    cmd = input("Please enter what you'd like to do: ")
    if cmd == 'sell':
        for i in range(len(player.fish), -1, -1):
            player_money += player.fish[i].weight * 1.25
            player.fish.pop(i)
    elif cmd == 'buy':
        cmd2 = input("Please enter what you'd like to buy(rod, line, bait): ")
    else:
        
            
        
        