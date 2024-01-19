import random

numbers = []

"""
Makes a list of pre-determined size of "random" floats
"""
def make_num_list(length):
    for i in range(0, length):
        num = random.random()
        numbers.append(num)

"""
Finds smallest element and brings it to the first position
"""
def select_sort(list):
    for i in range(len(list)):
        smallest = i
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                smallest = j
        list[i], list[smallest] = list[smallest], list[i]

    print(list)

"""
Iterates through list and puts item in the correct position
"""
def insert_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

    print(list)


if __name__ == '__main__':
    make_num_list(5)
    print(numbers)
    #select_sort(numbers)
    insert_sort(numbers)
    