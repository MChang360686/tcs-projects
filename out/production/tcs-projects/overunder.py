import random
import math

class Player:

    def __init__(self, name, action_bet_on):
        self.name = name
        self.score = 0
        self.action = action_bet_on
        self.avg = random.randint(10, 30)

    def __str__(self):
        return f'{self.name} has {self.score} {self.action}s '
    
    def get_name(self):
        return self.name
    
    def get_action(self):
        return self.action
    
    def get_score(self):
        return self.score
    
    def set_score(self, amt):
        self.score += amt

    def __str__(self):
        return f'{self.name} {self.avg}'
    
def check_score(player, bet_value, higher):
    if higher:
        if player.get_score() > bet_value:
            return True
        else:
            return False
    else:
        if player.get_score() < bet_value:
            return True
        else:
            return False
        
def generate_players():
    names = ['bob', 'rob', 'job']
    action = input('Enter an action to bet on (points, rebounds): ')
    return [Player(random.choice(names), action) for i in range(random.randint(5, 10))]
        
def game():
    while True:
        bet_amt = int(input('Enter an amount to bet: '))
        players = generate_players()
        for player in players:
            print(player)
        player = players[int(input(f'Enter a choice (0 - {len(players) - 1}) '))]
        high_or_low = input('Higher or Lower? ')
        if high_or_low.lower() == 'higher':
            high_or_low = True
        else:
            high_or_low = False

        bar = float(player.avg) + .5

        actual = random.randint(10, 30)
        print(f'Actual score: {actual}')

        if actual > bar:
            if high_or_low == True:
                print('You win')
            else:
                print('You Loose')
        else:
            if high_or_low == False:
                print('You win')
            else:
                print('You Lose')

game()    
