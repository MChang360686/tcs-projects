import random

words = ["spaghetti"]

insults = ["your parents must be super proud of you"]

word = random.choice(words)
word_list = list(word)

score = len(word_list)
i = 0

player_guesses = []

lives = score + 5

for j in range(0, score):
    player_guesses.append("-")

while i < score:
    print(player_guesses)

    letter = input("Please enter a letter (lowercase) ")

    if letter in word_list:
        letter_index = word_list.index(letter)
        player_guesses[letter_index] = letter
        i += 1
    else:
        print(random.choice(insults))
        lives -= 1
        if lives <= 0:
            print("You Lose")
            break
        continue

    

print("You Win")


