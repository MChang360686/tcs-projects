import random

graph = []

def create_graph():
    for i in range(5):
        sublist = []
        for j in range(5):
            sublist.append(0)
        
        graph.append(sublist)

def print_graph():
    for sublist in graph:
        print(sublist)

def connect(a, b):
    if a < len(graph) and b < len(graph):
        graph[a][b] = 1
        graph[b][a] = 1
    else:
        print('Invalid vertices')

def game():
    create_graph()

    for i in range(0, 4):
        for i in range(0, 5):
            connect(i, random.randint(0, 4))

    print_graph()

    rooms_visited = []
    starting_room = random.randint(0, 4)
    rooms_visited.append(starting_room)
    print(starting_room)

    while len(rooms_visited) < 5:
        print(graph[starting_room])
        move = int(input('Enter a room to move to '))

        if move == random.randint(0, 4):
            print("The monster got you")
            break
        else:
            starting_room = move
            if starting_room not in rooms_visited:
                rooms_visited.append(move)
            if len(rooms_visited) >= 5:
                print('YOU WIN')
                break
            
game()