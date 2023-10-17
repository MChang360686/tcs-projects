#!/usr/bin/python3

# Ask for a message and a shift number


# use a dictionary to store the alphabet and their
# associated numbers as key value pairs
# Then, SHIFT the value assigned to each number
# by the given amount.  

# Concepts covered: Dictionaries, Lists, inputs, loops, functions, casting datatypes

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def getMsgInput():
  userInput = input("Please enter a message to encrypt (lowercase)")
  return userInput

def getKeyInput():
  userKey = int(input("Please input a number"))
  return userKey

def createDict():
  alphList = list(alphabet)
  

def shift(alphabetDict, shiftNum):
  for item in alphabetDict.keys():
    letter = alphabetDict[item]
    letter = (letter + shiftNum) % 26
    alphabetDict[item] = letter
  print(alphabetDict)
  return alphabetDict

def encrypt(message, alphabetDict):
  msgList = list(message)
  for letter in msgList:
    if letter in alphabetDict.keys():
      letter = alphabetDict[letter]
    
  msg = msgList.join()
  return msg

if __name__ == '__main__':
  pass