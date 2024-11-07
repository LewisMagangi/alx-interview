#!/usr/bin/python3
"""N-Queens Solver"""
import sys

# Ensure proper command line usage
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Validate the argument is a digit and at least 4
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

N = int(sys.argv[1])
if N < 4:
    print("N must be at least 4")
    exit(1)


def find_queen_positions(N, row=0, columns=[], diag1=[], diag2=[]):
    """Recursive generator to yield possible queen positions"""
    if row < N:
        for col in range(N):
            if col not in columns and row + col not in diag1 and row - col not in diag2:
                yield from find_queen_positions(N, row + 1, columns + [col], diag1 + [row + col], diag2 + [row - col])
    else:
        yield columns


def display_solutions(N):
    """Generate and print each solution configuration"""
    solution_list = []
    row_index = 0
    for solution in find_queen_positions(N):
        for col in solution:
            solution_list.append([row_index, col])
            row_index += 1
        print(solution_list)
        solution_list = []
        row_index = 0


display_solutions(N)
