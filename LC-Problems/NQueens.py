from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()             # Track columns with queens
        posDiag = set()         # r + c → positive diagonals
        negDiag = set()         # r - c → negative diagonals
        res = []                # Final list of valid board configurations
        board = [["."] * n for _ in range(n)]        # Create empty n x n board with "."
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]  # Found valid config → convert to list of strings and save
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:   # Skip if column or diagonals are under attack
                    continue
                col.add(c)                # Place the queen
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                backtrack(r + 1)  # Move to next row
                col.remove(c)                # Backtrack: remove queen and try next position
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)  # Start placing queens from row 0
        return res