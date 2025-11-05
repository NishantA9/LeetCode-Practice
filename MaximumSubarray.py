from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0  # maxSub holds best sum, curSum holds current running sum
        for num in nums:  # iterate through numbers
            if curSum < 0:
                curSum = 0  # reset if current sum is negative
            curSum += num  # add current number to running sum
            maxSub = max(maxSub, curSum)  # update best sum found
        return maxSub  # return maximum subarray sum