import random

class Domino:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def get_n1(self):
        return self.n1
    
    def get_n2(self):
        return self.n2
    
    def __str__(self):
        return f'n1: {self.n1} n2: {self.n2}'
    

def game():
    values = [0, 1, 2, 3, 4, 5, 6]
    dominoes = []
    players = []

    for value in values:
        for i in range(value + 1):
            dominoes.append(Domino(value, i))
    random.shuffle(dominoes)

    num_players = int(input('Please enter the number of players'))
    for i in range(0, num_players):
        players.append([])

    for j in range(0, len(dominoes) - 2):
        players[j % num_players].append(dominoes[j])

    while True:
        sub_list = []

        print(dominoes[-1])
        for i in range(0, num_players):
            print(f"Player {i+1}'s hand: {', '.join(str(domino) for domino in players[i])}")
            player_hand_index = int(input("Please enter a domino to play otherwise enter -1"))
            if player_hand_index == -1:
                continue
            else:
                if player_hand_index < len(players[i]):
                    sub_list.append(players[i][player_hand_index])
                    players[i].pop(player_hand_index)

            if len(players[i]) == 0:
                print(f'Player {i+1} wins!')
                break
            
        dominoes.append(sub_list)



game()
#TODO: add domino names and adjacency matrix https://www.geeksforgeeks.org/graph-and-its-representations/
