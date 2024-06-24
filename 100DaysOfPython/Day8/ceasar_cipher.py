import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text_input, delta, direction_type):
    text_shift = 0
    text_input_list = list(text_input)
    text_output_list = [""] * len(text_input)
    for i in range(0, len(text_input_list)):
        if text_input_list[i] in alphabet:
            text_index = alphabet.index(str(text_input_list[i]))  # Capture the indices of each letter in relation to alphabet
            if direction_type == "encode":
                text_shift = text_index + delta  # Shift the captured indices by the inputted amount to create shifted indices
            elif direction_type == "decode":
                text_shift = text_index - delta
            if text_shift > len(alphabet) - 1 or text_shift < -len(alphabet) + 1:
                text_shift %= len(alphabet)  # This is when ex. text_shift = 24 then we divide by 24 to get 1 and restart the loop
            text_output_list[i] = alphabet[text_shift]  # Pick the letters using the shifted indices and replace the original letters
        else:
            text_output_list[i] = text_input_list[i]
    print(f"The {direction_type}d text is {''.join(text_output_list)}")


print(art.logo)

keep_running = True

while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if restart == "no":
        print("Goodbye!")
        keep_running = False
