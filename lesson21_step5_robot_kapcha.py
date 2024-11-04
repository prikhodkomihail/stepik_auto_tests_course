from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    cb = browser.find_element(By.ID, "robotCheckbox")
    cb.click()

    rb = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rb.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()