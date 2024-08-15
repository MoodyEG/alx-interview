#!/usr/bin/python3
""" Log parsing """


import sys
import re


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
            pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) -' + \
            r' (\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]) ' + \
            r'"GET /projects/260 HTTP/1.1" (\d{1,3}) (\d+)$'
            if not re.fullmatch(pattern, line.strip()):
                print(line)
                print("fail")
                continue
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
    finally:
        print_stats(size, status)
