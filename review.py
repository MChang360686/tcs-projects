import random

x = 5

bool_var = True

float = 1.2

char = "a"

str_var = "abcdefghijklmnopqrstuvwxyz"

list = [1, 2, 3]

def function(word):
    print("This is a function")
    print(word)

def print_list(l):
    if len(l) == 0:
        print("List is empty")
    else:
        for item in l:
            print(item)

if __name__ == '__main__':
    function("tacos")