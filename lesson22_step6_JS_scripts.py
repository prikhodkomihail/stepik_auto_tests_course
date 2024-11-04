from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get("https://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element(By.ID, "input_value")
    y = calc(x_element.text)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    button.click()

    time.sleep(10)


