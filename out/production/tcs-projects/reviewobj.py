import random

def add():
    return random.randint(0, 100) + random.randint(0, 100)
    
for i in range(10):
    print(add())
    
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def get_name(self):
        return self.name
        
    def get_age(self):
        return self.age
        
    def get_height(self):
        return self.height
        
    def get_weight(self):
        return self.weight
        
    def set_name(self, new_name):
        self.name = new_name
        
    def set_age(self, new_age):
        self.age = new_age
        
    def set_height(self, new_height):
        self.height = new_height
        
    def set_weight(self, new_weight):
        self.weight = new_weight
        
    def __str__(self):
        return self.name + ' ' + self.age + ' ' + self.height + ' ' + self.weight + ' '
        

def game():
    people = []
    names = ['Bob', 'Rob', 'Job', 'Tob ias', 'Lob']
    for i in range(10):
        people.append(Person(random.choice(names), str(random.randint(20, 50)), str(random.randint(4, 7)), str(random.randint(100, 300))))

    for person in people:
        print(person)
        
game()
    