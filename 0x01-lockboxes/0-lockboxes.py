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

    len_ = len(boxes)
    unlocked = set([0])
    front = 0
    rear = 1
    keys = [0]

    while front != rear:
        if front >= len_:
            break
        for key in boxes[keys[front]]:
            if key not in unlocked and key < len_:
                unlocked.add(key)
                keys.insert(rear, key)
                rear += 1
        front += 1

    # print(unlocked, boxes)
    return len_ == len(unlocked)
