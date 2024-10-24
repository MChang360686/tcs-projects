import random

x = 5
if x == 4:
    print(4)
elif x == 5:
    print(5)
else:
    print('IDK')

d = [1, 2, 3, 4, 5, 6]

y = random.choice(d)

'''match y:
    case 1:
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)
    case 4:
        print(4)
    case 5:
        print(5)
    case 6:
        print(6)
    case _:
        print('IDK')'''

def twenty_one_rocks():

    rocks = 0
    while rocks < 21:
        player_rocks = int(input("Please enter a number between 1 and 3"))

        if player_rocks > 3 or player_rocks < 1:
            continue

        rocks += player_rocks
        
        match(rocks):
            case 1:
                rocks += 3
                print("CPU adds 3 rocks")
            case 2:
                rocks += 2
                print("CPU adds 2 rocks")
            case 3:
                rocks += 1
                print("CPU adds 1 rock")
            case _:
                continue
        print(rocks)
    print("You lose")

twenty_one_rocks()


"""
Basic if/else statements.

Show switch statements (match)

Explain why we'd use either

Proceed to teach Joe's 4 stones algorithm game
"""