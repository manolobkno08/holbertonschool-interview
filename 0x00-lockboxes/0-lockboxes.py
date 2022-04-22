def canUnlockAll(boxes):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    myKeys = [0]

    for key in myKeys:
        for item in boxes[key]:
            if item not in myKeys and item < len(boxes):
                myKeys.append(item)

    if len(myKeys) == len(boxes):
        return True
    return False
