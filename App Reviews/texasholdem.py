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

t = TexasHoldEm()
t.game()