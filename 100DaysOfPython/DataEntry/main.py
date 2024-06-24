from bs4 import BeautifulSoup
import requests
from FillUpBot import FillUpBot

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeDRFFHIgdt9VZ9KHhz5Ay87i_cOTLvop859mwND4xods0Dng/viewform?usp=sf_link"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_URL)
zillow = response.text

soup = BeautifulSoup(zillow, "html.parser")
fill_up_bot = FillUpBot()

raw_links = soup.select(selector=".StyledPropertyCardDataWrapper a")
links = [link.get("href") for link in raw_links]

raw_prices = soup.select(selector=".PropertyCardWrapper span")
prices = [price.get_text().strip("+/mo").strip("1 bd").strip("+") for price in raw_prices]

raw_addresses = soup.select(selector=".StyledPropertyCardDataWrapper address")
addresses = [address.get_text().replace("|", "").strip().replace("  ", " ") for address in raw_addresses]

print(prices)

fill_up_bot.fill_up(addresses, prices, links)

