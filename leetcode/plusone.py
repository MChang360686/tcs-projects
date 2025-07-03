digits = [1, 2, 3]

def add_one(digits):
    num = 0
    for i in range(len(digits) - 1, -1, -1):
        num += digits[i] * (10 ** (len(digits) - 1 - i))
    num += 1

    num = str(num)
    print([int(number) for number in num])


add_one(digits)
