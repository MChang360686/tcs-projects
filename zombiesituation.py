import random

zombies = ['basic']

map = [[], [], []]

class Zombie:
    def __init__(self, health, speed):
        self.health = health
        self.speed = speed

def build_map():
    for lane in map:
        for i in range(11):
            lane.append(' ')

def print_map():
    for lane in map:
        print(lane)

def spawn_zombie(difficulty):
    zombie = zombies[random.randint(0, difficulty)]
    lane = random.randint(0, 2)
    map[lane][10] = zombie

def move_zombies():
    for lane in map:
        for i in range(10, 1, -1):
            if lane[i] != ' ':
                lane[i-1] = lane[i]
                lane[i] = ' '

def check_game_over():
    for lane in map:
        if lane[0] != '0' and lane[0] != ' ':
            return True