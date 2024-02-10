import random

card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

def get_value(card_name):
    match (card_name):
        case "2":
            return 2
        case "3":
            return 3
        case "4":
            return 4
        case "5":
            return 5
        case "6":
            return 6
        case "7":
            return 7
        case "8":
            return 8
        case "9":
            return 9
        case "10":
            return 10
        case "jack":
            return 11
        case "queen":
            return 12
        case "king":
            return 13
        case "ace":
            return 14

def compare(player_card, cpu_card):
    if player_card > cpu_card:
        return 1
    elif cpu_card > player_card:
        return -1
    else:
        outcome = war()
        if outcome == 1:
            return 1
        elif outcome == -1:
            return -1
    
def war():
    p = get_value(random.choice(card))
    c = get_value(random.choice(card))
    if p > c:
        return 1
    elif c > p:
        return -1
    else:
        war()

player_score = 0
cpu_score = 0

while True:
    player = random.choice(card)
    input(f"Player drew a {player} ")
    cpu = random.choice(card)
    input(f"CPU drew {cpu} ")

    result = compare(get_value(player), get_value(cpu))

    if result == 1:
        print("Player wins this round")
        player_score += 1
    elif result == -1:
        print("CPU wins this round")
        cpu_score += 1

    print(player_score, cpu_score)

    if player_score >= 52 or cpu_score >= 52:
        if player_score == 52:
            print("Player wins")
            False
        elif cpu_score == 52:
            print("CPU wins")
            False