from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

EMAIL = "waddaboddle@gmail.com"
PASSWORD = "CemGxDMCwLjY@Exw6"
PHONE_NUMBER = "5148654275"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3720757954&f_AL=true&geoId=101330853&keywords=python%20developer&location=Montreal%2C%20Quebec%2C%20Canada&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

sign_in = driver.find_element(By.XPATH, value="/html/body/div[4]/a[1]")
time.sleep(2)
sign_in.click()

email = driver.find_element(By.ID, value="username")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
apply.click()

time.sleep(3)

phone_number = driver.find_element(By.CSS_SELECTOR, value=".fb-dash-form-element input")
phone_number.send_keys(PHONE_NUMBER)

time.sleep(1)

next_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-easy-apply-content button")
next_button.click()

next_button_second = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Continue to next step"]')
next_button_second.click()

question_one = driver.find_element(By.CSS_SELECTOR, value=)