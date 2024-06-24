import os
from data_manager import DataManager
from flight_search import FlightSearch
from twilio.rest import Client

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

client = Client(account_sid, auth_token)

data_manager = DataManager()
flight_search = FlightSearch()

iata_codes = data_manager.get_iata_codes()
prices = data_manager.get_prices()
search_results = []


for iata_code, price in zip(iata_codes, prices):
    search_result = flight_search.search_flights(iata_code, price)
    search_results.append(search_result)

print(search_results)

for result in search_results:
    if result is None:
        pass
    else:
        text = f"Low price alert! Only {result['price']} CAD to fly from {result['city_from']}-{result['dep_iata_code']} to {result['city_to']}-{result['dest_iata_code']}, from {result['from_date']} to {result['to_date']}"
        print(text)
        message = client.messages.create(
            from_='+13345106363',
            body='Bring an umbrella, it might rain ☔.',
            to='+15148654275'
        )
        print(message.status)
