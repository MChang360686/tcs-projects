
def fib_iterative(num):
    a = 0
    b = 1
    for i in range(0, num):
        c = a + b
        a = b
        b = c
        print(a, b)

fib_iterative(10)

def fib_recursive(a, b, c):
    if c == 0:
        return
    else:
        d = a + b
        a = b
        b = d
        print(a, b)
        return fib_recursive(a, b, c-1)

print(fib_recursive(0, 1, 10))