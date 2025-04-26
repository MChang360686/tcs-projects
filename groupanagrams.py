import time
anagrams = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

'''
Return the following

[["eat","tea","ate"],["tan","nat"],["bat"]]
'''

def group(anagrams):
    anagram_groups = {}

    for word in anagrams:
        word_list = sorted(list(word))

        sorted_word = ''.join(word_list)

        if sorted_word in anagram_groups.keys():
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    return [anagram_groups[key] for key in anagram_groups.keys()]

start = time.time()
print(group(anagrams))
stop = time.time()
print(stop - start)

def group_two(a):

    anagram_groups = {}
    hash = {}

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        hash[letter] = 0

    for word in a:

        split_word = list(word)

        for letter in split_word:
            hash[letter] += 1

        hash_num = ''.join(str(hash.values()))

        if hash_num in anagram_groups.keys():
            anagram_groups[hash_num].append(word)
        else:
            anagram_groups[hash_num] = [word]

        for key in hash.keys():
            hash[key] = 0

    return [anagram_groups[key] for key in anagram_groups.keys()]

start = time.time()
print(group_two(anagrams))
stop = time.time()
print(stop - start)

def group_three(anagrams):
    pts = {'a': 1, 'b': 2, 'c': 3}
    groups = {}

    for word in anagrams:
        score = 0
        for letter in word:
            if letter in pts:
                score += pts[letter]

        if score in groups.keys():
            groups[score].append(word)
        else:
            groups[score] = [word]

    return [groups[score] for score in groups.keys()]