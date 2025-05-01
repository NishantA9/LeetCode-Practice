from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)  # Initialize each element's LIS as 1
        for i in range(len(nums) - 1, -1, -1):        # Traverse from right to left
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:                # If a longer increasing subsequence can be formed
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)  # Return the maximum value in LIS array