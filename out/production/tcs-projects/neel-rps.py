import random

opt = ["rock", "paper", "scissors"]

def choose():
    return random.choice(opt)

def check(a, b):
    if a == b:
        return "tie"
    elif a == "rock" and b == "scissors":
        return "a"
    elif a == "rock" and b == "paper":
        return "b"
    elif a == "paper" and b == "rock":
        return "a"
    elif a == "paper" and b == "scissors":
        return "b"
    elif a == "scissors" and b == "paper":
        return "a"
    elif a == "scissors" and b == "rock":
        return "b"
    else:
        return "b"
    
def game():
    a = input("Enter rock, paper, or scissors: ")
    b = choose()
    if check(a, b) == "a":
        print("You win!")
    elif check(a, b) == "b":
        print("You lose!")
    else:
        print("It's a tie!")
game()