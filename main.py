import pandas as pd

nato_phonetic_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_list = {row.letter: row.code for (index, row) in nato_phonetic_df.iterrows()}

word = input("Type in a name: ").upper()

phonetic_name = [nato_phonetic_list[letter] for letter in word]

print(phonetic_name)
