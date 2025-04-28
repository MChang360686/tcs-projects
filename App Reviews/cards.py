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

    def draw_card(self):
        return self.deck.pop(0) if self.deck else None
    
    def discard_card(self, card):
        self.discard.append(card)

    def re_shuffle(self):
        self.deck.extend(self.discard)
        self.discard.clear()
        self.shuffle()

class Player():
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand)

class BlackJack():

    def __init__(self):
        n_players = int(input('Enter the number of players: '))
        s_money = int(input('Enter starting money for each player: '))
        self.players = [Player(f"Player {i+1}", s_money) for i in range(n_players)]
        self.dealer = Player("Dealer", 0)  # Dealer has no money
        self.deck = Deck()
        self.bets = {}

    def deal_hand(self):
        """Give each player and the dealer two cards."""
        for player in self.players + [self.dealer]:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]

    def make_bets(self):
        """Get bets from players."""
        for player in self.players:
            while True:
                try:
                    bet_amt = int(input(f"{player.name}, enter your bet (Available: ${player.money}): "))
                    if bet_amt > player.money:
                        print("You don't have enough money. Bet lower.")
                    else:
                        player.money -= bet_amt
                        self.bets[player.name] = bet_amt
                        break
                except ValueError:
                    print("Please enter a valid number.")

    def hand_value(self, hand):
        """Calculate the value of a hand."""
        value = 0
        aces = 0
        
        for card in hand:
            if card.value in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.value == 'Ace':
                aces += 1
                value += 11
            else:
                value += int(card.value)

        # Handle Aces (if value > 21, convert Aces from 11 to 1)
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value

    def hit(self, player):
        """Draw a card for the player."""
        player.hand.append(self.deck.draw_card())

    def check_bust(self, player):
        """Check if a player is bust (over 21)."""
        return self.hand_value(player.hand) > 21

    def play_turn(self, player):
        """Player's turn: choose to hit or stand."""
        print(f"{player.name}'s turn. Current hand: {player.show_hand()} (Value: {self.hand_value(player.hand)})")
        
        while self.hand_value(player.hand) < 21:
            action = input("Enter 'hit' or 'stand': ").strip().lower()
            if action == 'hit':
                self.hit(player)
                print(f"New hand: {player.show_hand()} (Value: {self.hand_value(player.hand)})")
                if self.check_bust(player):
                    print(f"{player.name} busts!")
                    return
            elif action == 'stand':
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

    def dealer_turn(self):
        """Dealer logic: Must hit if below 17."""
        print(f"\nDealer's turn. Dealer's hand: {self.dealer.show_hand()} (Value: {self.hand_value(self.dealer.hand)})")
        
        while self.hand_value(self.dealer.hand) < 17:
            print("Dealer hits.")
            self.hit(self.dealer)
            print(f"Dealer's new hand: {self.dealer.show_hand()} (Value: {self.hand_value(self.dealer.hand)})")
            
            if self.check_bust(self.dealer):
                print("Dealer busts!")
                return

        print("Dealer stands.")

    def determine_winners(self):
        """Decide winners and payout bets."""
        dealer_value = self.hand_value(self.dealer.hand)

        for player in self.players:
            player_value = self.hand_value(player.hand)

            if player_value > 21:
                print(f"{player.name} loses (busted).")
            elif dealer_value > 21 or player_value > dealer_value:
                print(f"{player.name} wins! Bet doubled.")
                player.money += self.bets[player.name] * 2
            elif player_value == dealer_value:
                print(f"{player.name} ties with dealer. Bet returned.")
                player.money += self.bets[player.name]
            else:
                print(f"{player.name} loses.")

    def game(self):
        """Play one full round of Blackjack."""
        while True:
            self.bets.clear()
            self.make_bets()
            self.deal_hand()

            # Players take turns
            for player in self.players:
                self.play_turn(player)

            # Dealer's turn
            self.dealer_turn()

            # Determine winners
            self.determine_winners()

            # Check if players have money left
            for player in self.players:
                if player.money <= 0:
                    print(f"{player.name} is out of money and leaves the game.")

            # Ask if players want another round
            again = input("\nPlay another round? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thanks for playing!")
                break

