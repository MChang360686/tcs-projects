import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def get_random(list):
    return random.choice(list)

def opp_num():
    num = []
    for i in range(0, 4):
        num.append(get_random(nums))
    return num
 
def game():
    round = 1
    hidden_number = opp_num()

    while round <= 8:
        ans = ''
        guess = list(input("Please enter a 4-digit number"))
        print(guess)
        for i in range(0, 4):
            if int(guess[i]) == hidden_number[i]:
                ans += 'A'
            elif int(guess[i]) in hidden_number:
                ans += 'B'
            else:
                ans += '_'

        if ans == 'AAAA':
            print("You Win!")
            print(hidden_number)
            break

        print(ans)
        round += 1
        
    if ans == 'AAAA':
        print("You Win!")
        print(hidden_number)
    else:
        print("You Lose")
        print(hidden_number)

game()
