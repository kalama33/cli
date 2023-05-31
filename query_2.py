"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock

# Get the user name
user_name = input("What is your user name? ")

# Greet the user
print(f"Hello, {user_name}!")

# Show the menu and ask to pick a choice
print("What would you like to do?")
print("1. List items by warehouse")
print("2. Search an item and place an order")
print("3. Quit")
choice = input("Type the number of the operation: ")

# If the user picks 1
if choice == "1":
    warehouses = set(item['warehouse'] for item in stock)
    for warehouse in warehouses:
        print(f"Items in warehouse {warehouse}:")
        for item in stock:
            if item['warehouse'] == warehouse:
                print("- " + item['category'])

# If the user picks 2
elif choice == "2":
    # Ask for item name
    item_name = input("What is the name of the item? ")
    
    # Search for the item in the warehouses
    total_amount = 0
    max_warehouse = None
    max_amount = 0
    
    for item in stock:
        if item['category'] == item_name:
            total_amount += 1
            if max_warehouse is None or item['warehouse'] == max_warehouse:
                max_warehouse = item['warehouse']
                max_amount += 1
            elif item['warehouse'] != max_warehouse and max_amount == 1:
                max_warehouse = 'Both warehouses'
                max_amount += 1
    
    # Print the total amount and location of the item
    print("Amount available:", total_amount)
    if total_amount > 0:
        print("Location:", end=" ")
        if max_warehouse == 'Both warehouses':
            print("Both warehouses")
        elif max_warehouse is not None:
            print(f"Warehouse {max_warehouse}")
    
        if max_warehouse == 'Both warehouses' and max_amount > 1:
            print("Maximum availability:", max_amount, "in", max_warehouse)
    
    else:
        print("Location: Not in stock")
    
    # Ask if the user wants to place an order
    order_choice = input("Would you like to order this item? (y/n) ")
    if order_choice.lower() == "y":
        # Ask for the desired amount
        desired_amount = int(input("How many would you like? "))
        
        if desired_amount <= total_amount:
            print(f"{desired_amount} {item_name} have been ordered.")
        else:
            print("*" * 50)
            print("There are not this many available. The maximum amount that can be ordered is", total_amount)
            max_order_choice = input("Would you like to order the maximum available? (y/n) ")
            if max_order_choice.lower() == "y":
                print(f"{total_amount} {item_name} have been ordered.")
            else:
                print("Order canceled.")
            print("*" * 50)

# If the user picks 3, do nothing

# If the user types anything different than 1, 2, or 3
else:
    print("*" * 50)
    print("Invalid operation.")
    print("*" * 50)

# Thank the user for the visit
print("\nThank you for your visit, " + user_name + "!")
