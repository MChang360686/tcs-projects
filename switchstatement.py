import random

# review switch statements in Python

num = random.choice([1, 2, 3, 4, 5, 6, 7, 8])

match num:
    case 1: 
        print(num)
    case 2:
        print(num)
    case 3:
        print(num)
    case 4:
        print(num)
    case 5:
        print(num)
    case 6:
        print(num)
    case 7:
        print(num)
    case 8:
        print(num)
    case _:
        print("Not a number 1-8")
