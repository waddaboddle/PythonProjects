from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

EMAIL = "pythontesting542@gmail.com"
PASSWORD = "%@3F%SR$YK9FXSM%p"
PROMISED_UP = 50
PROMISED_DOWN = 1000

istb = InternetSpeedTwitterBot()

# istb.get_internet_speed()
istb.tweet_at_provider(EMAIL, PASSWORD, PROMISED_DOWN, PROMISED_UP)
