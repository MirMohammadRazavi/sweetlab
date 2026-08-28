import os
from getpass import getpass
import json
import time
from datetime import datetime

# in the name of Allah :) .
# SweetLab project.

# ===== Variables =====
password = 1234
cart = []
orders = []
order_id_counter = 1
exit_program = False

# default data (only used on first run to seed the file)
default_data = [
    {"name": "Chocolate Cake", "price": 15.5, "stock": 10},
    {"name": "Vanilla Cake", "price": 12.0, "stock": 15},
    {"name": "Strawberry Cake", "price": 14.0, "stock": 8},
    {"name": "Red Velvet Cake", "price": 16.5, "stock": 7},
    {"name": "Cheesecake", "price": 10.0, "stock": 12},
    {"name": "Chocolate Brownie", "price": 5.5, "stock": 20},
    {"name": "Carrot Cake", "price": 13.0, "stock": 6},
    {"name": "Cinnamon Roll", "price": 4.5, "stock": 18},
    {"name": "Chocolate Donut", "price": 3.0, "stock": 25},
    {"name": "Vanilla Donut", "price": 3.0, "stock": 25},
    {"name": "Blueberry Muffin", "price": 4.0, "stock": 15},
    {"name": "Chocolate Chip Cookie", "price": 2.5, "stock": 30},
    {"name": "Butter Croissant", "price": 3.5, "stock": 14},
    {"name": "Apple Pie", "price": 9.0, "stock": 9},
    {"name": "Lemon Tart", "price": 6.5, "stock": 11},
    {"name": "Tiramisu", "price": 8.5, "stock": 7},
    {"name": "Chocolate Eclair", "price": 4.0, "stock": 16},
    {"name": "Strawberry Cupcake", "price": 3.5, "stock": 22},
    {"name": "Pistachio Macaron", "price": 5.0, "stock": 13},
    {"name": "Black Forest Cake", "price": 17.0, "stock": 5},
]


# ===== File Functions =====
# Single JSON file holds both products and orders:
# {
#     "products": [...],
#     "orders": [...]
# }

DATA_FILE = "sweetlab_data.json"


def save_all():
    # save both products and orders into one file
    all_data = {
        "products": data,
        "orders": orders
    }
    with open(DATA_FILE, "w") as file:
        json.dump(all_data, file, indent=4)


def load_all():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(dummy=None):
    # dummy param kept for backward compat with old save_data(data) calls
    save_all()


def save_orders(dummy=None):
    # dummy param kept for backward compat with old save_orders(orders) calls
    save_all()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ===== Init single data file =====
if not os.path.exists(DATA_FILE):
    # first run: create file with default products + empty orders
    initial = {
        "products": default_data,
        "orders": []
    }
    with open(DATA_FILE, "w") as file:
        json.dump(initial, file, indent=4)

_all = load_all()
data = _all["products"]
orders = _all["orders"]
if orders:
    order_id_counter = orders[-1]["order_id"] + 1


# ===== Helper Functions =====

def data_list():
    for index, item in enumerate(data, start=1):
        print(f"{index}. {item['name']}  -  ${item['price']}  (stock: {item['stock']})")


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


# returns True (go back) or False (exit program)
def while_yn():
    while_yn_var = True
    while while_yn_var:
        y_n = input(" y == Go back , n == exit = ")
        if y_n == "y":
            return True
        elif y_n == "n":
            return False
        else:
            print("Invalid choice! ")
            again_input = input("Again ? (n/y)= ")
            if again_input == "y":
                clear()
            elif again_input == "n":
                return False


def hello_word():
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to SweetLab.")
    os.system("cls" if os.name == "nt" else "clear")
    print("Hello, dear user.")
    os.system("cls" if os.name == "nt" else "clear")
    print("please wait for opening . . .")
    clear()
    loding()
    os.system("cls" if os.name == "nt" else "clear")


# ===== Search Function =====

