from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pathlib import Path

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("L9gDk@example.com")

    current_dir = Path.cwd()
    browser.find_element(By.ID, "file").send_keys(f"{current_dir}/file.txt")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(10)
