

def bin_search(list, begin, end, key):
    
    while begin <= end:

        middle = begin + (end - begin) // 2

        if list[middle] == key:
            return list[middle], middle
        elif list[middle] < key:
            begin = middle + 1
        elif list[middle] > key:
            end = middle - 1

    return -1

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#l.sort()
print(bin_search(l, 0, len(l)-1, 4))
