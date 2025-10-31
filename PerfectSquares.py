class Solution:
    def numSquares(self, n: int) -> int:
        # dp[x] = minimum number of perfect squares that sum to x
        dp = [n] * (n + 1)  # initialize with worst case (1+1+...)
        dp[0] = 0  # zero requires zero squares
        for target in range(1, n + 1):        # Build dp from 1 to n
            # try all square numbers s*s <= target
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break  # no need to check larger s
                dp[target] = min(dp[target], 1 + dp[target - square]) # choose the best between current and using this square
        return dp[n]  # minimum squares to form n