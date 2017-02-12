""" Functions in Python
"""
# pylint: disable=C0103


def my_function():
    """Simple function with local scope"""
    test = 'local' # local scope
    print('my_function:', test)

test = 'global' # global scope
my_function()
print('global:', test)


# Changing a mutable in a function affects the caller
x = [1, 2, 3]
def func(x):
    """Assign a new value"""
    x[1] = 88  # affects the caller!

func(x)
print(x)  # will print [1, 88, 3]


# Default parameter values like in JS ES6
def some_func(a, b, c):
    """Default parameters for the function"""
    print(a, b, c)
some_func(a=1, c=2, b=3)  # prints: 1 3 2
s_a = 8
s_b = 9
s_c = 10
some_func(s_a, s_b, s_c) # prints: 8, 9, 10
