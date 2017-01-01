"""This programs computes how many combinations are possible
to be made from a collection of 'n' unique integers grouped under 'g' elements.
You need to specify the length of the collection and how many elements at a time you
want to group from the collection.
The number of possible combinations will be printed."""
# pylint: disable=C0103
from math import factorial as fac

message = "Hello! Please complete the length of the collection and the value of the group"
set_message = "The collection length is:"
group_message = "Specify the group length:"

print(message)
print(set_message)
n = int(input())
print(group_message)
g = int(input())

result = fac(n) / (fac(g) * fac(n - g))
print("The number of possible combinations is " + str(int(result)))
