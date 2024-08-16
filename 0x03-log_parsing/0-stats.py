#!/usr/bin/python3
""" Log parsing """


import sys
import re


def print_stats(size: int, status: dict) -> None:
    """ Print stats """
    print("File size: {:d}".format(size))
    for key in sorted(status.keys()):
        if status[key] > 0:
            print("{:d}: {:d}".format(int(key), status[key]))


if __name__ == "__main__":
    status = {"200": 0, "301": 0, "400": 0,
              "401": 0, "403": 0, "404": 0,
              "405": 0, "500": 0}
    size = 0
    count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            pat = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - ' + \
                  r'\[\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}\.\d{1,6}\]' +\
                  r' "GET /projects/260 HTTP/1.1" (\d{1,3}) (\d{1,4})$'
            if not re.fullmatch(pat, line):
                continue
            count += 1
            line = line.split()
            if line[-2] in status:
                status[line[-2]] += 1
            size += int(line[-1])
            if count % 10 == 0:
                print_stats(size, status)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(size, status)
