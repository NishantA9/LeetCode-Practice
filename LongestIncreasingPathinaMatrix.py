from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # Memoization: (r, c) → length of longest increasing path from that cell
        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal): # Out of bounds or not strictly increasing
                return 0
            if (r, c) in dp:
                return dp[(r, c)]  # Return cached result
            res = 1  # Start with current cell
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c])) # Explore all 4 directions
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res  # Cache the result
            return res
        for r in range(ROWS): # Compute the result for every cell
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values()) # Return the longest path from any cell