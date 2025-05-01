from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)  # Handle case where max product is a single negative number
        curMin, curMax = 1, 1  # Initialize current min and max products
        for n in nums:
            tmp = curMax * n  # Temporarily store current max * n
            curMax = max(n * curMax, n * curMin, n)  # Update max: use current, extend max/min
            curMin = min(tmp, n * curMin, n)  # Update min similarly (use tmp for correct order)
            res = max(res, curMax)  # Update result with the best seen so far
        return res