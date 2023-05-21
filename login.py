# login.py

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import credentials

def login():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    time.sleep(2)

    driver.get('https://seller-area.youcan.shop/login')
    time.sleep(5)

    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys(credentials.email)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(credentials.password)
    password_input.send_keys(Keys.ENTER)

    time.sleep(10)

    return driver
