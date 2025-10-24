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
            
        encryptedMsg += f' {newChar}'
    
    return encryptedMsg

def decryptMsg(encrMsg):
    ctp = {}
    plaintxt = ''
    shift = int(input("Please enter shift num"))

    for i in range(0, 26):
        ctp[i] = letters[i]

    eMsg = encrMsg.split()

    for char in eMsg:
        if int(char) in ctp.keys():
            plaintxt += (ctp[int(char)] - shift)
        else:
            continue

    return plaintxt


msg = encryptMsg(input("Please enter a message"))
print(msg)

print(decryptMsg(msg))



endtime = time.time()

print(f'Time Elapsed: {(endtime - starttime)}')