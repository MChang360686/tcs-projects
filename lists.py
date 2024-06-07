input = [20, "append 30", "insert 1 3", "print"]
list = []

for command in input:
    if type(command) == int:
        list.append(command)
    elif type(command) == str:
        c = command.split()
        print(c)
        if c[0] == "append":
            list.append(int(c[1]))
        elif c[0] == "insert":
            list.insert(int(c[1]), int(c[2]))
        elif c[0] == "print":
            print(list)