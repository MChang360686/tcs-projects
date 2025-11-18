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
        self.bet = ''
        self.bet_amt = 0

    def __str__(self):
        return f'{self.name} has {self.money}'
        
class Game():
    
    def __init__(self):
        self.shoe = Shoe()
        self.players = []
        self.banker_cards = []
        self.player_cards = []
        for i in range(14):
            self.players.append(Player('Player ' + str(i)))

    def print_player_money(self):
        for player in self.players:
            print(player)

    def take_bets(self):
        for player in self.players:
            player.bet = input('Bet on Player, Banker, or Tie? (p, b, t): ')
            player.bet_amt = int(input('How much? '))
            
    def get_hand_value(self, hand):
        hand_value = 0
        for card in hand:
            match(card.value):
                case 1:
                    hand_value += 1
                case 2:
                    hand_value += 2
                case 3:
                    hand_value += 3
                case 4:
                    hand_value += 4
                case 5:
                    hand_value += 5
                case 6:
                    hand_value += 6
                case 7:
                    hand_value += 7
                case 8:
                    hand_value += 8
                case 9:
                    hand_value += 9
                case 0:
                    continue
                case _:
                    continue

        return hand_value % 10
                
    def new_round(self):
        self.banker_cards.clear()
        self.player_cards.clear()

        self.take_bets()

        for i in range(2):
            self.banker_cards.append(self.shoe.deal())
            self.player_cards.append(self.shoe.deal())

        b_hand_value = self.get_hand_value(self.banker_cards)
        p_hand_value = self.get_hand_value(self.player_cards)

        print(f'Banker has: {b_hand_value}')
        print(f'Player has: {p_hand_value}')

        if b_hand_value <= 2:
            self.banker_cards.append(self.shoe.deal())
            b_hand_value = self.get_hand_value(self.banker_cards)
            print(f'Banker has: {b_hand_value}')
        if p_hand_value <= 5:
            self.player_cards.append(self.shoe.deal())
            p_hand_value = self.get_hand_value(self.player_cards)
            print(f'Player has: {p_hand_value}')

        if self.get_hand_value(self.banker_cards) > self.get_hand_value(self.player_cards):
            print("Banker wins.  House takes 5% commission from all wins")
            for player in self.players:
                if player.bet == 'b':
                    print(f'{player.name} wins {(player.bet_amt * .95)}')
                    player.money += (player.bet_amt * .95)
                else:
                    continue
        elif self.get_hand_value(self.banker_cards) < self.get_hand_value(self.player_cards):
            print('Player wins. ')
            for player in self.players:
                if player.bet == 'p':
                    print(f'{player.name} wins {(player.bet_amt)}')
                    player.money += (player.bet_amt)
                else:
                    continue
        else:
            print('TIE bettors win ')
            for player in self.players:
                if player.bet == 't':
                    print(f'{player.name} wins {(player.bet_amt * 8)}')
                    player.money += (player.bet_amt * 8)
                else:
                    continue

        self.print_player_money()

g = Game()
while True:
    g.new_round()
    