import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
    
    def get_color(self):
        return self.color
    
    def get_value(self):
        return self.value
    
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def play_card(self, card_index, card_to_match):
        if self.cards[card_index].get_color() == card_to_match.get_color() or self.cards[card_index].get_value() == card_to_match.get_value():
            self.cards.pop(card_index)
            return True
        else:
            print("Card is invalid")
            return False
        
class Game:
    def __init__(self):
        num_players = int(input("Enter number of players: "))

        colors = ["red", "green", "blue", "yellow"]
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "reverse", "skip", "draw two", "draw four", "wild", "wild draw four"]

        deck = []
        for color in colors:
            for value in values:
                deck.append(Card(color, value))

        random.shuffle(deck)

        hands = {}
        for i in range(0, num_players):
            hands["Player " + str(i + 1)] = Hand()

        for hand in hands:
            for i in range(0, 7):
                hands[hand].add_card(deck.pop())
