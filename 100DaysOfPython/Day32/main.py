import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "pythontesting542@gmail.com"
MY_PASSWORD = "xxhr qtgx tuxx gaag"


with open("quotes.txt") as data_file:
    quotes_list = data_file.readlines()

quote_of_the_day = choice(quotes_list)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 5:

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="pythontesting456@yahoo.com",
                            msg=f"Subject:Saturday Quote\n\n{quote_of_the_day}"
                            )


# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# data_of_birth = dt.datetime(year=1999, month=3, day=5, hour=12)
# print(data_of_birth)
