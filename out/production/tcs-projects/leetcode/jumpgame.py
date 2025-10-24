l1 = [2, 3, 1, 1, 4]
l2 = [3, 2, 1, 0, 4]

def jump(list, index):
    if list[index] == 0:
        if index == len(list) - 1:
            return True
        else:
            return False
    else:
        if index >= len(list) - 1:
            return True
        else:
            return jump(list, index + list[index])

print(jump(l1, 0))
print(jump(l2, 0))

def fib(a, b):
    print(a + b)
    if b > 100:
        return None
    return fib(b, a + b)

fib(0, 1)