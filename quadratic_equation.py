"""Second order equation solved."""
# pylint: disable=C0103
import math

a = int(input("Enter a: "))
if a == 0:
    print("a should not be 0")
    a = int(input("Enter a again: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b**2 - (4 * a * c)

if d < 0:
    print("No real solution")
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print("One solutions: ", x)
else:
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    print("Two solutions: ", x1, " and", x2)
