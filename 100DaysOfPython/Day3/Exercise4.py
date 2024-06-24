# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

leap_4 = False
leap_100 = False
leap_400 = False

if year % 4 == 0:
    leap_4 = True

if year % 100 == 0:
    leap_100 = True

if year % 400 == 0:
    leap_400 = True

if (leap_4 == True) and (leap_400 == True):
    print("Leap year.")
elif (leap_4 == True) and (leap_100 == False):
    print("Leap year.")
# elif (leap_4 == True) and (leap_100 == True) and (leap_400 == False):
#     print("Not leap year.")
else:
    print("Not leap year.")
