from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Initialize left and right pointers  # noqa: E741
        while l <= r:  # Continue until search space is exhausted
            m = (l + r) // 2  # Find the middle index
            if nums[m] > target:  # If target is smaller, search the left half
                r = m - 1
            elif nums[m] < target:  # If target is larger, search the right half
                l = m + 1  # noqa: E741
            else:  # If found, return the index
                return m
        return -1  # If not found, return -1