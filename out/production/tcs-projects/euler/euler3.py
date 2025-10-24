import time

def is_prime(num):
    for i in range(2, num):
        if num % i != 0:
            continue
        else:
            return False
        
    return True

def naive(num):
    max = 0
    for i in range(2, num):
        if is_prime(i) == True:
            if num % i == 0:
                if i > max:
                    max = i
        else:
            continue
    
    return max


