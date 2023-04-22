import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:
phone_dict = {row.letter: row.code for index, row in data.iterrows()}
# print(data1)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: ").upper()
list_of_phonetic_code = [phone_dict[letter] for letter in name]
print(list_of_phonetic_code)
