#!/usr/bin/python3
""" Log parsing """


import sys


def print_stats(size, status):
    """ Print stats """
    print("File size: {}".format(size))
    for key in sorted(status.keys()):
        if status[key] > 0:
            print("{}: {}".format(key, status[key]))


if __name__ == "__main__":
    status = {"200": 0, "301": 0, "400": 0,
              "401": 0, "403": 0, "404": 0,
              "405": 0, "500": 0}
    size = 0
    count = 0
    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status)
                count = 1
            else:
                count += 1
            line = line.strip()
            line = line.split()
            if len(line) > 2:
                if line[-2] in status:
                    size += int(line[-1])
                    status[line[-2]] += 1
    except KeyboardInterrupt:
        print_stats(size, status)
