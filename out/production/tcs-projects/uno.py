import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
    
    def get_color(self):
        return self.color
    
    def get_value(self):
        return self.value
    
    def __str__(self):
        return f"{self.color} {self.value}"

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def play_card(self, card_index, card_to_match):
        if 0 <= card_index < len(self.cards):
            selected_card = self.cards[card_index]
            if selected_card.get_color() == card_to_match.get_color() or selected_card.get_value() == card_to_match.get_value() or selected_card.get_value() in ["wild", "wild draw four"]:
                return self.cards.pop(card_index)
        return None

    def __str__(self):
        return ", ".join([f"{i}: {card}" for i, card in enumerate(self.cards)])

class Deck:
    def __init__(self):
        self.cards = []
        colors = ["red", "green", "blue", "yellow"]
        values = [0] + [1, 2, 3, 4, 5, 6, 7, 8, 9, "reverse", "skip", "draw two"] * 2
        wild_cards = ["wild", "wild draw four"] * 4

        for color in colors:
            for value in values:
                self.cards.append(Card(color, value))
        for wild in wild_cards:
            self.cards.append(Card("wild", wild))

        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop(0)
        return None

    def return_cards(self, cards):
        self.cards.extend(cards)
        random.shuffle(self.cards)

class Game:
    def __init__(self):
        num_players = int(input("Enter number of players: "))
        self.deck = Deck()
        self.discard_pile = []
        self.players_hands = {f"Player {i+1}": Hand() for i in range(num_players)}

        # Deal 7 cards to each player
        for hand in self.players_hands.values():
            for _ in range(7):
                hand.add_card(self.deck.deal_card())

        # Start the discard pile with the top card
        self.discard_pile.append(self.deck.deal_card())

        # Track current player and turn direction
        self.current_player_index = 0
        self.turn_direction = 1  # 1 for clockwise, -1 for counter-clockwise

    def play_game(self):
        while True:
            current_player = list(self.players_hands.keys())[self.current_player_index]
            print(f"\n{current_player}'s turn.")
            print(f"Top card: {self.discard_pile[-1]}")
            print(f"Your hand: {self.players_hands[current_player]}")

            while True:
                try:
                    card_index = int(input("Enter card index to play or -1 to draw: "))
                    if card_index == -1:
                        # Draw a card
                        new_card = self.deck.deal_card()
                        if new_card:
                            self.players_hands[current_player].add_card(new_card)
                            print(f"You drew: {new_card}")
                        else:
                            print("No cards left to draw!")
                        break
                    else:
                        played_card = self.players_hands[current_player].play_card(card_index, self.discard_pile[-1])
                        if played_card:
                            self.discard_pile.append(played_card)
                            print(f"You played: {played_card}")
                            self.handle_special_card(played_card)
                            break
                        else:
                            print("Invalid card. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Try again.")

            # Check if player has won
            if not self.players_hands[current_player].cards:
                print(f"\n{current_player} wins!")
                break

            # Move to the next player
            self.current_player_index = (self.current_player_index + self.turn_direction) % len(self.players_hands)

    def handle_special_card(self, card):
        if card.get_value() == "reverse":
            self.turn_direction *= -1
        elif card.get_value() == "skip":
            self.current_player_index = (self.current_player_index + self.turn_direction) % len(self.players_hands)
        elif card.get_value() == "draw two":
            next_player = (self.current_player_index + self.turn_direction) % len(self.players_hands)
            for _ in range(2):
                self.players_hands[list(self.players_hands.keys())[next_player]].add_card(self.deck.deal_card())
        elif card.get_value() == "wild":
            new_color = input("Choose a color (red, green, blue, yellow): ").strip().lower()
            card.color = new_color
        elif card.get_value() == "wild draw four":
            new_color = input("Choose a color (red, green, blue, yellow): ").strip().lower()
            card.color = new_color
            next_player = (self.current_player_index + self.turn_direction) % len(self.players_hands)
            for _ in range(4):
                self.players_hands[list(self.players_hands.keys())[next_player]].add_card(self.deck.deal_card())

game = Game()
game.play_game()
