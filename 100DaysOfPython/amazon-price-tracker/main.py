from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

MY_EMAIL = "pythontesting542@gmail.com"
MY_PASSWORD = "xxhr qtgx tuxx gaag"
url = "https://www.amazon.ca/gp/product/B07P5K93ZN/ref=ox_sc_saved_title_1?smid=A162NJZ8LAARQB&psc=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
}

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price_whole = soup.find(class_="a-price-whole")
price_fraction = soup.find(class_="a-price-fraction")
price = float(f"{price_whole.get_text()}{price_fraction.get_text()}")

product_title = soup.find(id="productTitle").get_text().strip()
print(product_title)

target_price = 100

if price <= target_price:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="muhai0503@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now ${price}.\n{url}")
