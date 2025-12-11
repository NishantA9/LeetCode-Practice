from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Initialize left and right pointers
        while left <= right:  # Binary search loop
            m = (left + right) // 2  # Find the middle index
            if nums[m] > target:
                right = m - 1  # Move right pointer left
            elif nums[m] < target:
                left = m + 1  # Move left pointer right
            else:
                return m  # Target found at index m
        return left  # Target not found, return insert position