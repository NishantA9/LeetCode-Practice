from typing import List
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)  # Track seen numbers in each row
        col = collections.defaultdict(set)  # Track seen numbers in each column
        square = collections.defaultdict(set)  # Track seen numbers in each 3x3 box
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue  # Skip empty cells
                val = board[r][c]
                if (val in row[r] or val in col[c] or val in square[(r // 3, c // 3)]):
                    return False  # Duplicate found in row, column, or 3x3 square
                row[r].add(val)  # Mark value as seen in current row
                col[c].add(val)  # Mark value as seen in current column
                square[(r // 3, c // 3)].add(val)  # Mark value in current 3x3 square
        return True  # No duplicates found — valid Sudoku