from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, res, count = 0, 0, 0  # Initialize left pointer, result, and count of zeros  # noqa: E741
        for r in range(len(nums)):  # Iterate through the array with right pointer
            if nums[r] == 0:  # If we encounter a zero, increment the count of zeros
                count += 1
            while count > 1:  # If there are more than one zero in the window
                if nums[l] == 0:  # If the left pointer is at a zero
                    count -= 1  # Decrement the count of zeros
                l += 1  # Move the left pointer to the right # noqa: E741
            res = max(res, r - l + 1)  # Update the result with the maximum length found     
        return res  # Return the maximum length of consecutive ones with at most one zero flipped