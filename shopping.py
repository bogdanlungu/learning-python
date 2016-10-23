# This program runs a shopping cart
# There is a cart, the user can add or remove items from the cart

def get_order():
    print("[command] [item] [command is a to add, d to delete, q to quit]")
    line = input()
    command = line[:1] #access the input from user and extract first char which is the command
    item = line[2:] #extract the item using offset "2:" which is first letter
                    #from second word and goes until the end of the string

    return command, item

# Check the command received from the user and add, remove or quit the cart
def process_order(order, cart):
    command, item = order
    if command == "a":
        cart.add(item)
        print(command)
    elif command == "d" and item in cart:
        cart.remove(item)
    elif command == "q":
         return False

    return True

# The main function that runs the program
def go_shopping():
    cart = set() # use set instead of a list, in order to prevent duplicates

    while True:
        order = get_order()
        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")

go_shopping()
