import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Type in a name: ").upper()

phonetic_name = [phonetic_dict[letter] for letter in word]

print(phonetic_name)
