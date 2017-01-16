""" Some useful information about dictionaries.
    Dictionaries are one of the most interesting built-in data type.
    They look like JavaScript object.
"""
# pylint: disable=C0103

a = {'A': 1, 'B': 2, 'C': 3}
b = {'A': 1, 'B': 2, 'C': 3}
c = {'A': 1, 'B': 2, 'C': 3}
d = dict(zip(['A', 'B', 'C'], [1, 2, 3]))

print(a == b == c == d)
print(d['A'])


# Dictionaries are mutable data types
a['A'] = 5
print('New value of a is: ' + str(a))


# Delete a key
del a['C']
print('New value of a after deleting one key: ' + str(a))


# Add a new Key
a['C'] = 8
print('New value of a after adding a key is: ' + str(a))


# Keys, values and items - special dictionary objects called dictionary views
# Keys
print('The a dictionary keys are ' + str(a.keys()))

# Values
print('The a dictionary values are ' + str(a.values()))

# Items
print('The a dictionary items are ' + str(a.items()))
