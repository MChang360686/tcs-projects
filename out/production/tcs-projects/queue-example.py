list = [1, 2, 3, 4, 5]

def enqueue(list, item):
    list.append(item)

def dequeue(list):
    list.pop(0)

def is_empty(list):
    if len(list) == 0:
        return True
    else:
        return False
    
def peek(list):
    return list[0]


print(peek(list))












