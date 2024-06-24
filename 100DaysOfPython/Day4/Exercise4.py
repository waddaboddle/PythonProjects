import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

rps = [rock, paper, scissors]
player_choice = int(input("What do you choose? Rock (0), Paper (1) or Scissors (2): \n"))
if player_choice >= 3 or player_choice < 0:
    print("Number not in range")
else:
    print("You chose: " + rps[player_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose: " + rps[computer_choice])

    if player_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 1 and computer_choice == 0:
        print("You lose!")
    elif player_choice == 1 and computer_choice == 2:
        print("You win!")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif player_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("It\'s a draw!")


# Another way of doing it

# if player_choice >= 3 or player_choice < 0:
#     print("Number not in range")
# elif player_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice > player_choice:
#     print("You lose!")
# elif computer_choice == 0 and player_choice == 2:
#     print("You lose")
# elif 2 > player_choice > computer_choice:
#     print("You win!")
# elif computer_choice == player_choice:
#     print("It's a draw!")

