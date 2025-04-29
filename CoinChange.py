from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)        # Step 1: Initialize dp array with dummy max value (amount+1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0
        for a in range(1, amount + 1):        # Step 2: Build up the dp table
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c]) # Try taking coin 'c' and update minimum coins for amount 'a'
        return dp[amount] if dp[amount] != amount + 1 else -1  # Step 3: Check if a valid solution exists