#!/usr/bin/python3

"""program to solve N-queens puzzle"""

import sys


def is_safe(board, row, col, n):
    """ Check if there is a queen in the same column"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """solve nqueens"""
    if n < 4:
        return []

    def solve(board, row):
        """solve"""
        if row == n:
            solutions.append(
                    [[r, c] for r, row in enumerate(board)
                        for c, val in enumerate(row) if val == 1])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0
    solutions = []
    solve([[0] * n for _ in range(n)], 0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = solve_nqueens(N)
        for solution in solutions:
            print(solution)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
