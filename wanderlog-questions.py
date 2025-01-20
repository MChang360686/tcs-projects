transactions = ['notebook', 'notebook', 'mouse', 'keyboard', 'mouse']

def groupTransactions(array):
    d = {}
    d_2 = {}

    for item in array:
        if item in d.keys():
            d[item] += 1
        else:
            d[item] = 1
        
    print(d)

    for item in d.keys():
        if d[item] in d_2.keys():
            continue
        else:
            d_2[d[item]] = []
    print(d_2)

    for item in d.keys():
        if d[item] in d_2.keys():
            d_2[d[item]].append(item)
            d_2[d[item]].sort()
    print(d_2)

    arr = []
    for number in d_2.keys():
        for item in d_2[number]:
            arr.append(item + ' ' + str(number))
    print(arr)
    return arr

groupTransactions(transactions)