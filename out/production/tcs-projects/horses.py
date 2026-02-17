import random

class Horse:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return 'Name: ' + self.name + ' Age: ' + str(self.age)

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 5000

    def change_money(self, amt):
        self.money += amt

    def __str__(self):
        return self.name
    
        
def make_horses() -> list:
    return [Horse(random.choice(['bobere', 'job', 'CHUNK', 'Junade']), random.randint(1, 3)) for _ in range(5)]

def game():
    horses = make_horses()
    players = {}
    num_players = int(input('Enter the number of players: '))

    for i in range(1, num_players+1):
        players['Player ' + str(i)] = [Player('Player ' + str(i)), None, 0]

    while True:
        for horse in horses:
            print(horse)

        for player in players:
            players[player][1] = input('Enter a horse name to bet on: ')
            bet_amt = int(input(player + ' Enter an amount of money to bet: '))
            players[player][0].change_money(-bet_amt)
            players[player][2] = bet_amt

        winner = random.choice(horses)

        for player in players:
            if players[player][1] == winner.name:
                print('Player ' + player + ' won $' + str(players[player][2]))
                players[player][0].change_money(players[player][2])
                players[player][2] = 0
            else:
                print('Player ' + player + ' lost $' + str(players[player][2]))
                players[player][2] = 0

game()
