#!/usr/bin/python3
""" Rain """


def rain(walls):
    """ Given a list of non-negative integers representing walls of width 1,
        calculate how much water will be retained after it rains.
        walls is a list of non-negative integers.
        Return: Integer indicating total amount of rainwater retained.
        Assume that the ends of the list (before index 0 and after index
        walls[-1]) are not walls, meaning they will not retain water.
        If the list is empty return 0. """
    if walls is None:
        return 0
    idxLeft = 0
    idxRight = len(walls) - 1
    leftMax = 0
    rightMax = 0
    rainwater = 0
    while (idxLeft <= idxRight):
        leftMax = max(leftMax, walls[idxLeft])
        rightMax = max(rightMax, walls[idxRight])
        if leftMax < rightMax:
            rainwater += leftMax - walls[idxLeft]
            idxLeft += 1
        else:
            rainwater += rightMax - walls[idxRight]
            idxRight -= 1
    return rainwater
