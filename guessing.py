import random

list = []

d6 = [1, 2, 3, 4, 5, 6]

"""
Choose an item from a die (list of nums)
"""
def roll_die(die):
    return random.choice(die)

"""
Check if number is less than or greater than
actual number
"""
def check_num(num1, num2):
    if num1 == num2:
        return True
    else:
        return False

"""
Play game (use a while loop)
"""
def play():
    num = roll_die(d6)
    while True:
        player_guess = int(input("Please enter a number to guess"))

        if check_num(num, player_guess):
            print("Congratulations! You guessed correctly!")
            player_response = input("Play again? (y/n)")
            if player_response == 'y':
                continue
            else:
                False
        else:
            print("Not Quite...")

if __name__ == '__main__':
    pass