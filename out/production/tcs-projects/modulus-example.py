
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetDict = {}
i = 0
for letter in alphabet:
    alphabetDict[letter] = i + 2
    i += 1
    
print(alphabetDict)
