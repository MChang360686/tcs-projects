import random

class Player:
    def __init__(self, name, starting_place):
        self.name = name
        self.starting_place = starting_place
        self.score = 0
        self.pieces = []

    def get_active_pieces(self):
        return self.pieces
    
    def add_new_piece(self):
        self.pieces.append(self.starting_place)

    def bump_piece(self, position):
        self.pieces.remove(position)

    def piece_finish(self):
        self.pieces.remove(self.starting_place)
        self.score += 1

def d6():
    return random.randint(1, 6)

def game():
    play = True
    players = {'red': Player('red', 0), 'yellow': Player('yellow', 4), 'green': Player('green', 9), 'blue': Player('blue', 14)}
    board = []
    score_board = []
    for _ in range(20):
        board.append(0)

    while play:
        for player in players:
            input(player + "'s turn, press enter to pop the die")
            print(board)

            num_pieces = len(players[player].get_active_pieces())
            indices = players[player].get_active_pieces()

            roll = d6()
            print(roll)
            if roll == 6:
                choice = input('bring out new piece? (y/n) ')
                if choice == 'y':
                    players[player].add_new_piece()
                    if board[players[player].starting_place] != 0:
                        name = board[players[player].starting_place]
                        position = players[player].starting_place
                        players[name].bump_piece(position)
                    board[players[player].starting_place] = player
                else:
                    print(players[player].get_active_pieces())
                    index_choice = int(input('enter the index of the piece you wish to move '))
                    if index_choice < num_pieces:
                        # check if piece will finish.
                        if indices[index_choice] < players[player].starting_place:
                            if (indices[index_choice] + 6) % 20 >= players[player].starting_place:
                                # replace 0
                                board[indices[index_choice]] = 0
                                players[player].pieces[index_choice] = players[player].starting_place
                                players[player].piece_finish()
                        else:
                            board[indices[index_choice]] = 0
                            players[player].pieces[index_choice] = (players[player].pieces[index_choice] + 6) % 20
                            current_index = players[player].pieces[index_choice]
                            # check if we need to bump a piece
                            if board[players[player].pieces[index_choice]] != 0:
                                players[board[players[player].pieces[index_choice]]].bump_piece(current_index)
                                board[indices[index_choice]] = player
                            else:
                                board[indices[index_choice]] = player
                    else:
                        print('invalid piece index num, turn forfeit')
            else:
                if len(players[player].get_active_pieces()) == 0:
                    continue
                else:
                    print(players[player].get_active_pieces())
                    index_choice = int(input('enter the index of the piece you wish to move '))
                    if index_choice < num_pieces:
                        # check if piece will finish.
                        if indices[index_choice] < players[player].starting_place:
                            if (indices[index_choice] + roll) % 20 >= players[player].starting_place:
                                # replace 0
                                board[indices[index_choice]] = 0
                                players[player].pieces[index_choice] = players[player].starting_place
                                players[player].piece_finish()
                        else:
                            board[indices[index_choice]] = 0
                            players[player].pieces[index_choice] = (players[player].pieces[index_choice] + roll) % 20
                            current_index = players[player].pieces[index_choice]
                            # check if we need to bump a piece
                            if board[players[player].pieces[index_choice]] != 0:
                                players[board[players[player].pieces[index_choice]]].bump_piece(current_index)
                                board[indices[index_choice]] = player
                            else:
                                board[indices[index_choice]] = player
                    else:
                        print('invalid piece index num, turn forfeit')

            if players[player].score == 4:
                score_board.append(player)

            if len(score_board) == 4:
                for i in range(len(score_board)):
                    print(i + '. ' + player)

game()
