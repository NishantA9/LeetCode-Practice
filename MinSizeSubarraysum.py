from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0, 0  # left pointer and current sum
        res = float("inf")  # Initialize result as infinity
        for right in range(len(nums)):  # right pointer
            total += nums[right]  # Add current number to total
            while total >= target:  # While sum is enough
                res = min(right - left + 1, res)  # Update min length
                total -= nums[left]  # Remove leftmost number
                left += 1  # Move left pointer forward
        return 0 if res == float("inf") else res  # Return 0 if no valid subarray