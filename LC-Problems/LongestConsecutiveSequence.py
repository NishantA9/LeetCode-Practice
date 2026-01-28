from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # Convert the list of numbers into a set to remove duplicates and allow O(1) lookups for the elements
        longest = 0   # Initialize a variable to keep track of the longest sequence length        
        for n in nums:  # Iterate over each number in the original list
            if (n - 1) not in numSet:  # Check if the current number is the start of a sequence (i.e., there is no number 'n-1' in the set)                
                length = 0 # If it is the start, initialize the length of this sequence                                
                while (n + length) in numSet: # Continue checking for the next numbers in the sequence by incrementing length until the sequence breaks
                    length += 1                                
                longest = max(length, longest) # Update the longest sequence found so far                
        return longest # Return the length of the longest consecutive sequence