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

