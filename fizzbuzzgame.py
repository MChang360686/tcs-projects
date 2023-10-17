#!/usr/bin/python3

# Ask for a number, say 'fizz' if divisibly by 3,
# 'buzz' if divisible by 5, and 'fizzbuzz' if divisible
# by both 

number = int(input("Please enter a number: "))

if number % 5 == 0 and number % 3 == 0:
    print("fizzbuzz")
elif number % 5 == 0:
    print("buzz")
elif number % 3 == 0:
    print("fizz")
else:
    print("Number is neither divisible by 5 or 3")