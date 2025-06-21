import random

def get_num():
    return random.randint(1, 100)
    
def reduce(num):
    return num % 4
    
def game():
    players = []
    num_players = int(input('Enter a number of players'))
    
    for i in range(num_players):
        guess = int(input('Player ' + str(i) + ' guess'))
        players.append(guess)
    
    num = get_num()
    num = reduce(num)
    
    for i in range(num_players):
        if players[i] % 4 == num:
            print('Player ' + str(i) + ' wins')
        else:
            print('Player ' + str(i) + ' was wrong')
            
game()
    
    
    
