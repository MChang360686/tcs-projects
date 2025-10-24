
stack = []

def push(list, item):
    list.append(item)

def pop(list):
    return list.pop()

def reverse(stack, temp):
    if len(stack) == 0:
        return temp
    else:
        item = pop(stack)
        push(temp, item)
        return reverse(stack, temp)

push(stack, 3)
push(stack, 2)
push(stack, 1)
print(stack)

s = reverse(stack, [])
print(s)
