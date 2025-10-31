from typing import List
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])  # number of rows and columns
        dp = [0] * (N + 1)  # dp[c] stores ways from current row at column c
        dp[N - 1] = 1  # base: one way from destination cell if it's not blocked
        for r in range(M - 1, -1, -1):  # iterate rows bottom-up
            for c in range(N - 1, -1, -1):  # iterate columns right-to-left
                if grid[r][c]:  # obstacle found
                    dp[c] = 0  # no paths through an obstacle
                else:
                    dp[c] += dp[c + 1]  # ways = down (dp[c]) + right (dp[c+1])
        return dp[0]  # ways from top-left