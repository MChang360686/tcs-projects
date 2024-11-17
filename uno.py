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
        
class Deck:
    def __init__(self):
        self.cards = []
        colors = ["red", "green", "blue", "yellow"]
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "reverse", "skip", "draw two", "draw four", "wild", "wild draw four"]

        deck = []
        for color in colors:
            for value in values:
                deck.append(Card(color, value))

        random.shuffle(deck)

    def deal_card(self):
        return self.cards.pop(0)
    
    def return_cards(self, cards):
        # shuffle in list of cards
        for card in cards:
            self.cards.append(card)

        random.shuffle(self.cards)

    
        
class Game:
    def __init__(self):
        num_players = int(input("Enter number of players: "))

        deck = Deck()
        discard_pile = []

        players_hands = {}
        for i in range(0, num_players):
            players_hands["Player " + str(i + 1)] = Hand()

        for hand in players_hands:
            for i in range(0, 7):
                players_hands[hand].add_card(deck.pop())


    """
    Go to target player.  Let them play a card.  If they
    """
    def turn(self, current_player_number):
        player_card_index = input("Please enter a card index number: ")
        player_card = self.players_hands["Player 1"].cards[player_card_index]

        if player_card.get_color() == self.pile[0].get_color() or player_card.get_value() == self.pile[0].get_value():
            self.players_hands["Player " + str(current_player_number)].play_card(player_card_index, self.pile[0])
        elif player_card.get_value() == "wild":
            self.players_hands["Player " + str(current_player_number)].play_card(player_card_index, self.pile[0])
        elif player_card.get_value() == "wild draw four":
            self.players_hands["Player " + str(current_player_number)].play_card(player_card_index, self.pile[0])
            self.players_hands["Player " + str(current_player_number + 1)].add_card(self.deck[0])


    # Setup the game
    def play_game(self):
        pass