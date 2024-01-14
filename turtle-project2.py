import turtle
import random

# get code from here https://realpython.com/beginners-guide-python-turtle/#final-project-the-python-turtle-race

die = [1, 2, 3, 4, 5, 6]

t1 = turtle.Turtle()
t1.color("green")
t1.shape("turtle")
t1.penup()
t1.goto(-200, 100)
t2 = t1.clone()
t2.color("blue")
t2.penup()
t2.goto(-200, -100)

'''
>>> player_one.goto(300,60)
>>> player_one.pendown()
>>> player_one.circle(40)
>>> player_one.penup()
>>> player_one.goto(-200,100)
>>> player_two.goto(300,-140)
>>> player_two.pendown()
>>> player_two.circle(40)
>>> player_two.penup()
>>> player_two.goto(-200,-100)
'''

t1.goto(300, 60)


"""
>>> die = [1,2,3,4,5,6]

>>> for i in range(20):
...     if player_one.pos() >= (300,100):
...             print("Player One Wins!")
...             break
...     elif player_two.pos() >= (300,-100):
...             print("Player Two Wins!")
...             break
...     else:
...             player_one_turn = input("Press 'Enter' to roll the die ")
...             die_outcome = random.choice(die)
...             print("The result of the die roll is: ")
...             print(die_outcome)
...             print("The number of steps will be: ")
...             print(20*die_outcome)
...             player_one.fd(20*die_outcome)
...             player_two_turn = input("Press 'Enter' to roll the die ")
...             die_outcome = random.choice(die)
...             print("The result of the die roll is: ")
...             print(die_outcome)
...             print("The number of steps will be: ")
...             print(20*die_outcome)
...             player_two.fd(20*die_outcome)
"""