def search_products():
    search_product = input("Please enter the product name: ").strip()

    if search_product == "":
        print("Search cannot be empty!")
        time.sleep(1)
        return None

    search_results = []

    for index, item in enumerate(data):
        if search_product.lower() in item["name"].lower():
            search_results.append((index, item))

    if not search_results:
        print("No product found!")
        time.sleep(1)
        return None

    print("\nSearch results:")
    for number, result in enumerate(search_results, start=1):
        print(f"{number}. {result[1]['name']}  -  ${result[1]['price']}  (stock: {result[1]['stock']})")

    return search_results


# ===== Product Management =====

def edit_product():
    search_product = input("Please enter the product name: ")
    loding()
    search_results = []

    for index, item in enumerate(data):
        if search_product.lower() in item["name"].lower():
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
        print(f"{number}. {result[1]['name']}  -  ${result[1]['price']}  (stock: {result[1]['stock']})")

    try:
        search_product_number = int(
            input("\nPlease choose the product number: ")
        )
    except ValueError:
        print("Please enter a valid number!")
        time.sleep(1)
        return

    if search_product_number < 1 or search_product_number > len(search_results):
        print("Invalid product number!")
        time.sleep(1)
        return

    selected = search_results[search_product_number - 1]

    original_index = selected[0]
    selected_product = selected[1]
    time.sleep(1)
    print(f"\nSelected product: {selected_product['name']}")
    time.sleep(0.5)

    print("\nWhat do you want to edit?")
    print("1. Name")
    print("2. Price")
    print("3. Stock")
    print("4. All")

    try:
        edit_choice = int(input("\nChoose: "))
    except ValueError:
        print("Please enter a valid number!")
        time.sleep(1)
        return

    new_name = selected_product["name"]
    new_price = selected_product["price"]
    new_stock = selected_product["stock"]

    if edit_choice == 1 or edit_choice == 4:
        new_name = input(f"Enter new name (current: {selected_product['name']}): ")
        if new_name.strip() == "":
            print("Name cannot be empty!")
            time.sleep(1)
            return
        if any(char.isdigit() for char in new_name):
            print("Name cannot contain numbers!")
            time.sleep(1)
            return

    if edit_choice == 2 or edit_choice == 4:
        try:
            new_price = float(input(f"Enter new price (current: ${selected_product['price']}): "))
            if new_price < 0:
                print("Price cannot be negative!")
                time.sleep(1)
                return
        except ValueError:
            print("Please enter a valid number!")
            time.sleep(1)
            return

    if edit_choice == 3 or edit_choice == 4:
        try:
            new_stock = int(input(f"Enter new stock (current: {selected_product['stock']}): "))
            if new_stock < 0:
                print("Stock cannot be negative!")
                time.sleep(1)
                return
        except ValueError:
            print("Please enter a valid number!")
            time.sleep(1)
            return

    if edit_choice not in [1, 2, 3, 4]:
        print("Invalid choice!")
        time.sleep(1)
        return

    data[original_index]["name"] = new_name
    data[original_index]["price"] = new_price
    data[original_index]["stock"] = new_stock

    save_data(data)
    loding()
    clear()
    print("\nProduct successfully updated!")
    time.sleep(1)


def delete_product():
    search_product = input("Search product: ").strip()

    if search_product == "":
        print("Search cannot be empty!")
        time.sleep(1)
        clear()
        return

    search_results = []

    for index, item in enumerate(data):
        if search_product.lower() in item["name"].lower():
            search_results.append((index, item))

    if not search_results:
        clear()
        print("No product found!")
        time.sleep(1)
        return

    print("\nSearch results:")

    for number, result in enumerate(search_results, start=1):
        print(f"{number}. {result[1]['name']}  -  ${result[1]['price']}  (stock: {result[1]['stock']})")

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

    print(f"\nSelected product: {selected_product['name']}")

    confirm = input(
        "Are you sure you want to delete this product? (y/n): "
    ).lower()

    if confirm == "y":
        data.pop(original_index)
        save_data(data)
        loding()
        clear()
        print("Product successfully deleted!")
        time.sleep(1)
    elif confirm == "n":
        print("Delete cancelled.")
        time.sleep(1)
    else:
        print("Invalid input!")
        time.sleep(1)


# ===== Cart Functions =====

