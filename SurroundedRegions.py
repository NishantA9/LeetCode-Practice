from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):# DFS to mark connected 'O's starting from borders
            if (r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O"):
                return  # Out of bounds or not an 'O' → stop
            board[r][c] = "T"  # Temporarily mark as non-flippable (connected to border)
            # dfs(r + 1, c)            # Explore all 4 directions
            # dfs(r - 1, c)
            # dfs(r, c + 1)
            # dfs(r, c - 1)
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(ROWS): # Step 1: DFS from all border 'O's
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs(r, c)        
        for r in range(ROWS):   # Step 2: Flip all remaining 'O's to 'X' (surrounded)
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"  
                elif board[r][c] == "T":
                    board[r][c] = "O"      
        # for r in range(ROWS):   # Step 3: Restore all 'T' back to 'O' (border-connected)
        #     for c in range(COLS):
        #         if board[r][c] == "T":
        #             board[r][c] = "O"
        
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         ROWS, COLS = len(board), len(board[0])
#         def capture(r, c):        # DFS to mark 'O's connected to border as temporary 'T'
#             if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):  # Stop DFS if out of bounds or current cell is not 'O'
#                 return
#             board[r][c] = "T"  # Temporarily mark as safe
#             capture(r + 1, c)            # Explore in all 4 directions= up, down, left, right
#             capture(r - 1, c)
#             capture(r, c + 1)
#             capture(r, c - 1)
#         for r in range(ROWS): # Step 1: Mark 'O's on the border and connected to border
#             for c in range(COLS):
#                 if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
#                     capture(r, c)
#         for r in range(ROWS): # Step 2: Convert surrounded 'O's to 'X'
#             for c in range(COLS):
#                 if board[r][c] == "O":
#                     board[r][c] = "X"
#         for r in range(ROWS): # Step 3: Convert back temporary 'T' to 'O'
#             for c in range(COLS):
#                 if board[r][c] == "T":
#                     board[r][c] = "O"