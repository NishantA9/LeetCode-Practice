from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]        # Add virtual balloons with value 1 at both ends
        dp = {}  # Memoization: (l, r) → max coins
        def dfs(l, r):  # noqa: E741
            if l > r:
                return 0  # No balloons left to burst
            if (l, r) in dp:
                return dp[(l, r)]  # Return cached result
            dp[(l, r)] = 0
            for i in range(l, r + 1): # Try bursting each balloon i in [l...r] last
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)  # Solve left and right sides
                dp[(l, r)] = max(dp[(l, r)], coins)  # Maximize coins
            return dp[(l, r)]
        return dfs(1, len(nums) - 2) # Start with actual range (excluding the added 1s)