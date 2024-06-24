from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeDRFFHIgdt9VZ9KHhz5Ay87i_cOTLvop859mwND4xods0Dng/viewform?usp=sf_link"


class FillUpBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(FORM_URL)

    def fill_up(self, addresses, prices, links):
        for i in range(0, len(addresses)):
            time.sleep(1)

            address_input = self.driver.find_element(By.XPATH,
                                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(addresses[i])

            price_input = self.driver.find_element(By.XPATH,
                                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(prices[i])

            link_input = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(links[i])

            submit = self.driver.find_element(By.XPATH,
                                              value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit.click()

            time.sleep(1)

            restart = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            restart.click()
