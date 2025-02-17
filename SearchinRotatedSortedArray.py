from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # Initialize the search space  # noqa: E741
        while l <= r:         # Binary search
            m = (l + r) // 2  # Calculate the middle index
            if target == nums[m]:  # Check if the middle element is the target
                return m
            if nums[l] <= nums[m]: # Check if the left half is sorted
                # Check if the target lies within the left sorted portion
                if target > nums[m] or target < nums[l]:
                    l = m + 1  # Move to the right half  # noqa: E741
                else:
                    r = m - 1  # Move to the left half
            else:  # Otherwise, the right half is sorted
                if target < nums[m] or target > nums[r]: # Check if the target lies within the right sorted portion
                    r = m - 1  # Move to the left half
                else:
                    l = m + 1  # Move to the right half  # noqa: E741
        return -1  # Target not found