import time

starttime = time.time()

name = 'robert'

for letter in name:
    print(letter)

for i in range(0, 5):
    print(i)

num = 0
while num < 5:
    print(num)
    num+=1

endtime = time.time()
timeelapsed = endtime - starttime

print(timeelapsed)