def add_to_cart():
    if not data:
        print("No products available!")
        time.sleep(1)
        return

    data_list()
    try:
        choice = int(input("\nChoose product number to add to cart: "))
    except ValueError:
        print("Please enter a valid number!")
        time.sleep(1)
        return

    if choice < 1 or choice > len(data):
        print("Invalid product number!")
        time.sleep(1)
        return

    if data[choice - 1]["stock"] <= 0:
        print(f"Sorry, {data[choice - 1]['name']} is out of stock!")
        time.sleep(1)
        return

    cart.append(data[choice - 1]["name"])
    data[choice - 1]["stock"] = data[choice - 1]["stock"] - 1
    save_data(data)
    print(f"\n{data[choice - 1]['name']} added to cart!")
    time.sleep(1)


def view_cart():
    if not cart:
        print("Your cart is empty!")
        time.sleep(1)
        return False  # empty cart - caller should not pause

    print("\nYour Cart:")
    for index, item in enumerate(cart, start=1):
        print(f"{index}. {item}")
    return True


def remove_from_cart():
    if not cart:
        print("Your cart is empty!")
        time.sleep(1)
        return

    view_cart()
    try:
        choice = int(input("\nChoose product number to remove from cart: "))
    except ValueError:
        print("Please enter a valid number!")
        time.sleep(1)
        return

    if choice < 1 or choice > len(cart):
        print("Invalid product number!")
        time.sleep(1)
        return

    removed = cart.pop(choice - 1)
    for product in data:
        if product["name"] == removed:
            product["stock"] = product["stock"] + 1
            break
    save_data(data)
    print(f"\n{removed} removed from cart!")
    time.sleep(1)


def clear_cart():
    global cart
    if not cart:
        print("Your cart is already empty!")
        time.sleep(1)
        return

    for item in cart:
        for product in data:
            if product["name"] == item:
                product["stock"] = product["stock"] + 1
                break
    cart = []
    save_data(data)
    print("Cart cleared!")
    time.sleep(1)


