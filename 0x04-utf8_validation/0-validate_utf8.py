#!/usr/bin/python3

def validUTF8(data):
    for v in data:
        if (v >> 8) != 0:
            return False
    return True
