from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to keep track of the seen numbers in each column, row, and 3x3 square.
        # The keys in these dictionaries will be the row index, column index, and (row//3, column//3) tuple for squares.
        # The values will be sets that store the numbers already seen in that particular row, column, or square.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r//3, c//3)

        # Loop through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # If the current cell contains a ".", it is empty, so skip it.
                if board[r][c] == ".":
                    continue

                # Check if the current number is already in the corresponding row, column, or 3x3 square.
                # If it is, the Sudoku board is invalid, so return False.
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False

                # If the current number is not yet in the row, column, or square, add it to the respective set.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        # If no duplicates were found, the board is valid, so return True.
        return True
