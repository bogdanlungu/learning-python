class Cart:

    def __init__(self):
        self._contents = dict()

    def __repr__(self):
        return "{0} {1}".format(Cart, self.__dict__)

    def process(self, order):
        if order.add:
            if not order.item in self._contents:
                self._contents[order.item] = 0
            self._contents[order.item] += 1
        elif order.delete:
            if order.item in self_contents:
                self.contents[order.item] -= 1
                if self._contents[order.item] <= 0:
                     del self._contents[order.item]



class Order:

    def __init__(self):
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        print("[command] [item] [command is a to add, d to delete, q to quit]")
        line = input()
        command = line[:1] #access the input from user and extract first char which is the command
        self.item = line[2:] #extract the item using offset "2:" which is first letter

        if command == "a":
           self.add = True
        elif command == "d":
            self.delete = True
        elif command == "q":
            self.quit = True



cart = Cart()
order = Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = Order()
    order.get_input()

print(cart)
