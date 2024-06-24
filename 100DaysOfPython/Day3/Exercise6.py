# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lowercase = name1.lower()
name2_lowercase = name2.lower()
name_joined = name1_lowercase + name2_lowercase

t_count = name_joined.count("t")
r_count = name_joined.count("r")
u_count = name_joined.count("u")
e_count = name_joined.count("e")
l_count = name_joined.count("l")
o_count = name_joined.count("o")
v_count = name_joined.count("v")

digit_1 = t_count + r_count + u_count + e_count
digit_2 = l_count + o_count + v_count + e_count
love_score = int(f"{digit_1}{digit_2}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")

