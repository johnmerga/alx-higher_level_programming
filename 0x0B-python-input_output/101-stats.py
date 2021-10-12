#!/usr/bin/python3
''' script for processing requests logs '''
import signal
import re

count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0


def print_logs():
    ''' prints the logs '''
    global status_codes, total_file_size

    print('File size: {:d}'.format(total_file_size))
    for code, tally in status_codes.items():
        if tally:
            print('{:d}: {:d}'.format(code, tally))


def sigint(sig, sframe):
    ''' SIGINT handler '''
    if count % 10:
        print_logs()
    signal.default_int_handler()
    exit(0)


def main():
    ''' logs network requests '''
    global count, status_codes, total_file_size

    signal.signal(signal.SIGINT, sigint)
    r = re.compile(r'(?P<ip_address>.*) - \[(?P<date>.+)\] ' +
                   r'"GET /projects/260 HTTP/1.1" ' +
                   r'(?P<status_code>\d+) (?P<file_size>\d+)\w*$')
    while True:
        count += 1
        try:
            match = r.match(input()).groupdict()
            if not match:
                continue
        except EOFError:
            print_logs()
            exit(0)
        status_code = int(match['status_code'])
        if status_code in status_codes:
            status_codes[status_code] += 1
            total_file_size += int(match['file_size'])
            if not count % 10:
                print_logs()

if __name__ == '__main__':
    main()
