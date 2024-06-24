# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art


def guess_check(user_guess, turns, answer):
    if user_guess == answer:
        print(f"You got it! The answer was {answer}")
    elif user_guess > answer:
        print("Too high. ")
        return turns - 1
    elif user_guess < answer:
        print("Too low. ")
        return turns - 1


def guessing_game():
    print(art.logo)

    number = random.randint(1, 100)
    print(f"Here is the answer for testing: {number}")
    print("I'm thinking of a number between 1-100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "hard":
        attempts = 5
    elif difficulty == "easy":
        attempts = 10
    print(f"You have {attempts} attempts to guess the number")

    lives = attempts

    guess = 0

    while guess != number:
        guess = int(input("Make a guess: "))
        lives = guess_check(guess, lives, number)

        if lives == 0:
            print("You've run out of guesses, you lose! ")
        elif guess != number:
            print("Guess again.")
            print(f"You have {lives} attempts remaining to guess the number. ")

        # lives -= 1
        # if 0 < lives < attempts and play_game:
        #     print("Guess again.")
        #     print(f"You have {lives} attempts remaining to guess the number. ")
        # elif lives == 0:
        #     print("You've run out of guesses, you lose! ")
        #     play_game = False


guessing_game()
