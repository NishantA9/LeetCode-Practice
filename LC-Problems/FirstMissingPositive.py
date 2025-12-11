from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the list

        # Step 1: Replace negative numbers and numbers > n with 0
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0  # Set out-of-range values to 0

        # Step 2: Use index as a marker for presence of numbers
        for i in range(n):
            val = abs(nums[i])  # Get the absolute value
            if 1 <= val <= n:  # If value is in the range 1 to n
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1  # Mark as found by making negative
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (n + 1)  # Special marker for found

        # Step 3: Find the first index with a non-negative value
        for i in range(n):
            if nums[i] >= 0:
                return i + 1  # The missing positive is index + 1

        return n + 1  # If all are present, return n + 1