from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict with a list as the default value type, This will store the mapping of character count to the list of anagrams
        res = defaultdict(list)
        
        # Iterate through each string in the input list
        for s in strs:
            count = [0] * 26 # Initialize a list of 26 zeros representing the count of each character (a-z)
            
            # Count the occurrences of each character in the current string
            for c in s:
                count[ord(c) - ord("a")] += 1 # Taking the ASCII value of the character and subtracting the ASCII value of 'a' to get the index
            
            res[tuple(count)].append(s) # Use the character count tuple as the key to group anagrams together
        
        return res.values() # Return all the grouped anagrams as a list of lists