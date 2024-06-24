import requests
import os

ENDPOINT = "https://api.tequila.kiwi.com/"
LOCATION_ENDPOINT = f"{ENDPOINT}locations/query"
KIWI_KEY = os.getenv("KIWI_KEY")


class FlightData:
    def __init__(self):
        self.header = {
            "apikey": KIWI_KEY
        }

    def city_code(self, city):
        params = {
            "term": city,
            "location_types": "airport",
        }

        response = requests.get(url=LOCATION_ENDPOINT, params=params, headers=self.header)
        code = response.json()["locations"][0]["city"]["code"]
        return code
