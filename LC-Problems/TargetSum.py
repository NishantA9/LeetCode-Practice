from typing import List
# from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> number of ways
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            # Option 1: Add current number # Option 2: Subtract current number
            dp[(i, total)] = (
                backtrack(i + 1, total + nums[i]) +
                backtrack(i + 1, total - nums[i])
            )
            return dp[(i, total)]
        return backtrack(0, 0)

#Another approach using dynamic programming space optimization
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int) #hashmap initialization
        dp[0] = 1  # Base case: 1 way to reach 0
        for num in nums:
            nextDp = defaultdict(int)
            for total, count in dp.items():
                nextDp[total + num] += count # Option 1: add the number
                nextDp[total - num] += count # Option 2: subtract the number
            dp = nextDp  # Move to next state
        return dp[target]  # Number of ways to reach 'target'

'''