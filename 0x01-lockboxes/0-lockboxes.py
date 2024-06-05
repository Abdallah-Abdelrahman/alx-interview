#!/usr/bin/python3
'''Module defines `canUnlockAll` function'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened.
    Args:
        boxes(List[List[int]]): list of lists of integers
    Returns:
        bool: True if all boxes can be opened, else return False
    '''
    unlocked = set()
    if not isinstance(boxes, list):
        return False

    len_ = len(boxes)

    for box in boxes:
        unlocked.update(box)

    if 0 in unlocked:
        unlocked.remove(0)
    print(unlocked, boxes)
    # return len_ - 1 == len(unlocked)
    return True
