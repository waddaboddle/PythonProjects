# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")  # This is a list
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

num_people = len(names)
randnum = random.randint(0, num_people - 1)
person_paying = names[randnum]

print(f"{person_paying} is going to buy the meal today!")

# person_paying = random.choice(names)

# print(f"{person_paying} is going to buy the meal today!")
