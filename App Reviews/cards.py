import random
import itertools

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

class TexasHoldEm:
    def __init__(self):
        n_players = int(input('Enter the number of players: '))
        s_money = int(input('Enter starting money for each player: '))
        self.players = [Player(f"Player {i+1}", s_money) for i in range(n_players)]
        self.deck = Deck()
        self.community_cards = []
        self.bets = {}
        self.pot = 0
        self.current_bet = 0

    def reset_round(self):
        self.deck = Deck()
        self.community_cards = []
        self.bets.clear()
        self.pot = 0
        self.current_bet = 0
        for player in self.players:
            player.hand = []

    def deal_hands(self):
        for player in self.players:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]

    def deal_flop(self):
        self.community_cards.extend([self.deck.draw_card() for _ in range(3)])
        print(f'Flop: {", ".join(str(c) for c in self.community_cards)}')

    def deal_turn(self):
        self.community_cards.append(self.deck.draw_card())
        print(f'Turn: {self.community_cards[-1]}')

    def deal_river(self):
        self.community_cards.append(self.deck.draw_card())
        print(f'River: {self.community_cards[-1]}')

    def place_bet(self, player, amount):
        """Handles betting and pot updates"""
        if amount > player.money:
            amount = player.money  # all-in if player doesn't have enough
        player.money -= amount
        self.pot += amount
        self.bets[player.name] = self.bets.get(player.name, 0) + amount
        print(f"{player.name} bets {amount}. Remaining money: {player.money}")

    def betting_round(self, players):
        self.current_bet = 0
        active_players = players[:]

        for player in active_players[:]:
            if player.money <= 0:
                print(f"{player.name} is all-in and skips betting.")
                continue

            print(f"{player.name}'s turn. Money: {player.money}")
            cmd = input(f"{player.name}, what would you like to do? (fold, call, raise, check): ").strip().lower()

            if cmd == "fold":
                print(f"{player.name} folds.")
                active_players.remove(player)

            elif cmd == "check":
                if self.current_bet == 0:
                    print(f"{player.name} checks.")
                else:
                    print(f"{player.name} cannot check, must call or fold.")
                    active_players.remove(player)

            elif cmd == "call":
                call_amt = self.current_bet - self.bets.get(player.name, 0)
                self.place_bet(player, call_amt)

            elif cmd == "raise":
                raise_amt = int(input("Enter raise amount: "))
                total_bet = (self.current_bet - self.bets.get(player.name, 0)) + raise_amt
                self.place_bet(player, total_bet)
                self.current_bet += raise_amt

            else:
                print("Invalid command. Auto-folding.")
                active_players.remove(player)

        return active_players

    def check_order(self, player):
        values_map = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "10": 10,
            "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
        }
        hashed_hand = [values_map[card.value] for card in player.hand]
        hashed_hand.sort()

        for i in range(len(hashed_hand) - 1):
            if hashed_hand[i] + 1 != hashed_hand[i + 1]:
                return False
        return True
    
    def rank_hand(self, cards):
        """Evaluate a 5-card poker hand and return ranking tuple for comparison"""
        values_map = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "10": 10,
            "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
        }

        values = sorted([values_map[c.value] for c in cards], reverse=True)
        suits = [c.suit for c in cards]

        # Count duplicates
        counts = {}
        for v in values:
            counts[v] = counts.get(v, 0) + 1
        counts_sorted = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))

        is_flush = len(set(suits)) == 1
        is_straight = all(values[i] - 1 == values[i+1] for i in range(len(values)-1))
        
        # Special Ace-low straight (A,2,3,4,5)
        if set(values) == {14, 5, 4, 3, 2}:
            is_straight = True
            values = [5, 4, 3, 2, 1]

        # Straight flush
        if is_straight and is_flush:
            return (0, values)  # strongest

        # Four of a kind
        if counts_sorted[0][1] == 4:
            return (1, [counts_sorted[0][0], counts_sorted[1][0]])

        # Full house
        if counts_sorted[0][1] == 3 and counts_sorted[1][1] == 2:
            return (2, [counts_sorted[0][0], counts_sorted[1][0]])

        # Flush
        if is_flush:
            return (3, values)

        # Straight
        if is_straight:
            return (4, values)

        # Three of a kind
        if counts_sorted[0][1] == 3:
            kickers = [v for v in values if v != counts_sorted[0][0]]
            return (5, [counts_sorted[0][0]] + kickers)

        # Two pair
        if counts_sorted[0][1] == 2 and counts_sorted[1][1] == 2:
            kicker = [v for v in values if v not in (counts_sorted[0][0], counts_sorted[1][0])]
            return (6, [counts_sorted[0][0], counts_sorted[1][0]] + kicker)

        # One pair
        if counts_sorted[0][1] == 2:
            kickers = [v for v in values if v != counts_sorted[0][0]]
            return (7, [counts_sorted[0][0]] + kickers)

        # High card
        return (8, values)

    def best_hand(self, player):
        """Find best 5-card hand from 7 total cards"""
        all_cards = player.hand[:2] + self.community_cards
        best = (9, [])  # worse than any real hand
        best_combo = None

        for combo in itertools.combinations(all_cards, 5):
            score = self.rank_hand(combo)
            if score < best:
                best = score
                best_combo = combo

        return best, best_combo

    def determine_winner(self, players):
        """Compare all active players and return the winner(s)"""
        scores = []
        for player in players:
            score, combo = self.best_hand(player)
            scores.append((score, player, combo))

        scores.sort(key=lambda x: x[0])  # best hand first
        best_score = scores[0][0]
        winners = [s for s in scores if s[0] == best_score]

        return winners

    def game(self):
        new_round = True
        while new_round:
            self.reset_round()
            current_players = self.players[:]

            self.deal_hands()
            for player in current_players:
                print(f"{player.name} has {player.hand[0]}, {player.hand[1]}")

            # Flop
            self.deal_flop()
            current_players = self.betting_round(current_players)

            # Turn
            self.deal_turn()
            current_players = self.betting_round(current_players)

            # River
            self.deal_river()
            current_players = self.betting_round(current_players)

            winners = self.determine_winner(current_players)
            split_pot = self.pot // len(winners)

            for score, player, combo in winners:
                player.money += split_pot
                print(f"{player.name} wins with {', '.join(str(c) for c in combo)}! New balance: {player.money}")


            new_round = input("Play another round? (y/n): ").strip().lower() == "y"


    
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