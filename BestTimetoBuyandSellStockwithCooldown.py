from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # Memoization: (index, buying) → max profit
        def dfs(i, buying):
            if i >= len(prices):
                return 0  # Base case: no days left
            if (i, buying) in dp:
                return dp[(i, buying)]  # Return cached result
            cooldown = dfs(i + 1, buying)  # Option 1: skip this day
            if buying:
                buy = dfs(i + 1, False) - prices[i]  # Option 2: buy → subtract price and go to selling state next day
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i] # Option 2: sell → add price and skip one day (cooldown)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)  # Start from day 0 in buying state 