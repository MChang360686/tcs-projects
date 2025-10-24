#https://leetcode.com/problems/reverse-integer/description/

def reverse(integer):
    if integer < -2 ** 31 or integer > 2 ** 31 - 1:
        return 0
    else:
        if integer < 0:
            s = str(integer)
            s = s[1:len(s)]
            s = s[::-1]
            s = '-' + s
        else:
            s = str(integer)
            s = s[::-1]
        for i in range(0, len(s)):
            if s[i] == '-':
                continue
            elif s[i] == '0' and s[i + 1] != '0':
                s[i]

        return s
    
print(reverse(-123))
print(reverse(120))