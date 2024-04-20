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

    bet = input("Please place a bet ")


    while game:
        d.roll()
        dice_total = d.d1 + d.d2

        print(dice_total)

        if round_num == 1:
            if bet == 'pass':
                match(dice_total):
                    case 2 | 3 | 12:
                        print("You Lose")
                        break
                    case 7 | 11:
                        print("You Win")
                        break
                    case _:
                        point = dice_total
            elif bet == "don't pass":
                match(dice_total):
                    case 7 | 11:
                        print("You Lose")
                        break
                    case 2 | 3 | 12:
                        print("You Win")
                        break
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
                    break
                case 11:
                    print("Come bets win")
                    break
                case 7:
                    if dice_total == point:
                        print("Come bets win")
                        break
                    else:
                        print("Don't Come bets win")
                        break
                

craps()