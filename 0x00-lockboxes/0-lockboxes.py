#!/usr/bin/python3

"""
    You have n number of locked boxes in front of you. Each
    box is numbered sequentially from 0 to n - 1 and each box
    may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """Unlock boxes and return True or False"""
    unlockBoxes = [0]

    for key in unlockBoxes:
        for item in boxes[key]:
            if item not in unlockBoxes and item < len(boxes):
                unlockBoxes.append(item)
    if len(unlockBoxes) == len(boxes):
        return True
    else:
        return False
