from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[x] = number of ways to reach sum x
        dp = {0: 1}  # base: one way to reach 0 (take nothing)
        for total in range(1, target + 1):         # Build ways for all totals from 1..target
            dp[total] = 0  # start with zero ways
            for num in nums:
                # If we can use num, add ways to make (total - num)
                dp[total] += dp.get(total - num, 0)
        return dp[target] # Return number of ways to reach target