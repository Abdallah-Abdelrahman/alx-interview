#!/usr/bin/python3
'''Module defines `validUTF8` function '''


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data(List[int]): data set to check against
    Returns:
        bool: True if valid utf8 data, False otherwise
    '''
    i = 0
    while i < len(data):
        char = data[i]
        count = 0
        cursor = 7
        bit = 1

        while bit:
            if count > 4:
                break
            bit = (char >> cursor) & 1
            if bit:
                # if bit is set; increase count,
                # to determine number of bytes
                count += 1
            cursor -= 1

        if count > 4 or count == 1:
            # invalid bits sequence
            return False

        for j in range(1, count):
            # enumerate thro next elements,
            # to check their continuation code point
            if i + j >= len(data):
                # invalid byte sequence
                return False
            byte = data[i + j]
            if byte >> 6 != 0b10:
                # check value of leftmost 2 bits is 10
                # indicating continuation code point
                return False

        i += count if count else 1

    return True
