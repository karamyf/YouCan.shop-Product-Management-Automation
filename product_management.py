# product_management.py

import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
import os


def add_product(driver, product_name):
    driver.get('https://seller-area.youcan.shop/admin/products/create?')
    df = pd.read_excel(f'C:\\Users\\pc\\Desktop\\Home\\Work\\Fiverr\\Customers\\Bilal Hagouch\\Products\\{product_name}\\reviews\\reviews.xlsx')

    for i, row in df.iterrows():
        sku_input = driver.find_element(By.XPATH, "//input[@placeholder='SKU']")
        sku_input.send_keys(row.iloc[4])

        title_input = driver.find_element(By.XPATH, "//input[@placeholder='Name ( Ex: blue summer shirt.. )']")
        title_input.send_keys(row.iloc[5])

        # Rest of the code for entering product information

        save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save")]')
        save_button.click()

        time.sleep(7)

        driver.get('https://seller-area.youcan.shop/admin/products/create?')


def add_review(driver, product_name):
    driver.get("https://seller-area.youcan.shop/admin/products/reviews")
    driver.set_window_size(1936, 1096)
    df = pd.read_excel(f'C:\\Users\\pc\\Desktop\\Home\\Work\\Fiverr\\Customers\\Bilal Hagouch\\Products\\{product_name}\\reviews\\reviews.xlsx')

    for i, row in df.iterrows():
        name = row['Name']
        review = row['Review']
        image_path = row['Picture Path']

        driver.find_element(By.LINK_TEXT, "Add a review").click()

        driver.find_element(By.ID, "first-name").click()
        driver.find_element(By.ID, "first-name").send_keys(name)

        search_input = driver.find_element(By.CSS_SELECTOR, ".input-holder > input")
        search_input.click()

        # Rest of the code

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".button").click()
        driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) label").click()

# product_creation.py


def new_product(client_name, product_name):
    base_path = f"C:\\Users\\pc\\Desktop\\Home\\Work\\Fiverr\\Customers\\{client_name}\\Products\\{product_name}"

    os.makedirs(os.path.join(base_path, "images", "variants"))
    os.makedirs(os.path.join(base_path, "reviews", "images"))
    os.makedirs(os.path.join(base_path, "gifs"))

    reviews_df = pd.DataFrame(columns=["Name", "Review", "Picture Path"])
    reviews_file_path = os.path.join(base_path, "reviews", "reviews.xlsx")
    reviews_df.to_excel(reviews_file_path, index=False)

    print(f"New product '{product_name}' for client '{client_name}' created successfully.")
