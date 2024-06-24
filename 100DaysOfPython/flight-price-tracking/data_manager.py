import requests
import os
from flight_data import FlightData

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
SHEET_KEY = os.getenv("SHEET_KEY")


class DataManager:

    def __init__(self):
        self.prices = {}
        self.header = {}
        self.cities = {}

    def get_cities(self):
        self.header = {
            "Authorization": SHEET_KEY,
        }
        get_city_response = requests.get(url=SHEET_ENDPOINT, headers=self.header)

        self.cities = [city["city"] for city in get_city_response.json()["prices"]]
        self.prices = [city["lowestPrice"] for city in get_city_response.json()["prices"]]
        return self.cities

    def get_iata_codes(self):
        self.get_cities()
        flight_data = FlightData()
        iata_codes = [flight_data.city_code(city) for city in self.cities]

        for i, city in enumerate(self.cities):
            params = {
                "price": {
                    "iataCode": iata_codes[i]
                }
            }

            response = requests.put(url=f"{SHEET_ENDPOINT}/{i + 2}", json=params, headers=self.header)
            response.raise_for_status()
            return iata_codes

    def get_prices(self):
        # self.get_iata_codes()
        self.get_cities()
        return self.prices
