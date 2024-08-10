from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize a set to keep track of seen numbers
        hashSet = set()
        
        # Iterate through each number in the list
        for n in nums:
            # If the number is already in the set, a duplicate is found
            if n in hashSet:
                return True
            # Add the number to the set
            hashSet.add(n)
        
        # If no duplicates are found, return False
        return False
