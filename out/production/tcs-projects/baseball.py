import random

class Player:
    def __init__(self, name, bat, run, catch):
        self.name = name
        self.bat = bat
        self.run = run
        self.catch = catch
        
    def set_bat(self, amt):
        self.bat += amt
        
    def set_run(self, amt):
        self.run += amt
        
    def set_catch(self, amt):
        self.catch += amt
        
    def __str__(self):
        return f'{self.name} bat: {self.bat} run: {self.run} catch: {self.catch}'
        
def random_stat():
    return random.randint(60, 80)
    
def game():
    names = ['jonald', 'poperton', 'yunad']
    people = []
    team = []
    for i in range(20):
        people.append(Player(random.choice(names), random_stat(), random_stat(), random_stat()))
        
    for i in range(8):
        print(people)
        choice = int(input('Enter a number (0-20) to choose a player'))
        team.append(people[choice])