#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

print(validUTF8([229, 65, 127]))  # False
print(validUTF8([197, 130, 1]))   # True
print(validUTF8([235, 140, 4]))   # False
print(validUTF8([240, 162, 138, 147]))  # True (4-byte sequence)
print(validUTF8([250, 162, 138, 147, 187]))
