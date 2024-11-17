class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_height(self):
        return self.height
    
    def set_height(self, new_height):
        self.height = new_height

    def get_weight(self):
        return self.weight
    
    def set_weight(self, new_weight):
        self.weight = new_weight


steve = Person("Steve", 20, 6, 200)
print(steve.height)