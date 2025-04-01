from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])  # Get grid dimensions
        path = set()  # To keep track of visited cells during DFS
        def dfs(r, c, i): # Base case: All characters matched
            if i == len(word):
                return True
            # Invalid path: Out of bounds, wrong char, or cell already used
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))  # Mark the current cell as visited
            # Explore all 4 directions: down, up, right, left
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))  # Backtrack after exploring
            return res
        # Try to start DFS from every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # Start from index 0 of word
                    return True
        return False  # No valid path found