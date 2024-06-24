import pandas

# {"A": "Alfa", "B": "Bravo"}

nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(nato_alphabets)

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

invalid_input = True

while invalid_input:
    word = input("Enter a word: ").upper()
    try:
        nato_word = [nato_dict[letter] for letter in word]
        invalid_input = False
    except KeyError:
        print("Sorry only letters in the alphabet please.")
    else:
        print(nato_word)

