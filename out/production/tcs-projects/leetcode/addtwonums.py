l1 = [2, 4, 3]
l2 = [5, 6, 4]

def solution(list_one, list_two):
    a, b = [], []
    n1, n2 = '', ''

    for i in range(len(list_one) - 1, -1, -1):
        a.append(list_one[i])

    for num in a:
        n1 += str(num)

    for i in range(len(list_two) - 1, -1, -1):
        b.append(list_two[i])

    for num in b:
        n2 += str(num)

    n1 = int(n1)
    n2 = int(n2)

    sum = str(n1 + n2)

    return [int(num) for num in sum[::-1]]

print(solution(l1, l2))

'''ans = [7, 0, 8]'''