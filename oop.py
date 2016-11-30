class Fleet:

    def __init__(self):
        self._cars = []

    def add_car(self, car):
        self._cars.append(car)

    def remove_car(self, car):
        self, _people.remove(car)


    def show_fleet(self):
        for car in self._cars:
            car.display_brand()


class Car:

    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(id(self))
        print("The brand is: ", self.brand)


fleet = Fleet()
fleet.add_car(Car("Audi"))
fleet.add_car(Car("BMW"))
fleet.add_car(Car("Chevrolet"))
fleet.add_car(Car("Fiat"))
fleet.show_fleet()
