#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import signal
from sys import stdin
from re import search

STATUS = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
}


def print_statistics(total):
    '''print statistics'''
    out = f'File size: {total}\n'
    for k, v in sorted(STATUS.items()):
        if v > 0:
            out += f'{k}: {v}\n'
    print(out, end='')


if __name__ == '__main__':
    i = 0
    total = 0
    for line in stdin:
        # regex to match IPv4 address
        ip_m = search(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}', line)

        if not ip_m:
            # there's no match skip line
            continue

        toks = line.split(' ')
        size, status_code = toks[-1].replace('\n', ''), toks[-2]
        if status_code.isnumeric:
            STATUS[int(status_code)] += 1
        if size.isnumeric:
            total += int(size)

        signal.signal(signal.SIGINT, lambda x, y: print_statistics(total))
        if (i + 1) % 10 == 0:
            # print statistic
            print_statistics(total)
        i += 1
