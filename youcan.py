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

# Navigate to the product creation page
driver.get('https://seller-area.youcan.shop/admin/products/create?')

# Read the Excel file
df = pd.read_excel('products.xlsx', skiprows=3)

# Iterate over the rows in the Excel file
for i, row in df.iterrows():
   
    # Find the fields for the product information, and enter the information from your Excel sheet
    sku_input = driver.find_element(By.XPATH, "//input[@placeholder='SKU']")
    sku_input.send_keys(row.iloc[4])

    title_input = driver.find_element(By.XPATH, "//input[@placeholder='Name ( Ex: blue summer shirt.. )']")
    title_input.send_keys(row.iloc[5])
    
    meta_title_input = driver.find_element(By.XPATH, "//label[contains(text(), 'Meta title')]/following-sibling::input")
    meta_title_input.send_keys(row.iloc[5] + " Bilal Electro")
    
    meta_description_input = driver.find_element(By.XPATH, "//label[contains(text(), 'Meta description')]/following-sibling::textarea")
    meta_description_input.send_keys(row.iloc[5] + " Electro Bilal")
    '''
    category_input = driver.find_element(By.ID, 'category')
    category_input.send_keys(row['Category'])
    '''
    
    price_input = driver.find_element(By.XPATH, "//label[contains(text(), 'Price')]/following-sibling::input")
    price_input.send_keys(row.iloc[7])
    
    compare_price_input = driver.find_element(By.XPATH, "//label[contains(text(), 'Compare at price')]/following-sibling::input")
    compare_price_input.send_keys(row.iloc[6])
    
    cost_price_input = driver.find_element(By.XPATH, "//label[contains(text(), 'Cost price')]/following-sibling::input")
    cost_price_input.send_keys(float(row.iloc[7]) - 100)
    
    description_input = driver.find_element(By.CLASS_NAME, "fr-element")
    description_input.send_keys(row.iloc[9])


    # Locate the input element for the file upload
    image_input = driver.find_element(By.XPATH, '//input[@id="product-images-uploader"]')
    image_input.send_keys(row.iloc[10])
    
   
   
    #category section

    # find the input field and enter text from excel
    category_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Start typing to search for categories']")))
    category_input.send_keys(row.iloc[0]) # assuming the text is in the third column (index 2)

    time.sleep(2)

    # show the items element
    driver.execute_script("document.querySelector('div.items').style.display = 'flex';")

    # wait for the item to appear and click on it
    wait = WebDriverWait(driver, 10)
    item_text = row.iloc[0]
    item_xpath = f"//div[@class='item-info' and text()='{item_text}']"
    item = wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
    time.sleep(1)
    item.click()
    time.sleep(1)

    # Save the product
    save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save")]')
    save_button.click()

    
    # Wait for the product to be saved
    time.sleep(7)

    # Navigate back to the product creation page for the next product
    driver.get('https://seller-area.youcan.shop/admin/products/create?')

# Close the webdriver
driver.quit()
