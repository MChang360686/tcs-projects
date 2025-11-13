import random
import math

l = []

def d20():
    return random.randint(1, 20)
    
def d2():
    return random.randint(1, 2)
    
def build_board():
    for i in range(20):
        l.append(0)
        
def print_board():
    print(l)
    
def game():
    build_board()
    lives = 3
    negation = False
    location = 0
    score = 0
    
    while lives > 0:
        if d2() == 1:
            negation = True
        else:
            negation = False
        
        location = d20() - 1
        
        if negation:
            player_location = int(input('Go to !' + str(location) + ' '))
            if player_location == location:
                lives -= 1
                print('You are wrong.  Lose one life')
            else:
                score += 1
        else:
            player_location = int(input('Go to ' + str(location) + ' '))
            if player_location != location:
                lives -= 1
                print('You are in the wrong place.  Lose one life')
            else:
                score += 1
                
    print('Game Over.  Your final score is ' + str(score))
game()
        
            