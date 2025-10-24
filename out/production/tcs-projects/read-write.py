import os

# How can we check for directories (folders)?
directories = os.listdir()

for directory in directories:
    print(directory)

# Explain Read, Write, eXecute

with open('data.txt', 'w') as f:
    data = 'Hi'
    f.write(data)

with open('data.txt', 'r') as f:
    data = f.read()
    print(data)
