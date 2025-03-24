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
        self.discard = []
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

class Cantredraw():
    
    def __init__(self):
        pass

if __name__ == '__main__':
    game = input("Enter a game (blackjack, cantredraw): ").strip().lower()

    if game == 'blackjack':
        bj_game = BlackJack()
        bj_game.game()
    elif game == 'cantredraw':
        print("Cantredraw game is not fully implemented yet.")
    else:
        print("Invalid game selection.")
