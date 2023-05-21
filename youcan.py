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

#login method
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

#add products from excel sheet
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

#add reviews from excel sheet
# Add reviews from an Excel sheet
def add_review(driver, product_name):
    driver.get("https://seller-area.youcan.shop/admin/products/reviews")
    driver.set_window_size(1936, 1096)

    df = pd.read_excel(f'C:\\Users\\pc\\Desktop\\Home\\Work\\Fiverr\\Customers\\Bilal Hagouch\\Products\\{product_name}\\reviews\\reviews.xlsx')

    # Iteration
    for i, row in df.iterrows():
        name = row['Name']
        review = row['Review']
        image_path = row['Picture Path']

        driver.find_element(By.LINK_TEXT, "Add a review").click()

        driver.find_element(By.ID, "first-name").click()
        driver.find_element(By.ID, "first-name").send_keys(name)

        search_input = driver.find_element(By.CSS_SELECTOR, ".input-holder > input")
        search_input.click()
        
        # Search product
        search_input.send_keys(product_name)

        # Wait for the matching product titles to appear
        time.sleep(1)

        # Click on the first matching product
        driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) > .item-info").click()

        driver.find_element(By.CSS_SELECTOR, ".fr-element").click()
        element = driver.find_element(By.CSS_SELECTOR, ".fr-element")
        driver.execute_script(f"if(arguments[0].contentEditable === 'true') {{arguments[0].innerText = '{review}'}}", element)

        try:
            # Upload image if the file path exists
            if os.path.exists(image_path):
                uploader_input = driver.find_element(By.ID, "review-images-uploader")
                uploader_input.send_keys(image_path)
        except FileNotFoundError:
            print(f"Image file not found for row {i + 1}. Skipping...")

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".button").click()
        driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) label").click()


# Create folders for a new product
def new_product(client_name, product_name):
    base_path = f"C:\\Users\\pc\\Desktop\\Home\\Work\\Fiverr\\Customers\\{client_name}\\Products\\{product_name}"
    
    # Create folders
    os.makedirs(os.path.join(base_path, "images", "variants"))
    os.makedirs(os.path.join(base_path, "reviews", "images"))
    os.makedirs(os.path.join(base_path, "gifs"))
    
    # Create reviews.xlsx file
    reviews_df = pd.DataFrame(columns=["Name", "Review", "Picture Path"])
    reviews_file_path = os.path.join(base_path, "reviews", "reviews.xlsx")
    reviews_df.to_excel(reviews_file_path, index=False)

    print(f"New product '{product_name}' for client '{client_name}' created successfully.")



def main():

    print("Menu:")
    print("1 - Add product")
    print("2 - Add review")
    print("3 - Create new product")
    choice = input("Enter your choice: ")

    if choice == "1":
        driver = login()
        add_product(driver)
    elif choice == "2":
        driver = login()
        product_name = input("Enter the product name: ")
        add_review(driver, product_name)
    elif choice == "3":
        client_name = input("Enter the client name: ")
        product_name = input("Enter the product name: ")
        new_product(client_name, product_name)
    
    else:
        print("Invalid choice")

    # Close the webdriver
    driver.quit()


if __name__ == "__main__":
    main()
