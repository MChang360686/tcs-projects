import random

def get_num():
    return random.randint(0, 80)

class Ticket:
    def __init__(self, name):
        self.name = name
        self.nums = []
        
    def get_nums(self):
        return self.nums
        
    def set_nums(self, new):
        self.nums = new
        
def choose_nums():
    return [int(num) for num in input('Enter 20 numbers from 0 to 80 w/ spaces: ').split() ]
    
def game():
    num_players = int(input('Enter the number of players: '))
    tickets = []
    chosen_nums = []
    
    for i in range(num_players):
        tickets.append(Ticket(input('Enter ticket holder name: ')))
        tickets[i].set_nums(choose_nums())
        
    for j in range(20):
        chosen_nums.append(random.randint(0, 80))
        
    for ticket in tickets:
        for num in chosen_nums:
            if num in ticket.get_nums():
                print(f'{ticket.name} hit {num}')
                
game()
