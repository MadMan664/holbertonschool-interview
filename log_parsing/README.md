# Log Parsing

`0-stats.py` reads log lines from standard input, one at a time, and prints
running metrics.

## Input format

    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

A line that does not match this format is skipped (it is not counted).

## Output

After every 10 lines, on a keyboard interruption (CTRL + C), and once at the
end of the input if lines are left over, the script prints the statistics
from the beginning:

- `File size: <total size>`, the sum of all file sizes read so far
- one line `<status code>: <number>` for each status code that appeared,
  in ascending order. Only the codes 200, 301, 400, 401, 403, 404, 405
  and 500 are reported; a code that does not appear is not printed.

## Files

| File | Description |
|------|-------------|
| `0-stats.py` | Reads stdin and computes the metrics |

## Usage

    $ ./0-generator.py | ./0-stats.py
