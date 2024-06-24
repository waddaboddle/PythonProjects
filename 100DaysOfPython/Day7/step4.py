# Step 4

import random
import hangman_art
import hangman_words


end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# Set 'lives' to equal 6.
lives = 6
print(hangman_art.logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
bad_guess = []
for _ in range(word_length):
    display += "_"

print(hangman_art.stages[lives])
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    if guess in display:
        print(f"You have already guessed the letter {guess}. ")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life")
        bad_guess += guess
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose. ")
    if "_" not in display:
        end_of_game = True
        print(hangman_art.stages[lives])
        print(f"{' '.join(display)}")
        print("You win!")
    if "_" in display:
        print(hangman_art.stages[lives])
        print(f"{' '.join(display)}")
