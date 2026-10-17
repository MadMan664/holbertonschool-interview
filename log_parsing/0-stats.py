#!/usr/bin/python3
"""Log parsing: read log lines from stdin and print running metrics."""
import re
import sys

LINE = re.compile(r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\S+) (\d+)$')
CODES = (200, 301, 400, 401, 403, 404, 405, 500)


def print_stats(total, counts):
    """Print the total file size and the line count per status code."""
    print("File size: {:d}".format(total), flush=True)
    for code in sorted(counts):
        print("{:d}: {:d}".format(code, counts[code]), flush=True)


def main():
    """Read stdin line by line and print the stats every 10 valid lines."""
    total = 0
    counts = {}
    lines = 0
    try:
        for line in sys.stdin:
            match = LINE.match(line.rstrip("\n"))
            if match is None:
                continue
            total += int(match.group(2))
            if match.group(1).isdigit() and int(match.group(1)) in CODES:
                code = int(match.group(1))
                counts[code] = counts.get(code, 0) + 1
            lines += 1
            if lines % 10 == 0:
                print_stats(total, counts)
        print_stats(total, counts)
    except KeyboardInterrupt:
        print_stats(total, counts)
        raise


if __name__ == "__main__":
    main()
