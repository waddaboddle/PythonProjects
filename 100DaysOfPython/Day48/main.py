from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# driver.close()

names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul a")
times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul time")
python_events = {}
index = 0

for name, time in zip(names, times):
    python_events[index] = {"time": time.get_attribute("datetime")[0:10], "name": name.text}
    # print(name.text)
    # print(time.get_attribute("datetime")[0:10])
    index += 1

print(python_events)
driver.quit()
