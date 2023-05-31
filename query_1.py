"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock
                
# get user name
user_name = input("What is your user name? ")

# greet the user
print(f"Hello, {user_name}!")

# show menu
print("What would you like to do?")
print("1. List items by warehouse")
print("2. Search an item and place an order")
print("3. Quit")
choice = input("Type the number of the operation: ")

# if pick 1
if choice == "1":
    warehouse_1_categories = [item['category'] for item in stock if item['warehouse'] == 1]
    warehouse_2_categories = [item['category'] for item in stock if item['warehouse'] == 2]

# Imprimir las listas resultantes
    print("Categories in Warehouse 1:", warehouse_1_categories)
    print("Categories in Warehouse 2:", warehouse_2_categories)
                
# choice = input("Would you like to search an item and place an order?")
                
    # if  pick 2
elif choice == "2":
    # ask for item name
    item_name = input("What is the name of the item? ")
    
    # seaching items 
    total_amount = 0     # intitializing variables to keep track of the amount of searched items
    max_amount = 0       # max quantity found in any warehouse
    max_warehouse = None # to store warehouse with maximum quantity of items. 

    for item in stock:
        if item["category"] == item_name: # if item match input....
            total_amount +=1              # plus one
            # warehouse with maximum quantity?
            # ???
            if max_warehouse is None or item['warehouse'] == max_warehouse:
                max_warehouse = item['warehouse']
                max_amount += 1
            elif item['warehouse'] != max_warehouse and max_amount == 1:
                max_warehouse = 'Both warehouses'
                max_amount += 1
    
    # print the total amount and location of the item
    print("Amount available:", total_amount)
    if total_amount > 0:                      # available article
        print("Location:", end=" ")           # where?
        if max_warehouse == 'Both warehouses':
            print("Both warehouses")
        elif max_warehouse is not None:
            print(f"Warehouse {max_warehouse}")
    
        if max_warehouse == 'Both warehouses' and max_amount > 1:
            print("Maximum availability:", max_amount, "in", max_warehouse)
    
    else:
        print("Location: Not in stock")
        
        
    # ask if  user wants to place an order
    order_choice = input("Would you like to order this item? (y/n) ")
    if order_choice.lower() == "y": #casesensitive, lowercase
        # ask for the desired amount
        desired_amount = int(input("How many would you like? "))
        
        if desired_amount <= total_amount:
            print(f"{desired_amount} {item_name} have been ordered.")
        else:
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