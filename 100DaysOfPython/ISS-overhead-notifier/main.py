import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 45.501690
MY_LNG = -73.567253
MY_EMAIL = "pythontesting542@gmail.com"
MY_PASSWORD = "xxhr qtgx tuxx gaag"

LOCAL_UTC_OFFSET = -5


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LNG + 5 >= iss_longitude >= MY_LNG - 5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    lt_sunrise = utc_to_local(sunrise)
    lt_sunset = utc_to_local(sunset)
    time_now = datetime.now()

    print(f"sunset: {lt_sunset}")
    print(f"sunrise: {lt_sunrise}")
    print(f"now: {time_now.hour}")

    if not lt_sunrise <= time_now <= lt_sunset:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_close() and is_dark():
        print("Look up")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="muhai0503@gmail.com",
                                msg=f"Subject:Look Up!\n\nLook up! The ISS is up there somewhere!")

# If the ISS is close to my current position,
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
