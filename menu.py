# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Initialize the order list:
order_list = []

# Launch the store and present a greeting to the customer:
print("Welcome to Matthew's Food Truck. Food is Love!")

# Customers may want to order multiple items, so let's create a continuous loop:
place_order = True
while place_order:
    # Display menu categories:
    print("\nFrom which menu would you like to order? ")

    # Create a variable for the menu item number:
    i = 1

    # Dictionary to store the menu for later retrieval"
    menu_items = {}

    # Print the options to choose from menu headings (all the first-level dictionary items in menu):
    for key in menu.keys():
        print(f"{i}: {key}")

    # Store the menu category associated with its menu item number
        menu_items[i] = key
        
    # Add 1 to the menu item number
        i += 1

    # Get the customer's menu category selection:
    menu_selection = input("Please select a menu category by number: ")
    
    # Check if the input is an integer and within the menu category range
    if menu_selection.isdigit():
        menu_selection = int(menu_selection)
        if menu_selection in menu_items:
            menu_category_name = menu_items[menu_selection]
            print(f"\nYou selected {menu_category_name}.\n")

            # Display items in the selected menu category
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):  # Handle nested dictionaries
                    for sub_key, sub_value in value.items():
                        num_item_spaces = 24 - len(key + " - " + sub_key)
                        print(f"{i}      | {key} - {sub_key}{' ' * num_item_spaces} | ${sub_value}")
                        menu_items[i] = {
                            "Item name": f"{key} - {sub_key}",
                            "Price": sub_value
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    print(f"{i}      | {key}{' ' * num_item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # Get customer's choice of item from the category
            item_selection = input("\nPlease select an item by number: ")
            if item_selection.isdigit():
                item_selection = int(item_selection)
                if item_selection in menu_items:
                    item = menu_items[item_selection]
                    quantity = input("Enter quantity: ")

                    # Validate and set quantity
                    quantity = int(quantity) if quantity.isdigit() else 1

                    # Add item to order
                    order_list.append({
                        "Item name": item["Item name"],
                        "Price": item["Price"],
                        "Quantity": quantity
                    })
                    print(f"Added {quantity} x {item['Item name']} to your order.")

                else:
                    print("Invalid item selection. Please enter a valid item number.")
            else:
                print("Invalid input. Please enter a valid item number.")

        else:
            print("Invalid menu selection. Please choose a valid category number.")
    else:
        print("Invalid input. Please enter a number for the menu selection.")

    # Ask if they want to continue ordering
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").strip().lower()
    if keep_ordering == 'n':
        place_order = False

# Display the final order list
print("\nThank you for your order! Here is a summary of your items we are preparing for you:")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
for item in order_list:
    print(f"{item['Item name']:<25} | ${item['Price']:<5} | {item['Quantity']}")

# Calculate total cost
total_cost = sum(item['Price'] * item['Quantity'] for item in order_list)
print(f"\nTotal cost: ${total_cost:.2f}")