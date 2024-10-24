import random

x = [1, 2, 3]

def choose_cup():
    return random.choice(x)

def cup_guess_game():
    print('( ) ( ) ( )')
    hidden_num = choose_cup()
    player_guess = input('Guess the cup number (1, 2, 3)')
    if player_guess == str(hidden_num):
        print('Congratulations! You guessed correctly!')
        print('( ) x ( ) ( )')
        return 1
    else:
        print('Not Quite...')
        return 0
    
def game():
    score = 0
    while True:
        score += cup_guess_game()
        print('Score: ' + str(score))
        if input('Play again? (y/n)') == 'y':
            continue
        else:
            break

game()