import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import credentials

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

time.sleep(3)

# Navigate to the product creation page
driver.get('https://seller-area.youcan.shop/admin/products/create?')

# Read the Excel file
df = pd.read_excel('products.xlsx')

# Iterate over the rows in the Excel file
for i, row in df.iterrows():
    # Find the fields for the product information, and enter the information from your Excel sheet
    sku_input = driver.find_element(By.XPATH, "//input[@placeholder='SKU']")
    sku_input.send_keys("TEST")

    title_input = driver.find_element(By.XPATH, "//input[@placeholder='Name ( Ex: blue summer shirt.. )']")
    title_input.send_keys("TEST")
    
    '''
    category_input = driver.find_element(By.ID, 'category')
    category_input.send_keys(row['Category'])
    
    compare_price_input = driver.find_element(By.ID, 'compare_price')
    compare_price_input.send_keys(row['Compare Price'])
    '''
    price_input = driver.find_element(By.XPATH, "//label[contains(text(), 'Price')]/following-sibling::input")
    price_input.send_keys(666)

    cost_price = float(666) - 100
    cost_price_input = driver.find_element(By.XPATH, "//label[contains(text(), 'Cost price')]/following-sibling::input")
    cost_price_input.send_keys(str(cost_price))

    # Save the product
    save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save")]')
    save_button.click()

    
    # Wait for the product to be saved
    time.sleep(5)

    # Navigate back to the product creation page for the next product
    driver.get('https://seller-area.youcan.shop/admin/products/create?')

# Close the webdriver
driver.quit()
