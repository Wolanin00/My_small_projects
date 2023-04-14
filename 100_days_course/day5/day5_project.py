import string
import random

print('Welcome in PyPassword Generator!')
letters = int(input('How many letters would you like in your password? >>> '))
symbols = int(input('How many symbols would you like? >>> '))
numbers = int(input('How many numbers would you like? >>> '))

passwors = []
punctuation = string.punctuation
punctuation_to_remove = ['/', '\\', '[', ']', '{', '}', '"', "'", ',', '.']

for char in punctuation_to_remove:
    punctuation = punctuation.replace(char, '')
print(punctuation)

for _ in range(symbols):
    passwors.append(random.choice(punctuation))
for _ in range(numbers):
    passwors.append(random.choice(string.digits))
for _ in range(letters):
    passwors.append(random.choice(string.ascii_letters))

random.shuffle(passwors)

print(f"Your new Password: {''.join(passwors)}")
