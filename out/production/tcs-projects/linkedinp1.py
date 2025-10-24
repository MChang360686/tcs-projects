def f(x):
    return x + 1


def g(x):
    return x * 2

def h(x):
    return f(g(x))

print(h(2))
