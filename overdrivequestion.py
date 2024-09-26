listOfNums = [1, 2, 7, 3, 4, 5, 6, 7]

# O(n^2) with n-1 auxillary space
def solutionOne(list):
    subList = []
    for num in list:
        for n in subList:
            if (n == num):
                return n
            else:
                continue
        subList.append(num)
        print(subList)

# O(nlogn + n) with O(n) temp space
def sortSol(list):
    list.sort()
    for i in range(0, len(list)):
        if list[i] == list[i-1]:
            return list[i]
        else:
            continue

# O(n) with O(n) auxillary space
def dictSol(list):
    dictionary = {}
    for item in list:
        if item in dictionary.keys():
            return item
        else:
            dictionary[item] = 'exists'

print(solutionOne(listOfNums))
print(sortSol(listOfNums))
print(dictSol(listOfNums))



