x = 1
y = 2

# Swap variables w/o hardcoding
temp = x
x = y
y = temp

#print(x, y)

def fib(a, b):
    print(a, b)
    for i in range(0, 10):
        c = a + b
        a = b
        b = c
        print(c)

fib(0, 1)