import random

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.job = ''
        self.credit = 0

    def __str__(self):
        return "first name: " + self.fname + "\nlast name: " + self.lname + "\nage: " + str(self.age)
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.fname + " " + self.lname
    
    def set_age(self, age):
        self.age = age

    def set_name(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def set_job(self):
        pass

    def set_credit_score(self, score):
        self.credit = score

def game():
    
    def __init__(self, capital):
        self.capital = capital
        loans = []

    def get_capital(self):
        return self.capital
    
    def set_capital(self, amt):
        self.capital += amt

    