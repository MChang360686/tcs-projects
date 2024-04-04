import random

class Dice:

    def __init__(self) -> None:
        self.d1 = random.randint(1, 6)
        self.d2 = random.randint(1, 6)

    def roll(self):
        self.d1 = random.randint(1, 6)
        self.d2 = random.randint(1, 6)

    def get_value(self):
        return [self.d1, self.d2]

def craps():
    game = True
    round_num = 1
    d = Dice()
    point = ''

    while game:
        bet = input("Please place a bet ")

        d.roll()
        dice_total = d.d1 + d.d2

        if round_num == 1:
            if bet == 'pass':
                match(dice_total):
                    case 2 | 3 | 12:
                        print("You Lose")
                    case 7 | 11:
                        print("You Win")
                    case _:
                        point = dice_total
            elif bet == "don't pass":
                match(dice_total):
                    case 7 | 11:
                        print("You Lose")
                    case 2 | 3 | 12:
                        print("You Win")
                    case _:
                        point = dice_total
            else:
                print("You did not place a proper bet")
            round_num += 1
        else:
            d.roll()
            dice_total = d.d1 + d.d2

            match(dice_total):
                case 2 | 3 | 12:
                    print("Don't Come bets win")
                case 11:
                    print("Come bets win")
                case 7:
                    if dice_total == point:
                        print("Come bets win")
                    else:
                        print("Don't Come bets win")
                