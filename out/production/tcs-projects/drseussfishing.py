import random

fish = ['1 fish', '2 fish', 'red fish', 'blue fish']

def choose_fish():
    return random.choice(fish)
    
def game():
    num_players = int(input("enter number of players: "))
    scoreboard = {}
    
    for i in range(num_players):
        scoreboard[i] = 0
        
    for player in scoreboard.keys():
        print('Player ' + str(player) + "'s turn ")
        score = 0
        while True:
            input("Hit enter to fish")
            fish = choose_fish()
            print(fish)
            if fish == '1 fish':
                score += 1
            elif fish == '2 fish':
                score += 2
            elif fish == 'red fish':
                score = 0
            elif fish == 'blue fish':
                score += 5
                break
        scoreboard[player] = score
            
    print("Player " + str(max(scoreboard, key=scoreboard.get)) + " wins")
    print(scoreboard)
    
game()