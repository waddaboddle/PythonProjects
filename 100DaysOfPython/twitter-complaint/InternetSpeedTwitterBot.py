from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = None
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = None
        self.up = None
        self.speed = []

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_test = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        time.sleep(5)
        start_test.click()
        time.sleep(60)
        close_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        close_button.click()
        self.down = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self, email, password, promised_down, promised_up):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        email_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(email)

        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()

        time.sleep(5)

        password_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(password)



