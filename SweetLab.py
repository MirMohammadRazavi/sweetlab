import os
from getpass import getpass
import json
import time
import sqlite3

# in the name of Allah :) .
# SweetLab project.

# Variable
data = []
role = None
while_checker = True
password = 1234
again_input = None
password_checker = True
login_input = None
customer_checker = None
admin = None
customer_menu = None
admin_checker = None
# clear = os.system("cls" if os.name == "nt" else "clear")
list_num = len(data)
y_n = None
# data
data = [
    "Chocolate Cake",
    "Vanilla Cake",
    "Strawberry Cake",
    "Red Velvet Cake",
    "Cheesecake",
    "Chocolate Brownie",
    "Carrot Cake",
    "Cinnamon Roll",
    "Chocolate Donut",
    "Vanilla Donut",
    "Blueberry Muffin",
    "Chocolate Chip Cookie",
    "Butter Croissant",
    "Apple Pie",
    "Lemon Tart",
    "Tiramisu",
    "Chocolate Eclair",
    "Strawberry Cupcake",
    "Pistachio Macaron",
    "Black Forest Cake",
]


# SQL

connection = sqlite3.connect("sweetlab.db")
#connection.close()
cursor = connection.cursor()

# functions
# create json
def create_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# save json
def save_data(data):
    with open("sweetlab_data.json", "w") as file:
        json.dump(data, file, indent=4)

#data = load_data()
# load data
def load_data():
    with open("sweetlab_data.json", "r") as file:

        return json.load(file)

data_json = load_data()


# clear terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def data_list():
    for index, item in enumerate(data, start=1):
        print(f"{index}.{item}")


if not os.path.exists("sweetlab_data.json"):
    create_json("sweetlab_data.json", data)
else:
    data = load_data()


def edit_product():

    search_product = input("Please enter the product name: ")
    loding()
    search_results = []

    for index, item in enumerate(data):
        if search_product.lower() in item.lower():
            search_results.append((index, item))

    if not search_results:
        loding()
        clear()
        print("No product found!")
        
        time.sleep(1)
        print("please try agian.")
        time.sleep(1)
        return


    print("\nSearch results:")

    for number, result in enumerate(search_results, start=1):
        print(f"{number}. {result[1]}")

    search_product_number = int(
        input("\nPlease choose the product number: ")
    )

    if search_product_number < 1 or search_product_number > len(search_results):
        print("Invalid product number!")
        return

    selected = search_results[search_product_number - 1]

    original_index = selected[0]
    selected_product = selected[1]
    time.sleep(2)
    print(f"\nSelected product: {selected_product}")
    time.sleep(0.5)
    new_product_name = input("Enter new product name: ")

    if new_product_name.strip() == "":
        print("Product name cannot be empty!")
        return

    data[original_index] = new_product_name

    save_data(data)
    loding()
    clear()
    print("\nProduct successfully updated!")
    time.sleep(1)



