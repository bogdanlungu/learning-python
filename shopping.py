# This program runs a shopping cart
# There is a cart, the user can add or remove items from the cart

def get_order():
    print("[command] [item] [command is a to add, d to delete, q to quit]")
    line = input()
    command = line[:1] #access the input from user and extract first char which is the command
    item = line[2:] #extract the item using offset "2:" which is first letter
                    #from second word and goes until the end of the string

    return command, item

def add_to_cart(item, cart):
    if not item in cart:
        cart[item] = 0
    cart[item] += 1

def delete_from_cart(item, cart):
    if item in cart:
        if cart[item] == 1:
            del cart[item]
        else:
            cart[item] -= 1

# Check the command received from the user and add, remove or quit the cart
def process_order(order, cart):
    command, item = order
    if command == "a":
        add_to_cart(item, cart)
        print(command)
    elif command == "d" and item in cart:
        delete_from_cart(item, cart)
    elif command == "q":
         return False

    return True

# The main function that runs the program
def go_shopping():
    cart = dict()

    while True:
        order = get_order()
        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")

go_shopping()
