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

t1.goto(300, 60)
