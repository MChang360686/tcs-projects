import random

class Person():
    def __init__(self, name):
        self.name = name
        self.loan_amt = random.randint(100, 5000)
        self.repay_factor = random.randint(0, 100)

def generate_people():
    people = []
    names = ['bob', 'rob', 'job']
    for i in range(0, 10):
        people.append(Person(random.choice(names)))

    return people

def game():
    people = generate_people()
    money = 0

    for person in people:
        print(person.name, person.loan_amt, person.repay_factor)

        decision = input("Give loan? (y/n)")

        if decision == 'y':
            if random.randint(0, 100) <= person.repay_factor:
                money += person.loan_amt + (person.loan_amt * 0.05)
            else:
                print("borrower defaulted on loan")
        else:
            continue

    print('Your Score is: ' + str(money))

game()