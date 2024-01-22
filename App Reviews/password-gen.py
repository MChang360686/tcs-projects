import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '?']
chars = ['l', 'n', 's']

class Password:
    def __init__(self, length=20) -> None:
        self.length = length

    def generate(self):
        word = ''
        for i in range(self.length):
            char = random.choice(chars)
            match char:
                case 'l':
                    word += random.choice(letters)
                case 'n':
                    word += str(random.choice(numbers))
                case 's':
                    word += random.choice(symbols)

        return word

def make_password():
    pw_gen = Password()
    pw = pw_gen.generate()
    print(pw)

if __name__ == '__main__':
    make_password()