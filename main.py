import pandas as pd

# for (key, value) in student_dict.items():

# for (index, row) in student_data_frame.iterrows():
# Access index and row
# Access row.student or row.score

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_phonetic_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_list = {row.letter: row.code for (index, row) in nato_phonetic_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type in a name: ")

phonetic_name = [nato_phonetic_list[letter.upper()] for letter in user_input]

print(phonetic_name)
