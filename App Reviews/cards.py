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

        bets = {'dealer': 0}

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
        player = self.table.players[f"Player {player_num}"]

        if player_num == 1:
            if self.hand_value(player.hand) < 17:
                player.hand.append(self.deck.draw_card())
        else:
            player.hand.append(self.deck.draw_card())

        return self.hand_value(player.hand)
    
    def stand(self, player_num):
        player = self.table.players[f"Player {player_num}"]
        return self.hand_value(player.hand)
    
    def check_bust(self, player_num):
        player = self.table.players[f"Player {player_num}"]
        if self.hand_value(player.hand) > 21:
            return True
        else:
            return False
        
    def game(self):

        for player in self.table.players:
            self.bets[player] = 0

        while True:
            self.make_bets()
            self.deal_hand()
            for player in self.table.players:
                hand_value = self.hand_value(player.hand)
                print(f"{player.name} has a hand value of {hand_value}")

                player_decision = input("Please enter either hit or stand")

                while player_decision != 'stand':
                    if player_decision == 'hit':
                        hand_value = self.hit(player.name)
                        print(f"{player.name} has a hand value of {hand_value}")
                        if self.check_bust(player.name):
                            print("You bust")
                            break
                    else:
                        print("I don't know that command")
                        player_decision = input("Please enter either hit or stand")
                        continue
                    player_decision = input("Please enter either hit or stand")

                if player.hand_value(player.hand) > 21:
                    player.money -= self.bets[player.name]
                elif player.hand_value(player.hand) == 21:
                    player.money += self.bets[player.name] * 3
                else:
                    if player.hand_value(player.hand) > hand_value(self.table.players['Player 1'].hand):
                        player.money += self.bets[player.name] * 2


                
                
    
   



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


    '''Check if all cards in hand are the same suit'''
    def check_suit(self, hand):
        for card in hand:
            if card.suit != hand[0].suit:
                return False

        return True

    '''Check for duplicates'''
    def check_for_duplicates(self, hand):
        cards = {}
        duplicates = False
        for card in hand:
            if card.value in cards:
                cards[card.value] = None
            else:
                duplicates = True

        return duplicates

    '''Check number of duplicates (pair, 3 of a kind, 4 of a kind)'''
    
    

    '''Read value of hand of cards and return a hash'''
    def hand_value(self, hand):
        hand_val_numerical = []
        for card in hand:
            if card.value == 'Ace':
                hand_val_numerical.append(13)
            elif card.value == 'Jack':
                hand_val_numerical.append(10)
            elif card.value == 'Queen':
                hand_val_numerical.append(11)
            elif card.value == 'King':
                hand_val_numerical.append(12)
            else:
                hand_val_numerical.append(int(card.value))

        hand_val_numerical.sort()
        return hand_val_numerical


if __name__ == '__main__':
    game = input("Please enter a game (blackjack, cantredraw)")

    if game == 'blackjack':
        game = BlackJack()
        game.game()
    elif game == 'cantredraw':
        game = Cantredraw()
        game.deal_hand()
    else:
        print("I don't have that game")