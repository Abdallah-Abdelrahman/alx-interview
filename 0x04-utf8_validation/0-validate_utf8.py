#!/usr/bin/python3
'''Module defines `validUTF8` function '''


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding.

    Returns:
        bool: True if valid utf8 data, False otherwise
    '''
    i = 0
    while i < len(data):
        char = data[i]
        count = 0
        cursor = 7
        bit = 1

        if char > 255 or char < 0:
            # check if char range of byte size (0-255)
            return False

        while count < 4 and bit:
            bit = (char >> cursor) & 1
            if bit:
                # if bit is set increase count
                # to determine number of bytes
                count += 1
            cursor -= 1

        for j in range(count):
            # enumerate thro next elements,
            # to check there continuation code point
            i = j + 1
            byte = data[i]
            if byte > 255 or byte < 0:
                # check if range of byte size (0-255)
                return False
            if (byte >> 6) & 2 != 2:
                # check value of leftmost 2 bits is 10
                # indicating continuation code point
                return False

        i += 1

    return True
