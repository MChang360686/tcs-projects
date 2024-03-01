import random

d6 = [1, 2, 3, 4, 5, 6]

l = []

def fill_list(list, numList):
    for i in range(0, 10):
        list.append(random.choice(numList))

    return list

l = fill_list(l, d6)
print(l)

def selection_sort(list):

    for i in range(0, len(list)):
        current_min = list[i]
        current_min_index = i
     
        for j in range(1, len(list)):
            if list[j] < current_min:
                current_min = list[j]
                current_min_index = j

        temp = list[i]
        list[i] = current_min
        list[current_min_index] = temp
        

    return list

l = selection_sort(l)
print(l)