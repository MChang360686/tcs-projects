import random

def choose_question():
    return random.choice(['who is best coach', \
                        'who is the captain now', \
                        'why are we here', \
                        'where do you keep the beans', \
                        'Grab Bag'])

def quiz():
    while True: ans=input(choose_question()); print(ans)

quiz()