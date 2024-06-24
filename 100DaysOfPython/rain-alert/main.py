import requests
import os
from twilio.rest import Client

# account_sid = 'ACf16c1ba481abf32f1f5cd5ef6b2276c4'
account_sid = os.environ.get("TWILIO_ACC_SID")
# auth_token = 'a950dd91ae1ceada11725d9029a50d98'
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# api_key = "6cebee372b8ab6b58d7e83a8cd44c1ad"
api_key = os.environ.get("OMW_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
MY_LAT = 45.501690
MY_LNG = -73.567253
EXCLUDE = "current,minutely,daily,alerts"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": EXCLUDE,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

will_rain = False

weather_ids = []

for i in range(0, 11):
    weather_ids.append(data["hourly"][i]["weather"][0]["id"])
    if weather_ids[i] < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    # message = client.messages.create(
    #     from_='+13345106363',
    #     body='Bring an umbrella, it might rain ☔.',
    #     to='+15148654275'
    # )
    # print(message.status)
