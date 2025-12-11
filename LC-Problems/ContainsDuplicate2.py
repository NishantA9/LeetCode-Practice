from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}  # Dictionary to store the last index of each number
        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:  # Check if duplicate within k distance
                return True  # Found such a duplicate
            seen[nums[i]] = i  # Update the last seen index for this number
        return False  # No such duplicate found