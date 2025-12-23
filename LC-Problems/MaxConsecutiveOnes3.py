from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = {0: 0, 1: 0} # Initialize a dictionary to count occurrences of 0 and 1
        l = 0     # Left pointer for the sliding window  # noqa: E741
        res = 0   # Result to store the maximum length
        maxF = 0  # Maximum frequency of 1's in the current window
        for r in range(len(nums)):  # Iterate through the array with right pointer
            count[nums[r]] = 1 + count.get(nums[r], 0) # Increment the count of the current number (0 or 1)
            maxF = max(count[1], maxF) # Update the maximum frequency of 1's seen so far
            while (r - l + 1) - maxF > k: # Shrink the window from the left if the number of zeros exceeds k           
                count[nums[l]] -= 1 # Decrement the count of the number at left pointer              
                l += 1 # Move the left pointer to the right # noqa: E741               
            res = max(res, r - l + 1) # Update the result with the current window size        
        return res # Return the maximum length found      