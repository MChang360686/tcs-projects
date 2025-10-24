a = 'abcabcbb'
b = 'bbbbb'
c = 'pwwkew'

def longest_substring(string):
    longest = 0
    d = {}
    for i in range(0, len(string)):
        d[string[i]] = 0
        for j in range(i+1, len(string)):
            if string[j] in d.keys():
                break
            else:
                d[string[j]] = 0
                
        if len(d) > longest:
            longest = len(d)
        d.clear()

    return longest
            
print(longest_substring(a))
print(longest_substring(b))
print(longest_substring(c))