""" Some examples of decisions and iterations in Python
"""
# pylint: disable=C0103

# The ternary operator
order_total = 210
discount = 25 if order_total > 200 else 0
print(order_total, discount)


# simple for
a = [1, 2, 3, 4, 5, 6]
for n in a:
    print(n)

# for with range
for n in range(3):
    print(n)

# creating sequences with range, range accepts up to three arguments
# (start, stop, step)
print(list(range(3, 6)))
print(list(range(3, 10, 2)))  # including the step


# continue statement in Python
# apply a discount to products that are from last year
products = [
    {'sku': '1', 'year': 2016, 'price': 100.0},
    {'sku': '2', 'year': 2017, 'price': 50},
    {'sku': '3', 'year': 2015, 'price': 20},
]
for product in products:
    if product['year'] == 2017:
        continue
    product['price'] *= 0.6  # discount 40%
    print(
        'Price for sku', product['sku'],
        'is now', product['price'])


# break statement in Python
# check if an element of the list evaluates equals 3
items = [0, 4, 1, 2, 3, 9]  # True and 7 evaluate to True
found = False  # set a flag
for item in items:
    print('checking items', item)
    if item == 3:
        found = True
        break

if found:
    print('One item equals 3')
else:
    print('None equals 3')


# check for prime numbers in a range
primes = []
upto = 5
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)


# Python's switch
day_number = 6
if 1 <= day_number <= 5:
    day = 'Weekday'
elif day_number == 6:
    day = 'Saturday'
elif day_number == 0:
    day = 'Sunday'
else:
    day = ''
    raise ValueError(
        str(day_number) + ' not a valid day number.')
print(day)
