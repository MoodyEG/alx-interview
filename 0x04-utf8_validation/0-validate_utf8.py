#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ UTF-8 Validation """

    if not data:
        return False

    for i in range(len(data)):
        if data[i] >> 7 == 0:
            continue
        elif i + 1 > len(data) and data[i] >> 5 == 6\
                and data[i + 1] >> 6 == 2:
            i += 1
            continue
        elif i + 2 > len(data) and data[i] >> 4 == 14\
                and data[i + 1] >> 6 == 2\
                and data[i + 2] >> 6 == 2:
            i += 2
            continue
        elif i + 3 > len(data) and data[i] >> 3 == 30 \
                and data[i + 1] >> 6 == 2\
                and data[i + 2] >> 6 == 2\
                and data[i + 3] >> 6 == 2:
            i += 3
            continue
        else:
            return False

    return True
