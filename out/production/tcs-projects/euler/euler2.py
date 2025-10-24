import time

def fib(a, b):
    l = []
    l.append(a)
    l.append(b)
    for _ in range(0, 34):
        l.append(a + b)
        temp = a + b
        a = b
        b = temp

    return l

def naive(list):
    sum = 0

    for num in list:
        if num % 2 == 1:
            continue
        else:
            sum += num

    return sum

def better(list):
    sum = 0
    i = 1

    while i < len(list):
        sum += list[i]
        i += 3

    return sum

l = fib(1, 2)

start = time.process_time()
naive = naive(l)
end = time.process_time()
print(f'naive: {naive} {end - start}')

start = time.process_time()
better = better(l)
end = time.process_time()
print(f'naive: {better} {end - start}')

'''https://projecteuler.net/problem=2'''