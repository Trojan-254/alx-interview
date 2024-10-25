#!/usr/bin/python3
"""module for a log parser"""

from collections import defaultdict
import sys
import re


"""reads stdin, computes and returns metrics"""

total_file_size = 0
line_count = 0
status_code_counts = defaultdict(int)


pattern = (
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - \[(?P<date>[^\]]+)\] '
    r'"GET /projects/260 HTTP/1.1" (?P<status_code>\d{3}) (?P<file_size>\d+)'
)
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}


def print_metrics():
    """prints the required metrics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = re.match(pattern, line)

        if match:
            file_size = int(match.group('file_size'))
            status_code = int(match.group('status_code'))

            total_file_size += file_size

            if status_code in valid_status_codes:
              status_code_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
              print_metrics()

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
