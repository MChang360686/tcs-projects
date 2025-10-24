import random

suits = ['hearts', 'spades', 'diamonds', 'clubs']

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

score_1 = 0
score_2 = 0

player = input("Please enter a name ")

while True:
    card_1 = random.choice(values)
    card_2 = random.choice(values)

    c1 = random.choice(suits) + ' ' + card_1
    c2 = random.choice(suits) + ' ' + card_2

    input(f"CPU drew {c1}")
    input(f"{player} drew {c2}")

    if card_1 > card_2:
        print("CPU wins")
        score_1 += 1
    elif card_2 > card_1:
        print("Player wins!")
        score_2 += 1
    else:
        print('WAR!')
        c3 = random.choice(values)
        c4 = random.choice(values)
        c5 = random.choice(values)

        c6 = random.choice(values)
        c7 = random.choice(values)
        c8 = random.choice(values)

        if (c3 + c4 + c5) > (c6 + c7 +c8):
            print('Computer wins')
            score_1 += 1
        else:
            print('Player wins!')
            score_2 += 1


    print(score_1, score_2)
