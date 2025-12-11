from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]  # global max and min subarray sums
        curMax, curMin = 0, 0  # current max/min ending at this position
        total = 0  # sum of all elements
        for num in nums:
            curMax = max(curMax + num, num)  # best ending here for max
            curMin = min(curMin + num, num)  # best ending here for min
            total += num  # accumulate total sum
            globMax = max(globMax, curMax)  # update global max
            globMin = min(globMin, curMin)  # update global min
        # If all numbers negative, globMax is the answer; otherwise max of normal and circular
        return max(globMax, total - globMin) if globMax > 0 else globMax