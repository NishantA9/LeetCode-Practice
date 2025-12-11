# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()  # Sort the array in ascending order
#         return nums[len(nums) - k]  # Return the k-th largest element

# Solution 2: QuickSelect Algorithm (Optimized Approach)
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # Convert to index for k-th largest element (0-based index)
        def quickSelect(l, r): #  # noqa: E741
            pivot, p = nums[r], l  # Use the last element as pivot
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]  # Swap to partition
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]  # Place pivot in correct position
            if p > k:  # If pivot is too large, search left part
                return quickSelect(l, p - 1)
            elif p < k:  # If pivot is too small, search right part
                return quickSelect(p + 1, r)
            else:
                return nums[p]  # Found the K-th largest element
        return quickSelect(0, len(nums) - 1)