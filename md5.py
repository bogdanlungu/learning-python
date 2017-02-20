"""Convert a string to md5 hash"""
# pylint: disable=C0103
import hashlib


def toMD5(string):
    """To md5"""
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

m = toMD5('hello')
print(m)
