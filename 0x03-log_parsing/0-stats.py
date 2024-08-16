#!/usr/bin/python3
""" Log parsing """


import sys
import re


def print_stats(size: int, status: dict) -> None:
    """ Print stats """
    print("File size: {}".format(size))
    for key in sorted(status.keys()):
        if status[key] > 0:
            print("{}: {}".format(key, status[key]))


if __name__ == "__main__":
    status = {200: 0, 301: 0, 400: 0,
              401: 0, 403: 0, 404: 0,
              405: 0, 500: 0}
    size = 0
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            line = line.strip()
            pat = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - ' + \
                  r'\[\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}\.\d{1,6}\]' +\
                  r' "GET /projects/260 HTTP/1.1" (\d{1,3}) (\d{1,4})$'
            if not re.fullmatch(pat, line):
                continue
            line = line.split()
            if int(line[-2]) in status:
                status[int(line[-2])] += 1
                size += int(line[-1])
            if count % 10 == 0:
                print_stats(size, status)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(size, status)
