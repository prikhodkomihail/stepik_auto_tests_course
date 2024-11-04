from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get("https://SunInJuly.github.io/alert_accept.html")

    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    browser.switch_to.alert.accept()
    time.sleep(2)

    x_element = browser.find_element(By.ID, "input_value")
    y = calc(x_element.text)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.TAG_NAME, 'button').click()

    time.sleep(1)

    print(browser.switch_to.alert.text.split(': ')[-1])


