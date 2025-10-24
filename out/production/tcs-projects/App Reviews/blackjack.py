import random

suits = ["hearts", "clubs", "diamonds", "spades"]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
cards = []

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

"""
Store win inside of an object.  Change and view scores using getters and setters.
"""
class Win:
    def __init__(self, dealer_score, player_score, win) -> None:
        self.dealer_score = dealer_score
        self.player_score = player_score
        self.win = win

    def get_dealer_score(self):
        return self.dealer_score
    
    def set_dealer_score(self, score):
        self.dealer_score = score

    def get_player_score(self):
        return self.player_score
    
    def set_player_score(self, score):
        self.player_score = score

    def get_win(self):
        return self.win
    
    def set_win(self):
        if self.win == False:
            self.win = True
        else:
            self.win = False

    

score_player = 0

card = Card(random.choice(suits), random.choice(values))
card_2 = Card(random.choice(suits), random.choice(values))


play = True

def sum_cards(card, card_2, *cards):
    score = int(card.value) + int(card_2.value)
    for card in cards:
        val = card.value

        match(val):
            case '2':
                score += 2
            case '3':
                score += 3
            case '4':
                score += 4
            case '5':
                score += 5
            case '6':
                score += 6
            case '7':
                score += 7
            case '8':
                score += 8
            case '9':
                score += 9
            case '10':
                score += 10
            case 'jack':
                score += 10
            case 'queen':
                score += 10
            case 'king':
                score += 10
            case 'ace':
                if (score + 11) > 21:
                    score += 1
                else:
                    score += 11

    return score

def hit(c):
    return score_player + sum_cards(card, card_2, c)

def check_blackjack(score):
    if score < 21:
        print("Not Quite...")
    elif score == 21:
        print("Blackjack!!!")
    elif score > 21:
        print("Bust")
    else:
        pass

def play_again():
    response = input("Would you like to play again? (y/n) ")
    if response == 'y':
        return True
    elif response == 'n':
        return False
    else:
        print("I don't know what that command means ")
        return False
    
def dealer(dealer_total):
    if dealer_total < 21:
        if dealer_total >= 17:
            print("dealer stands on 17")
    elif dealer_total == 21:
        pass
    elif dealer_total > 21:
        print("dealer bust")

def check_win(dealer_score, player_score):
    if dealer_score > player_score:
        print("Dealer wins")
    elif player_score > dealer:
        print("YOU WIN!!!")
    else:
        print("Tie")
    
score_player = sum_cards(card.value, card_2.value)
print(score_player)

c, c2 = Card(random.choice(suits), random.choice(values)), Card(random.choice(suits), random.choice(values))
dealer_total = sum_cards(c, c2)
print(dealer_total)

w = Win(score_player, dealer_total, False)

while play:

    player_turn = input("Please enter a command (h, s) ")

    if player_turn == 'h':
        score_player = hit(Card(random.choice(suits), random.choice(values)))
        print(score_player)
        check_blackjack(score_player)
        check_win(dealer_total, score_player)
    elif player_turn == 's':
        play = play_again()
    else:
        print("I don't know that command ")
