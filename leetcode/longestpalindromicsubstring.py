s = 'babad' #bab or aba

def lps(s):
    longest_str = ''
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            str_start = s[i:j]
            if str_start == str_start[::-1]:
                if len(str_start) > len(longest_str):
                    longest_str = str_start

    return longest_str
print(lps(s))

def lps_better(s):
    if len(s) <= 1:
        return s[0]
    else:
        longest = ''

        for i in range(0, len(s)):
            start = i
            stop = i+1
            while start != 0 and stop != len(s):
                if start != 0:
                    start -= 1
                if stop != len(s):
                    stop += 1

                substring = s[start:stop]
                print(substring)

                if substring == s[::-1]:
                    if len(substring) > len(longest):
                        longest = substring

        return longest
    
print(lps_better(s))
