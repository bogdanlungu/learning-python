# names declared in the local scope

person = 'john'
age = 12


def show_info():
    person2 = 'smith'  # name declared in the enclosing scope


print(person)

# name is not accessible - declared in function enclosing scope

# print(person2)



def local():
    m = 7
    print(m)

m = 5
print(m)

local()


# define a class

class Bike:

    def __init__(self, colour, frame_material):  # sort of constructor in JavaScript

        self.colour = colour
        self.frame_material = frame_material

    def brake(self):  # declare a new method on the class

        print("Braking!")

# instantiate the class

cube = Bike('Red', 'Aluminium')
pegas = Bike('Black', 'Steel')

print(cube.colour)
print(pegas.frame_material)
print(cube.brake())
