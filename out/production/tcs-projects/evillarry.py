import random

SIZE = 6
map = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

player_has_key = False
player_has_food = False
door_unlocked = False

def print_map():
    for row in map:
        print(row)
    print()

def find_player():
    for i in range(SIZE):
        for j in range(SIZE):
            if map[i][j] == 'P':
                return i, j

def prepare_map():
    map[2][5] = 'D'

    items = ['K', 'F', 'EL', 'P']
    for item in items:
        while True:
            x = random.randint(0, SIZE - 1)
            y = random.randint(0, SIZE - 1)
            if map[x][y] == 0:
                map[x][y] = item
                break

def move_player(dx, dy):
    global player_has_key, player_has_food, door_unlocked

    x, y = find_player()
    nx, ny = x + dx, y + dy

    if not (0 <= nx < SIZE and 0 <= ny < SIZE):
        print("You hit a wall.")
        return False

    target = map[nx][ny]

    if target == 'K':
        player_has_key = True
        print("You picked up the key")

    elif target == 'F':
        player_has_food = True
        print("You picked up food")

    elif target == 'D':
        if player_has_key:
            door_unlocked = True
            print("You unlocked the door")
        else:
            print("The door is locked.")
            return False

    elif target == 'EL':
        if player_has_food and door_unlocked:
            print("You fed Evil Larry")
            print("YOU WIN!")
            return True
        else:
            print("Evil Larry eats YOU")
            print("GAME OVER")
            return True

    map[x][y] = 0
    map[nx][ny] = 'P'
    return False

def game():
    print("Welcome to EVIL LARRY")
    print("W/A/S/D to move. Find the key, unlock the door, feed Larry.\n")

    while True:
        print_map()
        move = input("Move (W/A/S/D): ").lower()

        if move == 'w':
            end = move_player(-1, 0)
        elif move == 's':
            end = move_player(1, 0)
        elif move == 'a':
            end = move_player(0, -1)
        elif move == 'd':
            end = move_player(0, 1)
        else:
            print("Invalid move.")
            continue

        if end:
            break

prepare_map()
game()
