import random

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        
    def get_model(self) -> str:
        return self.model
        
    def get_year(self) -> str:
        return self.year
        
    def get_mileage(self) -> int:
        return self.mileage
        
    def set_mileage(self, amt):
        self.mileage += amt
        
    def __str__(self):
        return f'{self.year} {self.model} with {self.mileage} miles '
        
class Person:
    
    def __init__(self, buyCar):
        self.buyCar = random.randint(0, 1)
        

def game():
    cars = []
    make = ['lamborghini', 'ferrari', 'honda', 'toyota', 'lexus']
    models = [1, 2, 3, 4, 5]
    for i in range(8):
        cars.append(Car(random.choice(make), random.choice(models), random.randint(2000, 2025), random.randint(500, 50000)))
