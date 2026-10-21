#!/usr/bin/python3
"""UTF-8 Validation: check that a list of integers is valid UTF-8."""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else False.

    Each integer stands for one byte (only its 8 least significant bits
    count). A character takes 1 to 4 bytes:

        0xxxxxxx                              1 byte
        110xxxxx 10xxxxxx                     2 bytes
        1110xxxx 10xxxxxx 10xxxxxx            3 bytes
        11110xxx 10xxxxxx 10xxxxxx 10xxxxxx   4 bytes

    The data is read once, keeping a count of continuation bytes (10xxxxxx)
    that are still expected for the character in progress.
    """
    remaining = 0

    for number in data:
        byte = number & 0xFF

        if remaining == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                remaining = 1
            elif byte >> 4 == 0b1110:
                remaining = 2
            elif byte >> 3 == 0b11110:
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1

    return remaining == 0
