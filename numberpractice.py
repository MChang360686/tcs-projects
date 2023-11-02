import time

starttime = time.time()

name = 'robert'

for letter in name:
    print(letter)

endtime = time.time()
timeelapsed = endtime - starttime

print(timeelapsed)