##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
from random import choice
import pandas

MY_EMAIL = "pythontesting542@gmail.com"
MY_PASSWORD = "xxhr qtgx tuxx gaag"

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")
letters = []
birth_dates = []
birthday_days = []

for num in range(1, 4):
    with open(f"letter_templates/letter_{num}.txt") as letter_file:
        letters.append(letter_file.read())


now = dt.datetime.now()
current_time = (now.day, now.month)

for i in range(0, len(birthdays)):
    birth_dates.append((birthdays[i]["day"], birthdays[i]["month"]))

recipient_name = [d["name"] for d in birthdays if d["month"] == now.month and d["day"] == now.day]
recipient_email = str([d["email"] for d in birthdays if d["month"] == now.month and d["day"] == now.day])[2:-2]

if current_time in birth_dates:
    letter_to_send = choice(letters).replace("[NAME]", str(recipient_name)[2:-2])
    print(letter_to_send)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=recipient_email,
                            msg=f"Subject:HBD!\n\n{letter_to_send}")

