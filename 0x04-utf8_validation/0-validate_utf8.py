#!/usr/bin/python3
"""UTF8 Validator"""


def validUTF8(data):
    for v in data:
        print(bin(v), bin(v & 0xFF))
        if (v >> 8) != 0:
            ...
    return True
