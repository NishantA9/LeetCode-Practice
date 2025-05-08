from typing import List
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1  # Base case: 1 way to reach 0
        for num in nums:
            nextDp = defaultdict(int)
            for total, count in dp.items():
                nextDp[total + num] += count # Option 1: add the number
                nextDp[total - num] += count # Option 2: subtract the number
            dp = nextDp  # Move to next state
        return dp[target]  # Number of ways to reach 'target'