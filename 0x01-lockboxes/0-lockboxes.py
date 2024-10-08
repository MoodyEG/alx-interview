#!/usr/bin/python3
""" LockBox """


def canUnlockAll(boxes):
    """ canUnlockAll """
    if type(boxes) is not list or len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    keys = set()
    keys.add(0)
    change = True
    while change:
        change = False
        for i, box in enumerate(boxes):
            if i in keys:
                for key in box:
                    if key < len(boxes) and key not in keys:
                        keys.add(key)
                        change = True
                        if len(keys) == len(boxes):
                            return True
    return False
