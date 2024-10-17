#TWO POINTERS APPROACH
# Time Complexity: O(n) where n is the number of elements in the array
# Space complexity: O(1) as we are not using any extra space
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize two pointers:  # 'l' (left) - where to place the next valid element. # 'r' (right) - to traverse through the list.
        l, r = 0, 0
        
        # Iterate through the list as long as 'r' (right pointer) is within the bounds of the list.
        while r < len(nums):
            # Initialize the count for how many times the current element appears.
            count = 1
            
            # Continue moving 'r' to the right as long as the current element (nums[r]) is equal to the next element (nums[r + 1]) to count the duplicates.
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1  # Move 'r' to the next element.
                count += 1  # Increment the count of the current element.
            
            # We only want to keep at most 2 duplicates, so we will place the current
            # element up to 'min(2, count)' times at the position indicated by 'l'.
            for i in range(min(2, count)):
                # Place the current element (nums[r]) at the position 'l'.
                nums[l] = nums[r]
                l += 1  # Move 'l' to the next position for the next valid element.
            
            # Move 'r' to the next new element after processing all duplicates of nums[r].
            r += 1
        
        # Return 'l', which represents the length of the modified list with at most
        # 2 occurrences of each element.
        return l
