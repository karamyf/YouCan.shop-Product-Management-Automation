import os
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from tkinter import Tk, Label, Button, Entry, StringVar


import credentials

# Login method
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

# Add products from an Excel sheet
def add_product(driver, product_name):
    # Navigate to the product creation page
    driver.get('https://seller-area.youcan.shop/admin/products/create?')

    # Read the Excel file
    df = pd.read_excel(f'C:\\Users\\pc\\Desktop\\Home\\Work\\Fiverr\\Customers\\Bilal Hagouch\\Products\\{product_name}\\reviews\\reviews.xlsx')

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

# Main menu

'''
def main():
    driver = None

    try:
        

        print("Menu:")
        print("1 - Add product")
        print("2 - Add review")
        print("3 - Create new product")
        choice = input("Enter your choice: ")

        if choice == "1":
            driver = login()
            product_name = input("Enter the product name: ")
            add_product(driver, product_name)
        elif choice == "2":
            product_name = input("Enter the product name: ")
            driver = login()
            add_review(driver, product_name)
        elif choice == "3":
            client_name = input("Enter the client name: ")
            product_name = input("Enter the product name: ")
            new_product(client_name, product_name)
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if driver is not None:
            # Close the webdriver
            driver.quit()


if __name__ == "__main__":
    main()
'''

# Function to handle the button click event for adding a product
def add_product_button_click():
    product_name = product_entry.get()
    if product_name:
        driver = login()
        add_product(driver, product_name)
        driver.quit()

# Function to handle the button click event for adding a review
def add_review_button_click():
    product_name = product_entry.get()
    if product_name:
        driver = login()
        add_review(driver, product_name)
        driver.quit()

# Function to handle the button click event for creating a new product
def create_product_button_click():
    client_name = client_entry.get()
    product_name = product_entry.get()
    if client_name and product_name:
        new_product(client_name, product_name)

# Create the GUI
root = Tk()
root.title("YouCan.shop Product Management")

# Labels
client_label = Label(root, text="Client Name:")
client_label.grid(row=0, column=0, padx=10, pady=10)
product_label = Label(root, text="Product Name:")
product_label.grid(row=1, column=0, padx=10, pady=10)

# Entry fields
client_entry = Entry(root)
client_entry.grid(row=0, column=1, padx=10, pady=10)
product_entry = Entry(root)
product_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons
add_product_button = Button(root, text="Add Product", command=add_product_button_click)
add_product_button.grid(row=2, column=0, padx=10, pady=10)
add_review_button = Button(root, text="Add Review", command=add_review_button_click)
add_review_button.grid(row=2, column=1, padx=10, pady=10)
create_product_button = Button(root, text="Create New Product", command=create_product_button_click)
create_product_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()