def delete_product():

    search_product = input("Search product: ").strip()

    if search_product == "":
        print("Search cannot be empty!")
        return

    search_results = []

    for index, item in enumerate(data):
        if search_product.lower() in item.lower():
            search_results.append((index, item))

    if not search_results:
        clear()
        print("No product found!")
        time.sleep(1)
        return

    print("\nSearch results:")

    for number, result in enumerate(search_results, start=1):
        print(f"{number}. {result[1]}")

    try:
        choice = int(input("\nChoose product number: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if choice < 1 or choice > len(search_results):
        print("Invalid product number!")
        return

    selected = search_results[choice - 1]

    original_index = selected[0]
    selected_product = selected[1]

    print(f"\nSelected product: {selected_product}")

    confirm = input(
        "Are you sure you want to delete this product? (y/n): "
    ).lower()

    if confirm == "y":

        data.pop(original_index)

        #time.sleep()
        save_data(data)
        loding()
        time.sleep(0.5)
        print("Product successfully deleted! ✅")
        time.sleep(0.5)
    elif confirm == "n":
        print("Delete cancelled.")

    else:
        print("Invalid input!")


def loding():
    for n in range(1, 3):
        print("please wait . ")
        time.sleep(0.5)
        clear()
        print("please wait . .")
        time.sleep(0.5)
        clear()
        print("please wait . . .")
        time.sleep(0.5)
        clear()


def add_product_while_yn():
    while_yn = True
    y_n = None
    while while_yn:
        y_n = input(" y == Go back , n == exit = ")
        if y_n == "y":
            add_product_while = True
            while_yn = False
        elif y_n == "n":
            while_yn = False
            add_product_while = False
        # while_checker = True
        elif y_n == "":
            print("Invalid choice! ")
            again_input = input("Again ? (n/y)= ")
        elif again_input == "y":
            while_yn = True
            clear()
        elif again_input == "n":
            break


def while_yn():
    while_yn = True
    while while_yn:
        y_n = input(" y == Go back , n == exit = ")
        if y_n == "y":
            admin_checker = True
            while_yn = False
        elif y_n == "n":
            while_yn = False
            admin_checker = False
        # while_checker = True
        elif y_n == "":
            print("Invalid choice! ")
            again_input = input("Again ? (n/y)= ")
        elif again_input == "y":
            while_yn = True
            clear()
        elif again_input == "n":
            break


def hello_word():
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to SweetLab.")
    # time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    # time.sleep(2)
    print("Hello, dear user.")
    # time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    # time.sleep(2)
    print("please wait for opening . . .")

    clear()
    loding()
    # time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")


def admin_panel():
    admin_checker = True
    while_checker = None
    add_product = None
    # while_yn = None
    add_product_while = None
    while admin_checker:
        while_checker = int(
            input("""

            please choose your : 
        
        ┌──────────────────────────────┐
        │         ADMIN PANEL          │
        ├──────────────────────────────┤
        │ 1. View Products             │
        │ 2. Add Product               │
        │ 3. Edit Product              │
        │ 4. Delete Product            │
        │ 5. View Orders               │
        │ 6. Manage Products           │
        │ 7. Exit                      │
        └──────────────────────────────┘

            Enter your choice: """)
        )
        # 1.View Products
        if while_checker == 1:
            data_list()
            while_yn()
        # 2. add Products
        elif while_checker == 2:
            clear()
            add_product_while = True
            while add_product_while:
                add_product = None
                add_product = input("Enter product name: ")

                if add_product.strip() == "":
                    print("You entered just the name!")
                    continue

                elif add_product.isdigit():
                    print("Product name cannot be a number!")

                elif any(char.isdigit() for char in add_product):
                    print("Product name cannot contain numbers!")

                else:
                    # print("please wait . . .")
                    clear()
                    loding()
                    data.append(add_product)
                    time.sleep(2)
                    save_data(data)
                    print("succsefuly")
                    time.sleep(1)

                y_n = None
                y_n = input("Add another product? y/n = ")
                if y_n == "y":
                    continue
                elif y_n == "n":
                    break
                else:
                    print("what's ??")
                    break
        # 3. Edit Products
        elif while_checker == 3:
            edit_product()
            
        elif while_checker == 4 :
            delete_product()


                


def customer_panel():
    customer_checker = True
    while customer_checker:
        clear()

        customer_menu = input("""

    please choose your : 

┌───────────────────────────────┐
│        CUSTOMER MENU :        │
├───────────────────────────────┤
│ 1.view menu                   │
│ 2.my order                    │
│ 3.go to Menu                  │
│ 4.Exit                        │
└───────────────────────────────┘

    Enter your choice: """)
        clear()

        if customer_menu == "1":
            clear()
            data_list()
            while_yn()

            y_n = input(" y == Go back , n == exit = ")
            if y_n == "y":
                customer_checker = True
            elif y_n == "n":
                customer_checker = False
                while_checker = True
            else:
                print("Invalid choice! ")
                again_input = input("Again ? (n/y)= ")
                if again_input == "y":
                    while_checker = True
                    clear()
                elif again_input == "n":
                    break

            if y_n == "y":
                customer_checker = True
            elif y_n == "n":
                break

        elif customer_menu == "2":
            clear()
            print("Updating . . .")
            y_n = input(" y == Go back , n == exit = ")

            if y_n == "y":
                customer_checker = True
            elif y_n == "n":
                customer_checker = False
                while_checker = True
            else:
                print("Invalid choice! ")
                again_input = input("Again ? (n/y)= ")
                if again_input == "y":
                    while_checker = True
                    clear()
                elif again_input == "n":
                    break

        elif customer_menu == "3":
            Menu()

        elif customer_menu == "4":
            break

        else:
            print("Invalid choice! ")
    # for view menu


# start the app
# create data file
# create_json("data.json")


def Menu():
    while_checker = True
    while while_checker:
        clear()
        role = input("""
    please choose your : 

┌───────────────────────────────┐
│            MENU :             │
├───────────────────────────────┤
│ 1.customer                    │
│ 2.admin                       │
│ 3.Exit                        │
└───────────────────────────────┘

    Enter your choice: """)

        if role == "1":
            print("Welcome, Customer!")
            customer_panel()
            while_checker = False
            break
        elif role == "2":
            admin = True
            while admin:
                password_input = int(getpass("Enter admin password: "))
                if password_input == password:
                    print("Welcome, Admin!  ")
                    time.sleep(1)
                    admin = False
                    admin_panel()
                    #break
                    # while_checker = False
                    #admin_panel()
                elif password_input != 1234 :
                    print("Wrong password!  ")
                    continue
                        
                        
                     
                

        else:
            ("Invalid input")
            while_checker = False
            print("Please run the program again.")

#create_json("sweetlab_data.json",data)
#data = load_data()
hello_word()
Menu()
save_data(data)
