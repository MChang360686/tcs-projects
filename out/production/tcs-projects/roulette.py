import random

def d37():
    return random.randint(0, 36)
    
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
        
def game():
    bets = []
    num_players = int(input('Enter a number of players: '))
    
    for i in range(num_players):
        bet_amt = int(input('Enter an amount to bet: '))
        bet_placement = input('Enter your bet(0-36) or even/odd: ')
        if bet_placement == 'even':
            bets.append([bet_amt, 'even'])
        elif bet_placement == 'odd':
            bets.append([bet_amt, 'odd'])
        else:
            bets.append([bet_amt, int(bet_placement)])
            
    spin = d37()
    
    print(spin)
    
    for i in range(num_players):
        if bets[i][1] == 'even':
            if is_even(spin):
                print('Player ' + str(i+1) + ' wins ' + str(bets[i][0]))
            else:
                continue
        elif bets[i][1] == 'odd':
            if not is_even(spin):
                print('Player ' + str(i+1) + ' wins ' + str(bets[i][0]))
            else:
                continue
        elif bets[i][1] == spin:
            print('Player ' + str(i+1) + ' wins ' + str(bets[i][0] * 35))
            
game()
