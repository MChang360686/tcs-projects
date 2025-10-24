import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

taken_spots = {}

def print_board():
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("-----------")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("-----------")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def move(a, b, marker):
    if tuple([a, b]) not in taken_spots:
        taken_spots[tuple([a, b])] = True
        board[a][b] = marker
    else:
        print("Invalid move")

def check_winner():
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return False

def game():
    
    win = check_winner()

    while win == False:
        print_board()

        a = int(input("Enter row: "))
        b = int(input("Enter column: "))
        move(a, b, 'X')
        win = check_winner()
        if win:
            print_board()
            print(f'{win} wins')
            break
        else:
            move(random.randint(0, 2), random.randint(0, 2), 'O')
        win = check_winner()

game()