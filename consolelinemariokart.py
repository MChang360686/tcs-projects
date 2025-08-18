import random

def d6():
    return random.randint(1, 6)

def item_box(num):
    return ["mushroom", "star", "blue shell", "banana", "pirhana plant", "blooper squid"][num - 1]

def find_first(list):
    for i in range(len(list) - 1, -1, -1):
        if list[i] != 0:
            return list[i]
        else:
            continue

def game():
    num_players = int(input("Please enter the number of players"))
    players = {}
    win = False
    board = []
    immune = []

    for i in range(1, num_players + 1):
        players['Player ' + str(i)] = 0

    for i in range(0, 30):
        board.append(0)

    while win != True:
        blinded = False
        for player in players:
            if not blinded:
                print(board)
            roll = d6()
            print(roll)
            board[players[player]] = 0
            players[player] += roll
            
            if players[player] >= 29:
                win = True
                print(player + ' wins!')
            else:
                board[players[player]] = player

            if players[player] in [5, 10, 15, 20, 25]:
                for _ in range(2):
                    item = item_box(d6())

                    if item == 'mushroom':
                        players[player] += 2
                    elif item == 'star':
                        immune.append(player)
                    elif item == 'blue shell':
                        first = find_first(board)
                        if first in immune:
                            immune.remove(first)
                        else:
                            players[first] -= 4
                    elif item == 'banana':
                        random_player = random.choice(list(players.keys()))
                        players[random_player] -= 1
                    elif item == 'pirhana plant':
                        continue
                    elif item == "blooper squid":
                        blinded = True

game()
