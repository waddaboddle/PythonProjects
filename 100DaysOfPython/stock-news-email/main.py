import requests
import os
from twilio.rest import Client
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "GC0JORQN9LNLEXY2"
NEW_API_KEY = "e240b5b86fc7433bb3fd2ca2f2b05d67"

TWILIO_KEY = "a950dd91ae1ceada11725d9029a50d98"
TWILIO_SID = "ACf16c1ba481abf32f1f5cd5ef6b2276c4"

client = Client(TWILIO_SID, TWILIO_KEY)

today = date.today()
yesterday = today - timedelta(days=1)
ereyesterday = yesterday - timedelta(days=1)

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

new_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEW_API_KEY
}

## STEP 1: Use https://www.alphavantage.co/documentation/
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yesterday's closing stock price.

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday_stock_price = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])
ereyesterday_stock_price = float(stock_data["Time Series (Daily)"][str(ereyesterday)]["4. close"])

stock_price_delta = yesterday_stock_price - ereyesterday_stock_price
percent_difference = round(100 * abs(stock_price_delta) / yesterday_stock_price, 2)
# percent_difference = 6
print(percent_difference)

news_response = requests.get(NEWS_ENDPOINT, params=new_params)
news_response.raise_for_status()
news_data = news_response.json()["articles"]

articles = [news_data[:3]]

up_down_symbol = None
if percent_difference > 0:
    up_down_symbol = "🔺"
else:
    up_down_symbol = "🔻"

if percent_difference >= 5:

    news_texts = [
        f"{STOCK}: {up_down_symbol}{round(percent_difference)}\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in articles]

    for text in news_texts:
        message = client.messages.create(
            from_='+13345106363',
            body=text,
            to='+15148654275'
        )
        print(message.status)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
