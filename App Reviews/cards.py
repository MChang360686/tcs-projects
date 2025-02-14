import random

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"
    
class Deck():
    def __init__(self):
        self.deck = []
        self.discard = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

        random.shuffle(self.deck)
                
    def shuffle(self):
        random.shuffle(self.deck)

    def get_deck_len(self):
        return len(self.deck)
    
    def draw_card(self):
        return self.deck.pop(0)
    
    def discard_card(self, card):
        self.discard.append(card)

    def re_shuffle(self):
        self.deck.extend(self.discard)

class Player():
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.hand = []

class Table():
    def __init__(self, num_players, starting_money):
        players = {}
        for i in range(0, num_players):
            players[f"Player {i+1}"] = Player(f"Player {i+1}")
            players[f"Player {i+1}"].money = starting_money

'''
Blackjack
'''
class BlackJack():

    def __init__(self):
        n_players = int(input('Please enter a number of players'))
        s_money = int(input('Please enter a starting amount of money for each player'))

        self.table = Table(num_players=n_players+1, starting_money=s_money)
        self.deck = Deck()

        bets = {'dealer': 100000}

    def deal_hand(self):
        for player in self.table.players:
            for i in range(0, 2):
                player.hand.append(self.deck.draw_card())

    def make_bets(self):
        for player in self.table.players:
            bet_amt = int(input(f"Please enter a bet for {player.name}"))
            if bet_amt > player.money:
                bet_amt = player.money
            else:
                player.money -= bet_amt
            self.bets[player.name] = bet_amt

    def hand_value(self, hand):
        value = 0
        for card in hand:
            if card.value == 'Ace':
                if value + 11 <= 21:
                    value += 11
                else:
                    value += 1
            elif card.value == 'Jack' or card.value == 'Queen' or card.value == 'King':
                value += 10
            else:
                value += int(card.value)

        return value

    def hit(self, player_num):
        if player_num == 1:
            #if self.table.players['player 1']
            pass



'''
Classic 5 card draw
'''
class Cantredraw():
    def __init__(self):
        n_players = int(input('Please enter a number of players'))
        s_money = int(input('Please enter a starting amount of money'))

        self.table = Table(num_players=n_players, starting_money=s_money)
        self.deck = Deck()

    def deal_hand(self):
        for player in self.table.players:
            for i in range(0, 5):
                player.hand.append(self.deck.draw_card())

if __name__ == '__main__':
    pass