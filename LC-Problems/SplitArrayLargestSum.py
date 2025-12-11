from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1  # Start with one subarray
            curSum = 0    # Current sum of the subarray
            for num in nums:
                curSum += num  # Add number to current subarray
                if curSum > largest:  # If sum exceeds allowed largest
                    subarray += 1     # Start a new subarray
                    if subarray > k:  # Too many subarrays needed
                        return False
                    curSum = num      # Start new subarray with current num
            return True  # Can split into k or fewer subarrays

        left, right = max(nums), sum(nums)  # Range for binary search
        res = right  # Store the minimum largest sum found
        while left <= right:
            mid = left + (right - left) // 2  # Try the middle value
            if canSplit(mid):  # If possible to split with this largest sum
                res = mid      # Update result
                right = mid - 1  # Try smaller largest sum
            else:
                left = mid + 1  # Try larger largest sum
        return res  # Return the minimum largest sum