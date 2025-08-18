
l = input("Please type the 7 letters from today's Spelling Bee ")
letters = list(l)
word = ''

for letter in letters:
    word = letter
    for i in range(0, len(l) - 1):
        word += l[1::]
        print(word)
        l += l[0]
        l = l[1::]
        word = letter