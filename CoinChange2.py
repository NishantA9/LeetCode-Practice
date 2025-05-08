from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make amount 0
        for i in range(len(coins) - 1, -1, -1): # For each coin, update number of ways to form amounts # You can also loop forward
            for a in range(1, amount + 1):
                if coins[i] <= a:
                    dp[a] += dp[a - coins[i]]
        return dp[amount]