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

numList = [1, 0, 4, 5, 7, 3, 9, 5, 6]

stack = []

def push(number):
    stack.insert(0, number)

def pop():
    value = stack[0]
    stack.pop()
    return value

push(5)
push(7)
push(8)

print(stack)

pop()

print(stack)
