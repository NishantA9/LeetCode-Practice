from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list of numbers into a set to remove duplicates and allow O(1) lookups for the elements
        numSet = set(nums)
        
        # Initialize a variable to keep track of the longest sequence length
        longest = 0
        
        # Iterate over each number in the original list
        for n in nums:
            # Check if the current number is the start of a sequence (i.e., there is no number 'n-1' in the set)
            if (n - 1) not in numSet:
                # If it is the start, initialize the length of this sequence
                length = 0
                
                # Continue checking for the next numbers in the sequence by incrementing length until the sequence breaks
                while (n + length) in numSet:
                    length += 1
                
                # Update the longest sequence found so far
                longest = max(length, longest)
        
        # Return the length of the longest consecutive sequence
        return longest