def place_order():
    global order_id_counter, cart

    if not cart:
        print("Your cart is empty! Add some products first.")
        time.sleep(1)
        return

    print("\nPlacing your order...")
    loding()

    order = {
        "order_id": order_id_counter,
        "products": cart.copy(),
        "status": "Pending",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    orders.append(order)
    order_id_counter = order_id_counter + 1

    save_orders(orders)

    cart = []

    print("Order successfully placed!")
    print(f"\nOrder ID: {order['order_id']}")
    print("Products:")
    for p in order["products"]:
        print(f"- {p}")
    print("Status: Pending")
    print(f"Date: {order['date']}")
    time.sleep(2)


# ===== Admin Order Functions =====

def admin_search_product():
    results = search_products()
    if results:
        time.sleep(2)


def view_orders():
    if not orders:
        print("No orders yet!")
        time.sleep(1)
        return

    print("\n=== All Orders ===\n")
    for order in orders:
        print(f"Order ID: {order['order_id']}")
        print("Products:")
        for p in order["products"]:
            print(f"  - {p}")
        print(f"Status: {order['status']}")
        if "date" in order:
            print(f"Date: {order['date']}")
        print("-" * 30)

    input("\nPress Enter to continue...")


def manage_orders():
    if not orders:
        print("No orders to manage!")
        time.sleep(1)
        return

    # show orders first without the pause
    print("\n=== All Orders ===\n")
    for order in orders:
        print(f"Order ID: {order['order_id']}")
        print("Products:")
        for p in order["products"]:
            print(f"  - {p}")
        print(f"Status: {order['status']}")
        if "date" in order:
            print(f"Date: {order['date']}")
        print("-" * 30)

    try:
        order_id = int(input("\nEnter Order ID to manage: "))
    except ValueError:
        print("Please enter a valid number!")
        time.sleep(1)
        return

    found_order = None
    for order in orders:
        if order["order_id"] == order_id:
            found_order = order
            break

    if not found_order:
        print("Order not found!")
        time.sleep(1)
        return

    print(f"\nOrder ID: {found_order['order_id']}")
    print(f"Current Status: {found_order['status']}")
    print("\nAvailable statuses:")
    print("1. Pending")
    print("2. Preparing")
    print("3. Completed")
    print("4. Cancelled")

    try:
        status_choice = int(input("\nChoose new status: "))
    except ValueError:
        print("Please enter a valid number!")
        time.sleep(1)
        return

    statuses = {
        1: "Pending",
        2: "Preparing",
        3: "Completed",
        4: "Cancelled"
    }

    if status_choice not in statuses:
        print("Invalid choice!")
        time.sleep(1)
        return

    found_order["status"] = statuses[status_choice]
    save_orders(orders)
    loding()
    print(f"\nOrder {found_order['order_id']} status updated to: {found_order['status']}")
    time.sleep(1)


def statistics():
    total_products = len(data)
    total_orders = len(orders)
    pending_orders = 0
    completed_orders = 0
    preparing_orders = 0
    cancelled_orders = 0

    for order in orders:
        if order["status"] == "Pending":
            pending_orders = pending_orders + 1
        elif order["status"] == "Completed":
            completed_orders = completed_orders + 1
        elif order["status"] == "Preparing":
            preparing_orders = preparing_orders + 1
        elif order["status"] == "Cancelled":
            cancelled_orders = cancelled_orders + 1

    total_inventory_value = 0
    for product in data:
        total_inventory_value = total_inventory_value + (product["price"] * product["stock"])

    print("\n=== SweetLab Statistics ===\n")
    print(f"Total Products: {total_products}")
    print(f"Total Orders: {total_orders}")
    print(f"Pending Orders: {pending_orders}")
    print(f"Preparing Orders: {preparing_orders}")
    print(f"Completed Orders: {completed_orders}")
    print(f"Cancelled Orders: {cancelled_orders}")
    print(f"Total Inventory Value: ${total_inventory_value:.2f}")

    if orders:
        product_count = {}
        for order in orders:
            for product in order["products"]:
                if product in product_count:
                    product_count[product] = product_count[product] + 1
                else:
                    product_count[product] = 1

        if product_count:
            max_count = 0
            most_ordered = None
            for product, count in product_count.items():
                if count > max_count:
                    max_count = count
                    most_ordered = product
            print(f"Most Ordered Product: {most_ordered} ({max_count} times)")

    input("\nPress Enter to continue...")


# ===== Admin Panel =====

def admin_panel():
    global exit_program
    admin_checker = True
    while admin_checker:
        clear()
        try:
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
        │ 5. Search Product            │
        │ 6. View Orders               │
        │ 7. Manage Orders             │
        │ 8. Statistics                │
        │ 9. Go Back                   │
        │ 10. Exit                     │
        └──────────────────────────────┘

            Enter your choice: """)
            )
        except ValueError:
            print("Please enter a valid number!")
            time.sleep(1)
            continue

        # 1. View Products
        if while_checker == 1:
            clear()
            data_list()
            go_back = while_yn()
            if not go_back:
                exit_program = True
                admin_checker = False

        # 2. Add Product
        elif while_checker == 2:
            clear()
            add_product_while = True
            while add_product_while:
                add_product = input("Enter product name: ")

                if add_product.strip() == "":
                    print("You entered just the name!")
                    continue

                elif add_product.isdigit():
                    print("Product name cannot be a number!")
                    continue

                elif any(char.isdigit() for char in add_product):
                    print("Product name cannot contain numbers!")
                    continue

                else:
                    try:
                        price = float(input("Enter product price: "))
                        if price < 0:
                            print("Price cannot be negative!")
                            continue
                    except ValueError:
                        print("Please enter a valid number!")
                        continue

                    try:
                        stock = int(input("Enter product stock: "))
                        if stock < 0:
                            print("Stock cannot be negative!")
                            continue
                    except ValueError:
                        print("Please enter a valid number!")
                        continue

                    clear()
                    loding()
                    data.append({
                        "name": add_product,
                        "price": price,
                        "stock": stock
                    })
                    time.sleep(1)
                    save_data(data)
                    print("succsefuly")
                    time.sleep(1)

                # loop until valid y/n
                y_n_valid = False
                while not y_n_valid:
                    y_n = input("Add another product? y/n = ")
                    if y_n == "y":
                        y_n_valid = True
                    elif y_n == "n":
                        y_n_valid = True
                        add_product_while = False
                    else:
                        print("what's ??")

        # 3. Edit Product
        elif while_checker == 3:
            clear()
            edit_product()

        # 4. Delete Product
        elif while_checker == 4:
            clear()
            delete_product()

        # 5. Search Product
        elif while_checker == 5:
            clear()
            admin_search_product()

        # 6. View Orders
        elif while_checker == 6:
            clear()
            view_orders()

        # 7. Manage Orders
        elif while_checker == 7:
            clear()
            manage_orders()

        # 8. Statistics
        elif while_checker == 8:
            clear()
            statistics()

        # 9. Go Back
        elif while_checker == 9:
            print("Going back to main menu...")
            time.sleep(1)
            admin_checker = False

        # 10. Exit
        elif while_checker == 10:
            print("Goodbye!")
            time.sleep(1)
            exit_program = True
            admin_checker = False

        else:
            print("Invalid choice!")
            time.sleep(1)


# ===== Customer Panel =====

def customer_panel():
    global exit_program
    customer_checker = True
    while customer_checker:
        clear()

        customer_menu = input("""

    please choose your : 

┌───────────────────────────────┐
│        CUSTOMER MENU :        │
├───────────────────────────────┤
│ 1. View Products              │
│ 2. Search Product             │
│ 3. Add To Cart                │
│ 4. View Cart                  │
│ 5. Remove From Cart           │
│ 6. Clear Cart                 │
│ 7. Place Order                │
│ 8. Go Back                    │
│ 9. Exit                       │
└───────────────────────────────┘

    Enter your choice: """)
        clear()

        if customer_menu == "1":
            data_list()
            go_back = while_yn()
            if not go_back:
                exit_program = True
                customer_checker = False

        elif customer_menu == "2":
            search_products()
            time.sleep(2)

        elif customer_menu == "3":
            add_to_cart()

        elif customer_menu == "4":
            # only pause if cart was not empty
            has_items = view_cart()
            if has_items:
                input("\nPress Enter to continue...")

        elif customer_menu == "5":
            remove_from_cart()

        elif customer_menu == "6":
            clear_cart()

        elif customer_menu == "7":
            place_order()

        elif customer_menu == "8":
            # Go Back = return to main menu
            print("Going back to main menu...")
            time.sleep(1)
            customer_checker = False

        elif customer_menu == "9":
            # Exit = close program
            print("Goodbye!")
            time.sleep(1)
            exit_program = True
            customer_checker = False

        else:
            print("Invalid choice! ")
            time.sleep(1)


# ===== Main Menu =====

def Menu():
    global exit_program
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
            time.sleep(1)
            customer_panel()
            # check exit_program flag, don't force exit
            if exit_program:
                while_checker = False

        elif role == "2":
            admin = True
            while admin:
                # allow cancel with 'q'
                password_str = getpass("Enter admin password (or 'q' to cancel): ")
                if password_str == "q":
                    print("Cancelled.")
                    time.sleep(1)
                    admin = False
                    continue
                try:
                    password_input = int(password_str)
                except ValueError:
                    print("Please enter a valid number!")
                    time.sleep(1)
                    continue
                if password_input == password:
                    print("Welcome, Admin!  ")
                    time.sleep(1)
                    admin = False
                    admin_panel()
                    if exit_program:
                        while_checker = False
                        admin = False
                else:
                    print("Wrong password!  ")
                    time.sleep(1)
                    clear()

        elif role == "3":
            print("Goodbye!")
            time.sleep(1)
            while_checker = False

        else:
            print("Invalid input")
            time.sleep(1)


# ===== Start =====
if __name__ == "__main__":
    try:
        hello_word()
        Menu()
        save_data(data)
    except KeyboardInterrupt:
        # graceful exit on Ctrl+C
        print("\n\nGoodbye! (interrupted)")
        save_data(data)
