from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Use difference accumulation: sum(0..n) - sum(nums)
        # Start with n (which is len(nums)) then add i - nums[i] for each index
        # The final value is the missing number.
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]  # add contribution of index minus value
        return res