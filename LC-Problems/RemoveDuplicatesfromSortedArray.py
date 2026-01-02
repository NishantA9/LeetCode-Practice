from typing import List
class Solution: #Two Pointers 
    def removeDuplicates(self, nums: List[int]) -> int:       
        l = 1   # Initialize the left pointer to 1 (first element is always unique) # noqa: E741                
        for r in range(1, len(nums)): # Iterate through the list starting from the second element (index 1)            
            if nums[r] != nums[r - 1]: # Check if the current element is different from the previous one             
                nums[l] = nums[r] # If different, assign the current element to the position at 'l'                
                l += 1 # Increment the left pointer    # noqa: E741            
        return l # Return the count of unique elements, which is the value of 'l'