import sys
fruits_shop_inventory ={"apple":{"quantity" : 10,
                                    "price": 100,
                                    "low-stock value":5},
                        "banana":{"quantity" : 20,
                                    "price": 30,
                                    "low-stock value":10}}

def update_inventory():
    item_name = input('Please enter item name - ')
    if item_name in fruits_shop_inventory:
        user_input = int(input('what do you want to update? Click 1 for quantity \n Click 2 for price \n Click 3 for low-stock value \n Please Enter the value = '))
        # print(user_input)
        choice_to_field = {
            1 :'quantity',
            2 : 'price',
            3 : 'low-stock value'
        }
        another_user_input = int(input(f'you have choose to update {choice_to_field[user_input]} \n Kindly enter the value you want to update here = '))
        # print(another_user_input)
        fruits_shop_inventory[item_name][choice_to_field[user_input]] = another_user_input
        show_inventory()
        main_function()
        # print(fruits_shop_inventory[item_name][choice_to_field[user_input]])
    else:
        print(f'{item_name} is not in the inventory want to add ?')
        if input('click yes = ').lower()=='yes':
            add_new_item()
        
        
def add_new_item():
    new_item_name = input('Please enter item name - ')
    if new_item_name in fruits_shop_inventory:
        print(f'{new_item_name} is alredy there in the inventory, then you just need to update the values of {new_item_name} in inventory system')
        if input('want to update? Click yes = ').lower() =='yes':
            update_inventory()
        else:
            show_inventory()
            main_function()
    else:
        new_item_quantity = int(input(f'Enter the quantity of {new_item_name} = '))
        new_item_price = int(input(f'Enter the price of {new_item_name} = '))
        new_item_lowstock_value = int(input(f'Enter the low-stock value of {new_item_name} = '))
        
        fruits_shop_inventory[new_item_name]={
            "quantity": new_item_quantity,
            "price":new_item_price,
            "low-stock value":new_item_lowstock_value
        }
        show_inventory()
        main_function()
        
def delete_item():
    item_name = input('Please enter item name - ')
    if item_name not in fruits_shop_inventory:
        print(f'{item_name} is not found')
    else:
        if input(f'Are you sure you want to delete {item_name}? Type yes to confirm = ').lower() == 'yes':
            del fruits_shop_inventory[item_name]
            show_inventory()
            main_function()
        else:
            print('The item is not yet deleted becauses you not write yes')
            show_inventory()
            main_function()

def show_inventory():
    for key in fruits_shop_inventory:
        print(f"The inventory has {key} with quantity {fruits_shop_inventory[key]['quantity']}, price {fruits_shop_inventory[key]['price']}, and low-stock value is {fruits_shop_inventory[key]['low-stock value']}.")
    main_function()

def main_function():
    user_input = int(input(f"What do you want to do? Click 1 to see the inventory \n Click 2 to add new item into the inventory \n Click 3 to update the existing inventory or it's value \n Click 4 to delete the item from inventory \n Kindly Enter your answer here = "))
    if user_input == 1:
        show_inventory()
    elif user_input == 2:
        add_new_item()
    elif user_input == 3:
        update_inventory()
    elif user_input == 4:
        delete_item()
    else:
        print('You entered the wrong number. Kindly enter perfect number')
        sys.exit()

main_function()


# def update_item_quantity(item_name,given_quantity):
#     if item_name in fruits_shop_inventory:
#         fruits_shop_inventory[item_name]['quantity'] = given_quantity
#         # show_inventory()
    
# def update_item_price(item_name,given_price):
#     if item_name in fruits_shop_inventory:
#         fruits_shop_inventory[item_name]['price'] = given_price
#         # show_inventory()

# def update_item_lowstock_value(item_name,given_lowstock_value):
#     if item_name in fruits_shop_inventory:
#         fruits_shop_inventory[item_name]['low-stock value'] = given_lowstock_value
#         # show_inventory()

# item_name = input('Please enter item name - ')
# quantity = int(input('Please enter the quantity you want to update - '))

# update_item_quantity(item_name=item_name,given_quantity=quantity)