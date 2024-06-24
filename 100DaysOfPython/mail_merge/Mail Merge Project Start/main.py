with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_string = letter_file.read()

for name in names_list:
    letter_to_send = open(f"./Output/ReadyToSend/{name.strip()}.txt", mode="w")
    letter_string.replace("[name]", name.strip())
    letter_to_send.write(letter_string.replace("[name]", name.strip()))
