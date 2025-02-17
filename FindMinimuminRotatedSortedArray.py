from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]  # Initialize result as the first element
        l, r = 0, len(nums) - 1 # Set left and right pointers  # noqa: E741
        while l <= r:    # Perform binary search
            if nums[l] < nums[r]:  # If array is already sorted, the leftmost element is the minimum
                res = min(res, nums[l])
                break
            m = (l + r) // 2 # Calculate middle index
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # Determine which side to search next
                l = m + 1  # Minimum is on the right  # noqa: E741
            else:  
                r = m - 1 # Minimum is on the left
        return res  # Return the minimum element found