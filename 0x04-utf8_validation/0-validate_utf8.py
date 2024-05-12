#!/usr/bin/python3
"""UTF8 Validator"""


def validUTF8(data):
    for v in data:
        if (v >> 8) != 0:
            return False
    return True
