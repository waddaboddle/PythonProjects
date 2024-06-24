import requests
import os
from datetime import date, timedelta

KIWI_KEY = os.getenv("KIWI_KEY")
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
FLY_FROM = "YUL"
TOMORROW = (date.today() + timedelta(days=1)).strftime("%d/%m/%Y")
SIX_MONTHS = (date.today() + timedelta(weeks=26)).strftime("%d/%m/%Y")


class FlightSearch:

    def __init__(self):
        self.search_result = {}
        self.header = {
            "apikey": KIWI_KEY
        }

    def search_flights(self, destination_city, max_price):
        params = {
            "fly_from": FLY_FROM,
            "fly_to": destination_city,
            "date_from": TOMORROW,
            "date_to": SIX_MONTHS,
            "curr": "CAD",
            "price_from": 0,
            "price_to": max_price,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 21,
            "limit": 100,
        }

        search_response = requests.get(url=SEARCH_ENDPOINT, params=params, headers=self.header)
        if search_response.json()["_results"] > 0:
            data = search_response.json()["data"][0]
            # dep_iata_code = data["flyFrom"]
            # dest_iata_code = data["flyTo"]
            # city_from = data["cityFrom"]
            # city_to = data["cityTo"]
            # price = data["price"]
            # from_date = data["local_departure"]
            # to_date = data["route"][-1]["local_arrival"]

            self.search_result = {
                "dep_iata_code": data["flyFrom"],
                "dest_iata_code": data["flyTo"],
                "price": data["price"],
                "from_date": data["local_departure"][:10],
                "to_date": data["route"][-1]["local_arrival"][:10],
                "city_from": data["cityFrom"],
                "city_to": data["cityTo"],

            }

            return self.search_result

