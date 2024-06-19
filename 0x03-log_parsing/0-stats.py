#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import signal
from sys import stdin, exit
from re import compile

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
    exit(0)


# signal interrupt handler
# signal.signal(signal.SIGINT, handler)

if __name__ == '__main__':
    i = 1
    total = 0

    try:
        for line in stdin:
            # regex to match log line
            regex = compile(
                    r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}'
                    r' - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" '
                    r'(\d{3}) (\d+)$'
                    )
            m = regex.match(line)

            if not m:
                # there's no match skip line
                continue

            _, __, ___, status_code, size = m.groups()

            if status_code.isnumeric and int(status_code) in STATUS:
                STATUS[int(status_code)] += 1
            if size.isnumeric:
                total += int(size)

            if (i) % 10 == 0:
                # print statistic
                print_statistics(total)

            # book keeping
            i += 1
    except KeyboardInterrupt:
        print_statistics(total)
