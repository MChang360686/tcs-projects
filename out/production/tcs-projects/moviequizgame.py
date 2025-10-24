import random

q = {
        'what animal is most closely related to humans?': 'chimpanzee', \
        'what is the largest mammal?': 'blue whale'
    }

def choose_question():
    return random.choice(list(q.keys()))

def check_ans(que, ans):
    return True if q[que] == ans else False

def quiz():
    while True: question = choose_question(); \
        answer = input(question); \
        print(check_ans(question, answer))

quiz()
