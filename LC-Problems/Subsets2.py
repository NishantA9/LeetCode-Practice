from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the input to handle duplicates easily
        def backtrack(i, subset):
            if i == len(nums):  # Reached the end of the array
                res.append(subset[::])  # Add a copy of the current subset
                return
            subset.append(nums[i])            # Include nums[i]
            backtrack(i+1, subset)
            subset.pop()  # Backtrack: remove last element to try the other path
            while i + 1 < len(nums) and nums[i] == nums[i+1]:            # Skip duplicates
                i += 1
            backtrack(i+1, subset) # Exclude nums[i]
        backtrack(0, [])
        return res