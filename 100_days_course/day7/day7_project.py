import random
import replit
from stage import stage, logo
from hangman_words import word_list

# words = ['marta', 'banan', 'jablko']
words = word_list

lives = 0
word_to_find = random.choice(words)
# print(word_to_find) # To Check the words

print(logo)
out = []
for _ in range(len(word_to_find)):
    out += '_'
print(out)

is_guess = False

while not is_guess:
    guess = input('Guess a letter >>> ').lower()
    # replit.clear()
    print('\n' * 80)
    if guess in word_to_find:
        for ind, char in enumerate(word_to_find):
            if guess == char:
                out[ind] = char
        print('You guess a correct letter')
    else:
        lives += 1
        print('You guess a wrong letter')

    print(stage[lives])
    print(out)

    if '_' not in out:
        is_guess = True
        print('You win!')

    if lives == 6:
        is_guess = True
        print('You lose!')
