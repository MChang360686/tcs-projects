log = ["30 99 sign-in", "30 105 sign-out", "12 100 sign-in", "12 120 sign-out"]

def processLogs(log, maxSpan):

    si = {}
    so = {}
    results = []

    for l in log:
        log_strings = l.split(' ')
        print(log_strings)

        if log_strings[2] == 'sign-in':
            si[log_strings[0]] = log_strings[1]
        elif log_strings[2] == 'sign-out':
            so[log_strings[0]] = log_strings[1]

    for entry in so.keys():
        if entry in si.keys():
            if int(so[entry]) - int(si[entry]) <= maxSpan:
                results.append(int(entry))

    results.sort()
    return results

print(processLogs(log, 20))