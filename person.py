class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f'Name: {self.name} Age: {self.age} Height: {self.height}'
    
person = Person('Bob', 32, 6.0)
person2 = Person('Alice', 26, 5.5)
print(person)
print(person2)