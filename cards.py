import random

class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def get_suit(self):
        return self.suit
    
    def get_val(self):
        return self.val
    
def make_deck():
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    deck = []

    for suit in suits:
        for value in values:
            deck.append(Card(suit, value))

    random.shuffle(deck)
    return deck

def draw_card(deck):
    return deck.pop()

def war_game():

    deck = make_deck()
    player1 = []
    player2 = []

    for i in range(0, 26):
        player1.append(draw_card(deck))
        player2.append(draw_card(deck))

    while len(player1) > 0 and len(player2) > 0:

        p1 = player1.pop(0)
        p2 = player2.pop(0)
        x = input('Press enter to continue')
        print(p1.get_val(), p1.get_suit(), p2.get_val(), p2.get_suit())

        if p1.get_val() > p2.get_val():
            player1.append(p1)
            player1.append(p2)
            print("Player 1 wins the round")
        elif p2.get_val() > p1.get_val():
            player2.append(p1)
            player2.append(p2)
            print("Player 2 wins the round")
        else:
            player1.append(p1)
            player1.append(p2)

    if len(player1) == 52:
        print("Player 1 wins")
    elif len(player2) == 52:
        print("Player 2 wins")

war_game()