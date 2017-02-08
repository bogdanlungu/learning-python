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
