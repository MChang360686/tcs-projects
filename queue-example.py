

list = [1, 2, 3, 4, 5]

def enqueue(value):
    list.append(value)

def dequeue():
    list.pop(0)

def getLength():
    return len(list)

def peek():
    print(list[0])

print(list)
enqueue(32)
print(list)
dequeue()
print(list)
peek()
print(getLength())



