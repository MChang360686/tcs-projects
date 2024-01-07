x = 4


list = [1, 2, 3, 4, 5]

def printList(l):
    for num in l:
        num += 3
        print(num)

def compare(a, b):
    if(a > b):
        print("One Thing")
    else:
        print("Another Thing")

"""for i in range(0, 5):
    print(i)"""

printList(list)
compare(5, 8)
