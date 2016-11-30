# Cart class
# Adds or deletes products from the cart
# it also has a __repr__ method that shows what products are in the cart


class Cart:

    def __init__(self):
        self._contents = dict()

    def __repr__(self):
        return "Your shopping cart has these products: {0}".format(self._contents)

    def process(self, order):
        if order.add:
            if not order.item in self._contents:
                self._contents[order.item] = 0
            self._contents[order.item] += 1
        elif order.delete:
            if order.item in self._contents:
                self._contents[order.item] -= 1
                if self._contents[order.item] <= 0:
                    del self._contents[order.item]

