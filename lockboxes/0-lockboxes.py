#!/usr/bin/python3
"""Module for the lockboxes problem."""


def canUnlockAll(boxes):
    """Determine whether every box can be opened.

    Box 0 starts unlocked. Each box holds keys, and a key with the
    same number as a box opens that box.

    Args:
        boxes (list): a list of lists of keys, one list per box.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)
    if n == 0:
        return True

    opened = {0}
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == n
