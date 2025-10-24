num_lines = 0

with open('C:/Users/Owner/tcs-projects/cs50/lines.py') as file:
    for line in file:
        if line[0] == '#':
            continue
        elif line.strip() == '':
            continue
        else:
            num_lines += 1

print(num_lines)