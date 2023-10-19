#!/usr/bin/python3

# List of functions to show *what* functions can do
# Additionally, a class to demonstrate creating objects

def func():
    print("This is a function")

def funcInput(a, b, c):
    print("The function can take an input " + a + b + c)

def iteration(num):
    for i in range(0, num):
        print(i)

def recursion(input):
    if input == 0:
        print("base case")
    else:
        print(input-1)
        return recursion(input - 1)
    
if __name__ == '__main__':
    pass