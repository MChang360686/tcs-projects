import random
import time

words = ['hello', 'goodbye', 'flense', 'rotisserie', 'hamburger']

def write_words():
    output_str = ''
    for i in range(0, 30):
        word = random.choice(words)
        output_str += word + ' '

    return output_str

def calc_score(original_words, typed_words):
    words_correct = 0
    o_split = original_words.split(' ')
    t_split = typed_words.split(' ')
    for i in range(0, len(t_split)):
        if o_split[i] == t_split[i]:
            words_correct += 1
        else:
            continue

    original_word_list = list(original_words)
    typed_word_list = list(typed_words)
    num_wrong = 0

    for i in range(0, len(typed_word_list)):
        if original_word_list[i] != typed_word_list[i]:
            num_wrong += 1

    return words_correct, num_wrong


def test():
    start_time = time.time()

    words = write_words()
    typed_words = ''

    for word in words.split(' '):
        typed_word = input(word + ' ')
        typed_words += typed_word + ' '

        end_time = time.time()

        if end_time - start_time >= 10:
            print(calc_score(words, typed_words))
            print("Time's Up!")
            break

test()