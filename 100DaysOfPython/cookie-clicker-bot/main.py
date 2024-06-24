from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

t_end = time.time() + 60*5

def check_upgrades():
    if

while time.time() < t_end:
    cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
    cookie.click()





