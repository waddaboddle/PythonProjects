from game_data import data
from random import randint
from art import vs
from art import logo


def higher_lower():
    play_game = True
    print(logo)
    score = 0

    # Set initial random numbers
    random_A = randint(0, len(data) - 1)

    subject_A = f'{data[random_A]["name"]}, a {data[random_A]["description"]}, from {data[random_A]["country"]}'
    subject_A_followers = data[random_A]["follower_count"]
    data.remove(data[random_A])

    while play_game:

        random_B = randint(0, len(data) - 2)
        # print(f"random_B is : {random_B}")

        # Set the two options to be compared and remove the option when picked from the list to avoid repetition

        subject_B = f'{data[random_B]["name"]}, a {data[random_B]["description"]}, from {data[random_B]["country"]}'
        subject_B_followers = data[random_B]["follower_count"]
        data.remove(data[random_B])

        # Determines the answer
        if subject_A_followers > subject_B_followers:
            answer = "a"
        else:
            answer = "b"

        # Print the options and ask for a guess
        # print(f"The computer thinks the answer is {answer}")
        print(f"Compare A: {subject_A}")
        # print(f"Psst here is the answer for A: {subject_A_followers}")
        print(vs)
        print(f"Against B: {subject_B}")
        # print(f"Psst here is the answer for B: {subject_B_followers}")
        guess_input = input("Who has more followers? Type 'A' or 'B': ")
        guess = guess_input.lower()

        if guess == answer:
            print(logo)
            score += 1
            subject_A = subject_B
            subject_A_followers = subject_B_followers
            print(f"You are right! Current score: {score}.")
            play_game = True
        else:
            print(logo)
            print(f"Sorry that's wrong. Final score {score}")
            play_game = False


higher_lower()
