import random

class Person:
    def __init__(self, fname, lname, height, weight, age):
        self.fname = fname
        self.lname = lname
        self.height = height
        self.weight = weight
        self.age = age
        
    def get_fname(self):
        return self.fname
    def get_lname(self):
        return self.lname
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_age(self):
        return self.age
    def set_fname(self, new):
        self.fname = new
    def set_lname(self, new):
        self.lname = new
    def set_weight(self, new):
        self.weight += new

    def __str__(self):
        return f'{self.fname} {self.lname} age: {self.age} height: {self.height} weight: {self.weight}'
    
class Papers:
    def __init__(self, fname, lname, height, weight, age):
        self.fname = fname
        self.lname = lname
        self.height = height
        self.weight = weight
        self.age = age
        
    def get_fname(self):
        return self.fname
    def get_lname(self):
        return self.lname
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_age(self):
        return self.age
    
    def __str__(self):
        return f'{self.fname} {self.lname} age: {self.age} height: {self.height} weight: {self.weight}'
    
def kiloToLb(weight):
    return weight * 2.2
    
def lbToKilo(weight):
    return weight / 2.2
    
def make_person():
    name = random.choice(['bob', 'rob', 'job'])
    lname = random.choice(['bobbertson', 'robertson', 'schloingilius'])
    age = random.randint(18, 80)
    height = random.uniform(1.0, 2.3)
    weight = random.randint(70, 100)

    return Person(name, lname, height, weight, age), Papers(name, lname, height, weight, age)

def game():
    people = []
    score = 0
    for i in range(10):
        a, b = make_person()
        people.append([a, b])

    for person in people:
        d3 = random.randint(1, 3)
        if d3 == 2:
            person[0].set_weight(15)

    for person in people:
        print('person')
        print(person[0])
        print('papers')
        print(person[1])

        if input('is this person smuggling a turkey? ') == 'y':
            if person[0].get_weight() - person[1].get_weight() == 15:
                print('this person was indeed smuggling a turkey.  Take them to prison. ')
                score += 1
            else:
                continue
        else:
            continue

    print(f'Your final score is {score}')

game()