class TexasHoldEm():
    
    def __init__(self):
        n_players = int(input('Enter the number of players: '))
        s_money = int(input('Enter starting money for each player: '))
        self.players = [Player(f"Player {i+1}", s_money) for i in range(n_players)]
        self.deck = Deck()
        self.community_cards = []
        self.bets = {}

    def deal_hands(self):
        for player in self.players:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]

    '''Deal the flop (3 cards)'''
    def deal_flop(self):
        for _ in range(0, 3):
            self.community_cards.append(self.deck.draw_card())
        
        for player in self.players:
            player.hand.extend(self.community_cards)

        print(f'Flop: {self.community_cards[0]}, {self.community_cards[1]}, {self.community_cards[2]}')

    '''Deal the turn'''
    def deal_turn(self):
        self.community_cards.append(self.deck.draw_card())

        for player in self.players:
            player.hand.append(self.community_cards[3])

        print(f'Turn: {self.community_cards[3]}')

    '''Deal the river'''
    def deal_river(self):
        self.community_cards.append(self.deck.draw_card())

        for player in self.players:
            player.hand.append(self.community_cards[4])

        print(f'River: {self.community_cards[4]}')

    def bet(self, player_name, amt):
        for player in self.players:
            if player.name == player_name:
                player.money -= amt
                self.bets[player_name] = amt
            else:
                continue

    def fold(self, player_name):
        self.bets[player_name] = 0

    def check_suits(self, player):
        for card in player.hand:
            if card.suit == player.hand[0].suit:
                continue
            else:
                return False
        return True
    
    def check_duplicates(self, player):
        duplicates = {}
        for card in player.hand:
            if card.value in duplicates.keys():
                duplicates[card.value] += 1
            else:
                duplicates[card.value] = 1

        return duplicates
    
    def check_order(self, player):
        hashed_hand = []
        for card in player.hand:
            match card.value:
                case '2':
                    hashed_hand.append(2)
                case '3':
                    hashed_hand.append(3)
                case '4':
                    hashed_hand.append(4)
                case '5':
                    hashed_hand.append(5)
                case '6':    
                    hashed_hand.append(6)
                case '7':
                    hashed_hand.append(7)
                case '8':
                    hashed_hand.append(8)
                case '9':
                    hashed_hand.append(9)
                case '10':
                    hashed_hand.append(10)
                case 'J':
                    hashed_hand.append(11)
                case 'Q':
                    hashed_hand.append(12)
                case 'K':    
                    hashed_hand.append(13)
                case 'A':
                    hashed_hand.append(14)
                case _:
                    continue

        hashed_hand.sort()
        print(hashed_hand)

        for i in range(len(hashed_hand) - 1):
            if hashed_hand[i] == hashed_hand[i+1] - 1:
                continue
            else:
                return False
            
        return True


    def sort_hands(self):
        hands = {'sf': [], '4ok': [], 'fh': [], 'f': [], 's': [], '3ok': [], '2p': [], '1p': [], 'hc': []}
        for player in self.players:
            player_dup = self.check_duplicates(player)
            flush = self.check_suits(player)
            order = self.check_order(player)

            if flush == True and order == True:
                hands['sf'].append(player.name)
            elif 4 in player_dup.values():
                hands['4ok'].append(player.name)
            elif 3 in player_dup.values() and 2 in player_dup.values():
                hands['fh'].append(player.name)
            elif flush == True:
                hands['f'].append(player.name)
            elif order == True:
                hands['s'].append(player.name)
            elif 3 in player_dup.values():
                hands['3ok'].append(player.name)
            elif len([pair for pair in player_dup.values() if pair == 2]) == 2:
                hands['2p'].append(player.name)
            elif 2 in player_dup.values():
                hands['1p'].append(player.name)
            else:
                hands['hc'].append(player.name)

        print(hands)
        return hands

    def game(self):
        new_round = True
        while new_round == True:
            current_players = self.players

            self.deal_hands()
            self.deal_flop()

            '''for card in self.community_cards:
                print(card)'''
            
            for player in current_players:
                print(f'{player.name} has {player.hand[0]}, {player.hand[1]}')
                cmd = input(f'{player.name}, what would you like to do? (fold, call, raise): ').strip().lower()
                if cmd == 'fold':
                    self.fold(player.name)
                    current_players.remove(player)
                elif cmd == 'call':
                    amt = int(input('How much would you like to bet? '))
                    self.bet(player.name, amt)
                elif cmd == 'raise':
                    raise_amt = int(input('How much would you like to raise? '))
                    self.bet(player.name, raise_amt)
                else:
                    print('Invalid command. Please enter "fold", "call", or "raise".')
        

            self.deal_turn()

            for player in current_players:
                cmd = input(f'{player.name}, what would you like to do? (fold, call, raise): ').strip().lower()
                if cmd == 'fold':
                    self.fold(player.name)
                    current_players.remove(player)
                elif cmd == 'call':
                    self.bet(player.name, self.bets[player.name])
                elif cmd == 'raise':
                    raise_amt = int(input('How much would you like to raise? '))
                    self.bet(player.name, self.bets[player.name] + raise_amt)
                else:
                    print('Invalid command. Please enter "fold", "call", or "raise".')

            self.deal_river()

            hands_ranked = self.sort_hands()

            '''Go down the Dict to see who has the highest ranked hand'''
            for hand in hands_ranked:
                if len(hands_ranked[hand]) > 0:
                    '''For each player, give them the pot / num players with highest hand'''
                    for player_name in hands_ranked[hand]:
                        for player in self.players:
                            if player.name == player_name:
                                cards = [(card.suit, card.value) for card in player.hand]
                                print(f'{player.name} wins with {cards}')
                                player.money += sum(self.bets.values()) // len(hands_ranked[hand])
                    break
                else:
                    continue

            for player in self.players:
                print(f'{player.name} has {player.money}')

            new_round = True if input('Play another round? (y/n)') == 'y' else False

