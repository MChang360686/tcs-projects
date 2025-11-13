import random

class Card:
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value
        
    def __str__(self):
        return self.name + ' of ' + self.suit

class Shoe:
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        names = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
        self.cards = []
        self.discard_pile = []
        for i in range(6):
            for j in range(4):
                suit = suits[j]
                for k in range(13):
                    self.cards.append(Card(suit, names[k], values[k]))
                    
        random.shuffle(self.cards)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        card = self.cards[0]
        self.cards.pop(0)
        return card
        
    def discard(self, card):
        self.cards.append(card)
        
    def reshuffle(self):
        self.cards.extend(self.discard)
        random.shuffle(self.cards)
        
class Player():
    def __init__(self, name):
        self.name = 'Player ' + str(name)
        self.money = 2500
        
def game():
    
    def __init__(self):
        shoe = Shoe()
        players = []
        for i in range(14):
            players.append()