"""Convert a string to md5 hash"""
# pylint: disable=C0103
import hashlib


def get_input():
    """Get input"""
    print("Welcome! \nEnter the string to you want to convert:")
    return input()


def toMD5(string):
    """To md5"""
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    print("The hash is: \n" + m.hexdigest())

the_input = get_input()
toMD5(the_input)
