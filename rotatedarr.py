import sys

arr = [0, 1, 2, 3, 4, 5]
arr_two = [4, 5, 0, 1, 2, 3]

def naive(list):
    min = sys.maxint
    for num in list:
        if num < min:
            min = num

    return min


def better(list):
    start, end = 0, len(list) - 1

    while start < end:
        midpoint = (end - start) // 2

        if list[midpoint] < list[end]:
            end = midpoint
        else:
            start = midpoint + 1

    return list[start]

print(better(arr))
print(better(arr_two))