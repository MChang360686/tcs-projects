import random

suits = ["hearts", "clubs", "diamonds", "spades"]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
cards = []

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

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
    else:
        print("Bust")

def play_again():
    response = input("Would you like to play again? (y/n) ")
    if response == 'y':
        return True
    elif response == 'n':
        return False
    else:
        print("I don't know what that command means ")
        return False
    
score_player = sum_cards(card, card_2)
print(score_player)

while play:

    player_turn = input("Please enter a command (h, s) ")

    if player_turn == 'h':
        score_player = hit(Card(random.choice(suits), random.choice(values)))
        print(score_player)
        check_blackjack(score_player)
    elif player_turn == 's':
        play = play_again()
    else:
        print("I don't know that command ")
