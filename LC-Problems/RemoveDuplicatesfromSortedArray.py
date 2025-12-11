#Two Pointers 
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize the left pointer to 1 (first element is always unique)
        l = 1
        
        # Iterate through the list starting from the second element (index 1)
        for r in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[r] != nums[r - 1]:
                # If different, assign the current element to the position at 'l'
                nums[l] = nums[r]
                # Increment the left pointer
                l += 1
        
        # Return the count of unique elements, which is the value of 'l'
        return l
