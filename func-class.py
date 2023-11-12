#!/usr/bin/python3

# List of functions to show *what* functions can do
# Additionally, a class to demonstrate creating objects

class car():
    numWheels = 4
    color  ='red'

def func():
    print("This is a function")

def funcInput(a, b, c):
    print("The function can take an input " + a + b + c)

def iteration(num):
    for i in range(0, num):
        print(i)

def recursion(input):
    if input == 0:
        print("base case" + input)
    else:
        print(input-1)
        return recursion(input - 1)
    
(lambda a, b : a + b)(3, 5)

def sum(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

def printWordList():
    wordList = ["this", 'is', 'a', 'list']
    for word in wordList:
        print(word)

numList = [1, 0, 4, 5, 7, 3, 9, 5, 6]

stack = []

def push(number):
    stack.insert(0, number)

def pop():
    value = stack[0]
    stack.pop(0)
    return value

#printWordList()

"""push(5)
push(7)
push(8)

print(stack)

pop()

print(stack)

push(6)

print(stack)


pop()

print(stack)
"""

numberList = []

def enqueue(item):
    numberList.append(item)

def dequeue():
    value = numberList[0]
    numberList.pop(0)
    return value

def isEmpty():
    if len(numberList) == 0:
        return True
    else:
        False

def size():
    return len(numberList)

enqueue(5)
enqueue(6)
enqueue(7)
print(numberList)
print(size)
print(isEmpty())
dequeue()
print(numberList)

