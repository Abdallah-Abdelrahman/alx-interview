#!/usr/bin/python3
'''Module defines `validUTF8` function '''


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding.

    Returns:
        bool: True if valid 1byte utf8, False otherwise
    '''
    for char in data:
        if 255 < char < 0:
            return False
        # using bit-wise right shift to get MSB
        # then mask it with one to get the value of MSB
        # if it's 0 then it's valid 1byte utf8
        if (char >> 8) & 1 == 1:
            return False

    return True
