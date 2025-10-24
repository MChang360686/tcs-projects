str = 'hello world'

def letter_capitalize(str):
    split_str = str.split(' ')
    result = ''
    
    for word in split_str:
        word = word[0].upper() + word[1:]
        result += word + ' '

    result = result[:-1]

    result = result + 'k467jf8unc29'

    split_result = list(result)

    j = 0
    for i in range(0, len(split_result)):
        j += 1
        if j % 3 == 0:
            split_result[i] = 'X'
            j = 0

    result = ''.join(split_result)
    return result

print(letter_capitalize(str))

print(str.title())