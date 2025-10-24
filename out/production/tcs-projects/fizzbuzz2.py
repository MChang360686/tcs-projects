import random
import time

def make_list():
    list = []
    for i in range(1, 1001):
        list.append(i)

    return list

#print(make_list())

def fizz_buzz(list):
    for item in list:
        if (item % 5 == 0 and item % 3 == 0):
            print(f"{item} fizzbuzz")
        elif (item % 5 == 0):
            print(f"{item} buzz")
        elif (item % 3 == 0):
            print(f"{item} fizz")

#fizz_buzz(make_list())
            
def random_list():
    l = []
    length = random.randint(1, 10)
    for i in range(0, length):
        l.append(random.randint(1, 101))

    return l

def queue(list, item):
    list.append(item)

def peek(list):
    print(list[0])

def dequeue(list):
    list.pop(0)

"""queue = random_list()
print(queue)
dequeue(queue)
print(queue)
peek(queue)
queue(queue, 6)
print(queue)"""

def timer(t):
    time.sleep(t)
    print("Time is up")

timer(20)