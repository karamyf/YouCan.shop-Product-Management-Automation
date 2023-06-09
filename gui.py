from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu
from product_management import add_product, add_review, new_product
from login import login
import os

# Change your workflow
workflow = "C:\\Users\\pc\\Desktop\\Home\\Work\\Fiverr\\Customers"

# Create the GUI
root = Tk()
root.title("YouCan Product Management")

# Styling
root.geometry("500x500")
root.configure(bg="#212121")

label_font = ("Arial", 12, "bold")
button_font = ("Arial", 10)
entry_font = ("Arial", 10)

# Labels
client_label = Label(root, text="Client Name:", font=label_font, bg="#212121", fg="#ffffff")
client_label.grid(row=0, column=0, padx=10, pady=10)
product_label = Label(root, text="Product Name:", font=label_font, bg="#212121", fg="#ffffff")
product_label.grid(row=1, column=0, padx=10, pady=10)

# Dropdown menu variables
selected_client = StringVar(root)
selected_product = StringVar(root)

# Dropdown menus
clients_menu = OptionMenu(root, selected_client, "")
clients_menu.config(font=entry_font, bg="#424242", fg="#ffffff")
clients_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")

products_menu = OptionMenu(root, selected_product, "")
products_menu.config(font=entry_font, bg="#424242", fg="#ffffff")
products_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Update products menu based on selected client
def update_products_menu(*args):
    client_name = selected_client.get()
    if client_name:
        products = os.listdir(f"{workflow}\\{client_name}\\Products")
        products_menu["menu"].delete(0, "end")  # Clear previous menu options
        for product in products:
            products_menu["menu"].add_command(label=product, command=lambda p=product: selected_product.set(p))

selected_client.trace("w", update_products_menu)  # Call update_products_menu when selected client changes

# Search function for clients and products
def search_entries():
    search_term = search_entry.get()
    if search_term:
        # Search for clients
        clients = os.listdir(workflow)
        filtered_clients = [client for client in clients if search_term.lower() in client.lower()]
        clients_menu["menu"].delete(0, "end")
        for client in filtered_clients:
            clients_menu["menu"].add_command(label=client, command=lambda c=client: selected_client.set(c))

        # Search for products
        client_name = selected_client.get()
        if client_name:
            products = os.listdir(f"{workflow}\\{client_name}\\Products")
            filtered_products = [product for product in products if search_term.lower() in product.lower()]
            products_menu["menu"].delete(0, "end")
            for product in filtered_products:
                products_menu["menu"].add_command(label=product, command=lambda p=product: selected_product.set(p))

# Search entry field
search_entry = Entry(root, font=entry_font)
search_entry.grid(row=2, column=0, padx=10, pady=10, sticky="w")
search_button = Button(root, text="Search", command=search_entries, font=button_font, bg="#757575", fg="#ffffff")
search_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Buttons
def add_product_button_click():
    client_name = selected_client.get()
    product_name = selected_product.get()
    if client_name and product_name:
        driver = login()
        add_product(driver, product_name)
        driver.quit()

def add_review_button_click():
    client_name = selected_client.get()
    product_name = selected_product.get()
    if client_name and product_name:
        driver = login()
        add_review(driver, product_name)
        driver.quit()

def create_product_button_click():
    client_name = selected_client.get()
    product_name = selected_product.get()
    if client_name and product_name:
        new_product(client_name, product_name)

add_product_button = Button(root, text="Add Product", command=add_product_button_click, font=button_font, bg="#1976D2", fg="#ffffff", bd=0, padx=10, pady=5, relief="solid", borderwidth=0, highlightthickness=0, highlightbackground="#212121", highlightcolor="#212121", activebackground="#1565C0", activeforeground="#ffffff")
add_product_button.grid(row=3, column=0, padx=10, pady=10)
add_review_button = Button(root, text="Add Review", command=add_review_button_click, font=button_font, bg="#1976D2", fg="#ffffff", bd=0, padx=10, pady=5, relief="solid", borderwidth=0, highlightthickness=0, highlightbackground="#212121", highlightcolor="#212121", activebackground="#1565C0", activeforeground="#ffffff")
add_review_button.grid(row=3, column=1, padx=10, pady=10)
create_product_button = Button(root, text="Create New Product", command=create_product_button_click, font=button_font, bg="#1976D2", fg="#ffffff", bd=0, padx=10, pady=5, relief="solid", borderwidth=0, highlightthickness=0, highlightbackground="#212121", highlightcolor="#212121", activebackground="#1565C0", activeforeground="#ffffff")
create_product_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()