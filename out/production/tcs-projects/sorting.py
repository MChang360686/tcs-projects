import random

numbers = []

def make_num_list(length):
    for i in range(length):
        num = random.randint(1, 10)
        numbers.append(num)


def select_sort(list):
    for i in range(len(list)):
        smallest = i
        for j in range(i+1, len(list)):
            if list[j] < list[smallest]:
                smallest = j
        list[i], list[smallest] = list[smallest], list[i]

    print(list)

make_num_list(5)
print(numbers)
select_sort(numbers)

def insert_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

    print(list)

numbers.clear()
make_num_list(5)
print(numbers)
insert_sort(numbers)
    