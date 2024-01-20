import os
import random

letters = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '?']
chars = ['l', 'n', 's']

class Password:
    def __init__(self, length=20) -> None:
        self.length = length

    def generate(self):
        word = ''
        for i in range(0, self.length):
            char = chars.choice()
            match char:
                case 'l':
                    word += letters.choice()
                case 'n':
                    word += str(numbers.choice())
                case 's':
                    word += symbols.choice()

        return word

def make_password():
    pw_gen = Password()
    pw = pw_gen.generate()
    print(pw)

if __name__ == '__main__':
    make_password()