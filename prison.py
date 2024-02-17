import random

card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

def make_dicts(dict):
    for value in card_values:
        dict[value] = False

    return dict

def play():
    hearts = make_dicts({})
    diamonds = make_dicts({})
    spades = make_dicts({})
    clubs = make_dicts({})

    h = input("Please enter an exercise for hearts ")
    d = input("Please enter an exercise for diamonds ")
    s = input("Please enter an exercise for spades ")
    c = input("Please enter an exercise for clubs ")

    exercises = [hearts, diamonds, spades, clubs]
    suit_names = ['hearts', 'diamonds', 'spades', 'clubs']

    for i in range(0, 52):
        suit = random.choice(exercises)
        suit_name = random.choice(suit_names)
        card = random.sample(suit.keys(), 1)

        match (suit_name):
            case 'hearts':
                print(f"Do {card} {h}")
            case 'diamonds':
                print(f"Do {card} {d}")
            case 'spades':
                print(f"Do {card} {s}")
            case 'clubs':
                print(f"Do {card} {c}")

        input()

play()