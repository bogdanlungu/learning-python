import shopping.cart, shopping.order

cart = shopping.cart.Cart()
order = shopping.order.Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = shopping.order.Order()
    order.get_input()

print(cart)
