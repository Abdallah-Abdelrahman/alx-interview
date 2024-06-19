#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import signal
from sys import stdin
from re import search, compile

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


def handler(signum, frame):
    '''sginal handler'''
    print_statistics(total)


if __name__ == '__main__':
    i = 0
    total = 0
    # signal interrupt handler
    signal.signal(signal.SIGINT, handler)

    for line in stdin:
        # regex to match log line
        ip_regex = r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}'
        mid_regex = r' "GET /projects/260 HTTP/1.1" '

        regex = compile(ip_regex+r' - \[\S+ \S+\]'+mid_regex+r'(\d{3}) (\d+)$')
        m = regex.match(line)

        if not m:
            # there's no match skip line
            continue

        _, __, ___, status_code, size = m.groups()
        # size, status_code = toks[-1].replace('\n', ''), toks[-2]

        if status_code.isnumeric and int(status_code) in STATUS:
            STATUS[int(status_code)] += 1
        if size.isnumeric:
            total += int(size)

        if (i + 1) % 10 == 0:
            # print statistic
            print_statistics(total)
        i += 1
