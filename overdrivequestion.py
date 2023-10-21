
# How do we find a duplicate number in a list of n numbers?

# 1) we can sort the array and then find the duplicate
# 2) we can put the 
# 3) naive we can keep a running list of every number we've encountered and list it

listOfNums = [1, 2, 7, 3, 4, 5, 6, 7]

def sortSol(list):
    list.sort()
    for i in range(0, len(list)):
        if list[i] == list[i-1]:
            return list[i]
        else:
            return "No duplicates"

def dictSol(list):
    dictionary = {}
    for item in list:
        if item in dictionary.keys():
            return item
        else:
            dictionary[item] = 'exists'





