import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

phone_dict = {row.letter: row.code for index, row in data.iterrows()}
print(phone_dict)


def generate_phonetic():
    name = input("Enter a word: ").upper()
    try:
        list_of_phonetic_code = [phone_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list_of_phonetic_code)


generate_phonetic()
