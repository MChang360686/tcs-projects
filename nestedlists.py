records = [["chi", 20.0], ['beta', 50.0], ['alpha', 50.0]]


d = {}
names = []
scores = []

for record in records:
    d[record[0]] = record[1]

    if record[1] in scores:
        continue
    else:
        scores.append(record[1])

scores.sort()
penultimate_score = scores[1]

for student in d:
    if d[student] == penultimate_score:
        names.append(student)

names.sort()
for name in names:
    print(name)

