

def printWord(word):
    print(word)

numbers = [0, 1, 2, 3]
endpoint = len(numbers) - 1

def recursivelyPrint(index):
    if index == endpoint:
        print(numbers[endpoint])
    else:
        print(numbers[index])
        return recursivelyPrint(index + 1)
    
def iterativelyPrint(index):
    for item in numbers:
        print(item)
    
#printWord("pain")

recursivelyPrint(0)