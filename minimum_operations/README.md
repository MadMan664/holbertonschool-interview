# Minimum Operations

A text file contains a single character `H`. The only two operations
available are **Copy All** and **Paste**. `minOperations(n)` returns the
fewest number of operations needed to get exactly `n` `H` characters in the
file, or `0` if `n` is impossible to achieve.

## Approach

Multiplying the current length by a factor `f` costs one Copy All plus
`f - 1` Pastes, so `f` operations. The fewest operations for `n` is the sum
of the prime factors of `n`.

| n | Prime factors | Operations |
|---|---------------|------------|
| 4 | 2 x 2 | 4 |
| 9 | 3 x 3 | 6 |
| 12 | 2 x 2 x 3 | 7 |

## Files

| File | Description |
|------|-------------|
| `0-minoperations.py` | `minOperations(n)` returns an integer |

## Usage

    $ ./0-main.py
