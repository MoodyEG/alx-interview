#!/usr/bin/python3
""" Solving the N queens puzzle """
import sys


def solvequeen(n: int) -> None:
    """ Solving the N queens puzzle """
    # setting up the board
    board = [-1] * n
    # starting backtracking
    backqueen(board, 0)


def backqueen(board: list, row: int) -> None:
    """ Recursive helper function to place queens on the board """
    if row == len(board):
        # finished the final row
        print_solution(board)
        return
    # reseting
    board[row] = -1
    while (board[row] < len(board) - 1):
        # testing a vlaue and backtrack it
        board[row] += 1
        if isvalid(board, row):
            # if valid, we place a queen
            backqueen(board, row + 1)


def isvalid(board: list, row: int) -> bool:
    """ Check if placing a queen at this position is valid """
    for i in range(row):
        if board[i] == board[row]:
            # the same row
            return False
        if abs(board[i] - board[row]) == abs(i - row):
            # diagonal
            return False
    # all good
    return True


def print_solution(board: list) -> None:
    """ Print a solution of the N-Queens problem """
    solution = []
    for i in range(len(board)):
        # for each column, find the queen
        solution.append([i, board[i]])
    # print the solution
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    solvequeen(n)
