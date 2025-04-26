arr = [1, 2, 3, 4, 5]

target = 6

def naive_solve(target, list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                print(list[i], list[j])
            else:
                continue

def solve(targetNum, numList):
    values = {}

    for i in range(0, len(arr)):
        if numList[i] not in values.keys():
            values[numList[i]] = i
        complement = targetNum - numList[i]
        if complement in values.keys():
            print(values[complement], i)
        else:
            continue

#print(solve(target, arr))
print(naive_solve(target, arr))

'''T'''