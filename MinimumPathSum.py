from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])  # grid dimensions
        dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]  # dp with sentinel borders
        dp[ROWS - 1][COLS] = 0  # base: cost after bottom-right is 0
        for r in range(ROWS - 1, -1, -1):  # iterate rows bottom-up
            for c in range(COLS - 1, -1, -1):  # iterate cols right-to-left
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])  # take min of down/right
        return dp[0][0]  # answer: min path sum from top-left