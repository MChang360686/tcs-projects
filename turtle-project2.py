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


t1.goto(300,60)
t1.pendown()
t1.circle(40)
t1.penup()
t1.goto(-200,100)

t2.goto(300,-140)
t2.pendown()
t2.circle(40)
t2.penup()
t2.goto(-200,-100)


die = [1,2,3,4,5,6]

for i in range(20):
    if t1.pos() >= (300,100):
        print("Player One Wins!")
        break
    elif t2.pos() >= (300,-100):
        print("Player Two Wins!")
        break
    else:
        player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        t1.fd(20*die_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        t2.fd(20*die_outcome)

