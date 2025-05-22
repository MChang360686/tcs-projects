import random

class Player:
    def __init__(self, name):
        self.name = name

def choose_name():
    return random.choice(['bob', 'rob', 'tobit', 'geurgh', 'aeugh'])

def make_players(num_players):
    return [Player(choose_name()).name for _ in range(num_players)]

def game():

    num_players = int(input('Please enter a number of players'))

    players = make_players(num_players)

    rlgl = random.randint(100, 150)

    not_all_lost = True
    while not_all_lost:
        data = {}
        for player in players:
            data[player] = input('Please enter a number of steps')

        num_valid_steps = random.randint(5, 15)

        for player in players:
            if data[player] <= num_valid_steps:
                continue
            else:
                players.remove(player)

    a = players[:len(players)//2]
    b = players[len(players)//2]

