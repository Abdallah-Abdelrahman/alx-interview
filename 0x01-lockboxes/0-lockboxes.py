#!/usr/bin/python3
'''Module defines `canUnlockAll` function'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened.
    Args:
        boxes(List[List[int]]): list of lists of integers
    Returns:
        bool: True if all boxes can be opened, else return False
    '''
    if not isinstance(boxes, list):
        return False

    unlocked = set()
    len_ = len(boxes)

    for i, box in enumerate(boxes):
        if i == 0 and len(box) == 0:
            return False
        if 0 < i < len_ - 1 and len(box) == 0:
            return False
        unlocked.update(k for k in box if 0 < k < len_)

    # print(unlocked, boxes)
    return len_ - 1 == len(unlocked)
