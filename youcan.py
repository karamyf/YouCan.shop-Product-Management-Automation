import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import credentials
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import os

def login():
    # Set up the webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    time.sleep(2)

    # Navigate to the login page
    driver.get('https://seller-area.youcan.shop/login')
    time.sleep(5)

    # Find the email and password fields, and enter your login credentials
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys(credentials.email)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(credentials.password)
    password_input.send_keys(Keys.ENTER)

    time.sleep(10)

    return driver


def add_product(driver):
    # Navigate to the product creation page
    driver.get('https://seller-area.youcan.shop/admin/products/create?')

    # Read the Excel file
    df = pd.read_excel('products moha.xlsx', skiprows=39)

    # Iterate over the rows in the Excel file
    for i, row in df.iterrows():
        # Find the fields for the product information, and enter the information from your Excel sheet
        sku_input = driver.find_element(By.XPATH, "//input[@placeholder='SKU']")
        sku_input.send_keys(row.iloc[4])

        title_input = driver.find_element(By.XPATH, "//input[@placeholder='Name ( Ex: blue summer shirt.. )']")
        title_input.send_keys(row.iloc[5])

        # Rest of the code for entering product information

        # Save the product
        save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save")]')
        save_button.click()

        # Wait for the product to be saved
        time.sleep(7)

        # Navigate back to the product creation page for the next product
        driver.get('https://seller-area.youcan.shop/admin/products/create?')


def add_review(driver):
    # Navigate to the reviews page
    driver.get("https://seller-area.youcan.shop/admin/products/reviews")
    driver.set_window_size(1936, 1096)

    # Read data from Excel file
    df = pd.read_excel(r'C:\Users\pc\Desktop\Home\Work\Fiverr\Customers\Bilal Hagouch\Products\raddad\reviews\reviews.xlsx')

    # Iterate over rows in the Excel file
    for i, row in df.iterrows():
        name = row['Name']
        review = row['Review']

        # Click on "Add a review"
        driver.find_element(By.LINK_TEXT, "Add a review").click()

        # Enter data into the form
        driver.find_element(By.ID, "first-name").click()
        driver.find_element(By.ID, "first-name").send_keys(name)
        driver.find_element(By.CSS_SELECTOR, ".input-holder > input").click()
        driver.find_element(By.CSS_SELECTOR, ".input-holder > input").send_keys("a")
        driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) > .item-info").click()
        driver.find_element(By.CSS_SELECTOR, ".fr-element").click()
        element = driver.find_element(By.CSS_SELECTOR, ".fr-element")
        driver.execute_script(f"if(arguments[0].contentEditable === 'true') {{arguments[0].innerText = '<p>{review}</p>'}}", element)
        driver.find_element(By.CSS_SELECTOR, ".button").click()
        driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) label").click()


def main():
    driver = login()

    print("Menu:")
    print("1 - Add product")
    print("2 - Add review")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_product(driver)
    elif choice == "2":
        add_review(driver)
    else:
        print("Invalid choice")

    # Close the webdriver
    driver.quit()


if __name__ == "__main__":
    main()
