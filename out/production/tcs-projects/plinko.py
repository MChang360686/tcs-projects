import random
import os

l = ['', '', '', '', '', '', '', '']

def gen_num() -> int:
    return int.from_bytes(os.urandom(1))

def move_left(num) -> bool:
    if num <= 127:
        return True
    else:
        return False

def print_board() -> None:
    print(l)

def game() -> None:
    disc = 'O'

    start = int(input('Enter a position to drop at(1-8): ')) - 1
    l[start] = disc

    for i in range(0, 10):
        if move_left(gen_num()):
            if start == 0:
                continue
            else:
                l[start] = ''
                start -= 1
                l[start] = disc
        else:
            if start == 7:
                continue
            else:
                l[start] = ''
                start += 1
                l[start] = disc
        print(l)

    print(l)

game()