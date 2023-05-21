# gui.py

from tkinter import Tk, Label, Button, Entry
from product_management import add_product, add_review, new_product
from login import login

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
def add_product_button_click():
    product_name = product_entry.get()
    if product_name:
        driver = login()
        add_product(driver, product_name)
        driver.quit()

def add_review_button_click():
    product_name = product_entry.get()
    if product_name:
        driver = login()
        add_review(driver, product_name)
        driver.quit()

def create_product_button_click():
    client_name = client_entry.get()
    product_name = product_entry.get()
    if client_name and product_name:
        new_product(client_name, product_name)

add_product_button = Button(root, text="Add Product", command=add_product_button_click)
add_product_button.grid(row=2, column=0, padx=10, pady=10)
add_review_button = Button(root, text="Add Review", command=add_review_button_click)
add_review_button.grid(row=2, column=1, padx=10, pady=10)
create_product_button = Button(root, text="Create New Product", command=create_product_button_click)
create_product_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
