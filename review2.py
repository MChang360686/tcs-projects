
l = [3, 'strings', True, 3.14]
l.append(3)
l.append(5)
print(l)

x  = 5
x = 2
print(x)

nums = [1, 3, 5, 7, 3]
seen = []

for num in nums:
    if num in seen:
        print(num)
    else:
        seen.append(num)