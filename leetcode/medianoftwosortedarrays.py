n1 = [1, 3]
n2 = [2]
n3 = [1, 2]
n4 = [3, 4]

def naive(list, list2):
    list.extend(list2)
    list.sort()
    if len(list) % 2 == 1:
        index = len(list) // 2
        return list[index]
    else:
        index = len(list) // 2
        return (list[index] + list[index - 1]) / 2

print(naive(n1, n2))
print(naive(n3, n4))

'''https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/'''