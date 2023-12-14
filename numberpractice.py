import time

starttime = time.time()

"""name = 'robert'

for letter in name:
    print(letter)"""

"""for i in range(5, 0, -1):
    print(i)"""

"""num = 0
while num <= 5:
    print(num)
    num+=1"""

"""value = False
while value != True:
    print("Value is False")
    value = True"""


def printNum(num):
    print(num)

printNum(4)

endtime = time.time()
timeelapsed = endtime - starttime

print(timeelapsed)