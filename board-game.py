import random

class D6:
    def d6():
        return random.randint(1, 6)
    
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
def print_board(board):
    for row in board:
        print(board)

def game():

    n = int(input("Please enter a number of players"))