'''TODO: fix betting'''

    
class ChorDaiDi():

    def __init__(self):
        n_players = int(input('Enter the number of players: '))
        if n_players > 4:
            print("Maximum of 4 players allowed.")
            n_players = 4
        s_money = int(input('Enter starting money for each player: '))
        self.players = [Player(f"Player {i+1}", s_money) for i in range(n_players)]
        self.deck = Deck()
        self.bets = {}
        self.ranks = {'Spades': 3, 'Hearts': 2, 'Clubs': 1, 'Diamonds': 0}

    def deal_hands(self):
        cards_dealt = 0

        for i in range(0, len(self.deck)):
            if len(self.deck) - cards_dealt < self.n_players:
                '''push rest of cards to 3 of diamonds'''
                break
            else:
                self.players[f'Player {(i % self.n_players) + 1}'].append(self.deck.draw_card())

            cards_dealt += 1

        for player in self.players:
            for card in player.hand():
                if card.value == '3' and card.suit == 'Diamonds':
                    for card in self.deck():
                        player.hand.append(card)
                else:
                    continue

    
    def validate_cards(self, prev_hand, player_hand):
        prev = []
        player = []

        for card in prev_hand:
            if card.value not in ['Jack', 'Queen', 'King', 'Ace', '2']:
                prev.append(int(card.value))
            else:
                match(card.value):

                    case 'Jack':
                        prev.append(11)
                    case 'Queen':
                        prev.append(12)
                    case 'King':
                        prev.append(13)
                    case 'Ace':
                        prev.append(14)
                    case '2':
                        prev.append(15)
                    case _:
                        print('Invalid Card')
                        return False
                    
        for card in player_hand:
            if card.value not in ['Jack', 'Queen', 'King', 'Ace', '2']:
                player.append(int(card.value))
            else:
                match(card.value):

                    case 'Jack':
                        player.append(11)
                    case 'Queen':
                        player.append(12)
                    case 'King':
                        player.append(13)
                    case 'Ace':
                        player.append(14)
                    case '2':
                        player.append(15)
                    case _:
                        print('Invalid Card')
                        return False

        prev_sum = sum(prev)
        player_sum = sum(player)

        if player_sum >= prev_sum:
            return True
        else:
            return False

    
    def game(self):
        
        win = False
        while win != True:
            for player in self.players:
                if len(player.hand) > 0:
                    print(player.hand)
                    play = input('Please enter card indices separated by commas or enter to pass')
                    if play == '':
                        '''Player passes'''
                        continue
                    elif len(play.split(',')) == 1:
                        if int(play) <= len(player.hand) - 1 and int(play) >= 0:
                            if self.validate_cards(player.hand[int(play)]) == True:
                                player.hand.pop(int(play))
                                self.deck.discard.append(player.hand[int(play)])
                            else:
                                print('Invalid play')
                    else:
                        hand = []
                        for number in play.split(','):
                            
                            hand.append(int(number))

                        if self.validate_cards(hand) == True:
                            for number in play.split(','):
                                self.deck.discard.append(player.hand[int(number)])
                                player.hand.pop(int(number))
                                

                else:
                    win = True
                    break


    

    

            

if __name__ == '__main__':
    game = input("Enter a game (blackjack, texas holdem): ").strip().lower()

    if game == 'blackjack':
        bj_game = BlackJack()
        bj_game.game()
    elif game == 'texas holdem':
        th_game = TexasHoldEm()
        th_game.game()
    elif game == 'chordaidi':
        cdd = ChorDaiDi()
        cdd.game()
    else:
        print("Invalid game selection.")
