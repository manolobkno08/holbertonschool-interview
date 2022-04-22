#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Unlock boxes and return 
    True or False
    """
    unlockBoxes = [0]

    for key in unlockBoxes:
        for item in boxes[key]:
            if item not in unlockBoxes and item < len(boxes):
                unlockBoxes.append(item)
    if len(unlockBoxes) == len(boxes):
        return True
    else:
        return False
