import random

class Card:
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value
        
class Deck:
    def __init__(self):
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.deck = []
        for i in range(4):
            for j in range(13):
                self.deck.append(Card(suits[i], names[j], values[j]))
                
        random.shuffle(self.deck)
        
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop(0)
        
    def reshuffle(self, discard):
        self.deck.extend(discard)
        self.shuffle()
        
class Person:
    def __init__(self, name):
        self.name = name
        self.money = 10000
        self.bet = 0
        
def game():
    num_players = int(input('How many people are playing? '))
    players = [Person('player ' + str(i)) for i in range(num_players)]
    deck = Deck()
    
    hands = {}
    for player in players:
        hands[player.name] = [deck.deal(), deck.deal()]
        
    dealer_hand = [deck.deal(), deck.deal()]
    
    for player in players:
        print(hands[player.name])
        player.bet = int(input('Enter an amount to bet: '))
        while True:
            if input('hit or stay? ') == 'hit':
                hands[player.name] + [deck.deal()]
                sum = 0
                for card in hands[player.name]:
                    sum += card.value
                if sum > 21:
                    print(player + ' busted.')
                    player.bet = 0
                    break
            else:
                break
            
        
    while True:
        sum = 0
        for card in dealer_hand:
            sum += card.value
            
        if sum >= 17:
            break
        else:
            dealer_hand.append(deck.deal())
            
    for player in players:
        
        if player_hands[player.name] > dealer_hand
    
        
            