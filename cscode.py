import time

starttime = time.time()

letters = "abcdefghijklmnopqrstuvwxyz"
alphabet = []

for letter in letters:
    alphabet.append(letter)

    
cipher = {}

for i in range(0, 26):
    cipher[alphabet[i]] = i

def getShiftInput():
    shift = int(input("Please enter an integer to shift the code by"))
    return shift

print(cipher)

shiftNum = getShiftInput()

for key in cipher.keys():
    cipher[key] = (cipher[key] + shiftNum) % 26

print(cipher)

def encryptMsg(msg):
    encryptedMsg = ''
    for character in msg:
        match character:
            case ' ':
                continue
            case _:
                newChar = cipher[character]
            
        encryptedMsg += f' {str(newChar)}'
    
    return encryptedMsg

msg = encryptMsg(input("Please enter a message"))

print(msg)

def decryptMsg(msg):
    decryptedStr = ''

    for key in cipher.keys(): 
        num = (cipher[key] - shiftNum)
        if num < 0:
            num += 26
        cipher[key] = num

    for letter in msg:
        value = cipher[letter]
        decryptedStr.append(str(value))

    return decryptedStr


print(decryptMsg(msg))




endtime = time.time()

print(f'Time Elapsed: {(endtime - starttime)}')