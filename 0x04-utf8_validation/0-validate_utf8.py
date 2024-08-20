#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ UTF-8 Validation """
    i = 0
    for i in range(len(data)):
        # to get the least 8 bits
        if data[i] > 255:
            data[i] = data[i] & 255
    while i < len(data):
        if data[i] >> 7 == 0:
            # num < 128
            i += 1
            continue
        elif i + 1 < len(data) and data[i] >> 5 == 6\
                and data[i + 1] >> 6 == 2:
            # 192 <= num < 224
            i += 2
            continue
        elif i + 2 < len(data) and data[i] >> 4 == 14\
                and data[i + 1] >> 6 == 2\
                and data[i + 2] >> 6 == 2:
            # 224 <= num < 239
            i += 3
            continue
        elif i + 3 < len(data) and data[i] >> 3 == 30 \
                and data[i + 1] >> 6 == 2\
                and data[i + 2] >> 6 == 2\
                and data[i + 3] >> 6 == 2:
            # 240 <= num < 247
            i += 4
            continue
        else:
            # 248 <= num < 256
            # 128 <= num < 192
            return False

    return True
