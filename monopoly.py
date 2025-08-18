import random

board = []

class Property:
    def __init__(self, value, rent):
        self.value = value
        self.rent = rent
        self.buildings = []
        self.owner = ''

    def get_value(self):
        return self.value
    
    def set_owner(self, new_owner):
        self.owner = new_owner

    def get_buildings(self):
        return self.buildings

    def set_buildings(self,new_building):
        self.buildings.append(new_building)

def d6():
    return random.randint(1, 6)

def chance():
    return random.choice(['Get $100', 'Go to Go', 'Go to Jail', 'Get out of jail free'])

def comm_chest():
    return random.choice(['Go to Jail', 'Gain $100', 'Lose $50'])

def print_board():
    print(board)

def check_pass_go(num):
    if num >= 20:
        return True
    else:
        return False
    
def buy(money_available, price):
    decision = input("Buy Property? (y/n)")
    if decision == 'y' and money_available >= price:
        return True
    else:
        return False

def game():
    num_players = int(input('Please enter the number of players: '))
    score = {}
    win = False

    for _ in range(20):
        board.append(0)

    for i in range(num_players):
        score[i+1] = {'position': 0, 'money': 1500, 'properties': [], 'status': ''}

    while win == False:
        for i in range(num_players):
            print('Player ' + str(i+1) + "'s turn")
            doubles = 0

            while doubles < 3:
                d1 = d6()
                d2 = d6()
                
                if d1 == d2:
                    doubles += 1
                    if doubles > 2:
                        print("go to jail")
                        break

                    score[i+1]['position'] += d1 + d2
                    position = score[i+1]['position']
                    if check_pass_go(score[i+1]['position']):
                        # check if we passed go and wrap around
                        score[i+1]['position'] = score[i+1]['position'] % 20
                        score[i+1]['money'] += 200

                    if position == 9 or position == 19:
                        score[i+1]['money'] -= 100
                    elif position == 5 or position == 10 or position == 15:
                        return 'rail road'
                    elif position == 8:
                        card = chance()
                    elif position == 16:
                        card = comm_chest()
                    else:
                        return 'property'

                

                if d1 != d2:
                    break

            

            # remove player if they have no money
            if score[i+1]['money'] < 1:
                score.pop(i+1)

            if len(score) < 2:
                print("Game End")
                break

        break
    print(score)