from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def capture(r, c):        # DFS to mark 'O's connected to border as temporary 'T'
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):  # Stop DFS if out of bounds or current cell is not 'O'
                return
            board[r][c] = "T"  # Temporarily mark as safe
            # Explore in all 4 directions
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        for r in range(ROWS): # Step 1: Mark 'O's on the border and connected to border
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)
        for r in range(ROWS): # Step 2: Convert surrounded 'O's to 'X'
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(ROWS): # Step 3: Convert back temporary 'T' to 'O'
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"