import random

"""
Practice writing a function, using a for loop,
calling a function within a function
"""
def d6():
    return random.randint(1, 6)

def fill_list():
    l = []
    for i in range(0, 10):
        l.append(d6())

    return l

def print_list(list):
    for item in list:
        print(item)

def check_for_3(list):
    for number in list:
        if number == 3:
            print("Found 3")
        else:
            continue

print(d6())
print(fill_list())
x = fill_list()
print_list(x)
check_for_3(x)