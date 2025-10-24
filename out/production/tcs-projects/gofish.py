import random

class Deck:
    def __init__(self):
        self.cards = []
        self.discard = []

        for _ in range(4):
            for i in range(1, 14):
                self.cards.append(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def reshuffle(self):
        self.cards.extend(self.discard)

    def deal(self):
        return self.cards.pop(0)

    def discard(self, card):
        self.discard.append(card)

def fish(card_value, hand):
    if card_value in hand:
        return True
    else:
        return False

def game():
    d = Deck()
    d.shuffle()
    players = {1: [], 2: [], 3: [], 4: []}
    score = {1: 0, 2: 0, 3: 0, 4: 0}

    for player in players:
        for i in range(8):
            players[player].append(d.deal())

    while len(d.cards) > 0:
        for player in players:
            print("Player " + str(player) + " 's turn")
            print(players[player])
            card_to_find = int(input("Enter a card value from your hand "))
            player_to_ask = int(input("Enter target player (1-4) "))

            if card_to_find in players[player]:
                if fish(card_to_find, players[player_to_ask]):
                    print("card found")
                    players[player_to_ask].remove(card_to_find)
                    score[player] += 1
                else:
                    print("Go Fish")
                    players[player].append(d.deal())
            else:
                print("Card not in hand")

    print(max(score, key=score.get))
    
game()
