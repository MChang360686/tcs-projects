import random

def choose_question():
    return random.choice(['who is best coach', \
                        'who is the captain now'])

def check_ans(ans):
    return True if ans in {'who is best coach': 'Alice', 'who is the captain now': 'Bob'}.values() else False

def quiz():
    while True: ans=input(choose_question()); print(check_ans(ans))

quiz()