import random

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nHeight: {self.height}\nWeight: {self.weight}'
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_height(self):
        return self.height
    
    def get_weight(self):
        return self.weight

p1 = Person('Alice', 25, 160, 55)
p2 = Person('Bob', 30, 175, 70)

people = [p1, p2]

def print_people():
    for person in people:
        print(person)

def play():
    print_people()
    p_index = int(input("Please enter 0-1"))
    player_char = people[p_index]
    print(player_char.get_name())

    computer_char = random.choice(people)
    cpu_num = 0
    cpu_clues = []

    win = False

    while not win:
        cmd = input("Please enter age, height, or weight")
        if cmd == 'age':
            print(computer_char.get_age())
        elif cmd == "height":
            print(computer_char.get_height())
        elif cmd == "weight":
            print(computer_char.get_weight)
        
        guess = input("Please enter your guess")

        if guess == computer_char.get_name():
            win = True
            print(player_char.get_name())
            print("You Win!")
            break

        if cpu_num == 0:
            cpu_clues.append(player_char.get_age())
        elif cpu_num == 1:
            cpu_clues.append(player_char.get_height())
        elif cpu_num == 2:
            cpu_clues.append(player_char.get_weight())
        else:
            for person in people:
                if cpu_clues[0] == player_char.get_age() and cpu_clues[1] == player_char.get_height() and cpu_clues[2] == player_char.get_weight():
                    win = True
                    print(person.get_name())
                    print("You Lose!")
                    break
        cpu_num += 1
            
play()
