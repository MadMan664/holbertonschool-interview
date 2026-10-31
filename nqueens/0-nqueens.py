#!/usr/bin/python3
"""Solve the N queens puzzle and print every solution."""
import sys


def is_safe(cols, row, col):
    """Return True if a queen at (row, col) is not attacked by earlier rows."""
    for r in range(row):
        if cols[r] == col or abs(cols[r] - col) == row - r:
            return False
    return True


def solve(n, row, cols):
    """Place one queen per row and print every complete solution."""
    if row == n:
        print([[r, cols[r]] for r in range(n)])
        return
    for col in range(n):
        if is_safe(cols, row, col):
            cols.append(col)
            solve(n, row + 1, cols)
            cols.pop()


def main():
    """Check the arguments, then solve the puzzle for N."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, 0, [])


if __name__ == "__main__":
    main()
