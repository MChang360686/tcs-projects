import random

def opp_num():
    num = []
    for i in range(0, 4):
        num.append(random.randint(0, 9))
    return num

def game():
    hidden_number = opp_num()
    win = False

    for i in range(0, 8):
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
            win = True
            break

        print(ans)

    if win == False:    
        print("You Lose")
        print(hidden_number)

game()
