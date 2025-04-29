from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) #If there's only one house, just rob it and 1. Rob from 0 to n-2 (skip last house) 2. Rob from 1 to n-1 (skip first house)
    def helper(self, nums):
        rob1, rob2 = 0, 0  # rob1 = 2 steps back, rob2 = 1 step back
        for n in nums:
            temp = max(n + rob1, rob2)  # Rob this house + rob1 OR skip and take rob2
            rob1 = rob2
            rob2 = temp
        return rob2  # Best result at the end