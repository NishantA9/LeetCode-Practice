from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict with a list as the default value type
        # This will store the mapping of character count to the list of anagrams
        res = defaultdict(list)
        
        # Iterate through each string in the input list
        for s in strs:
            # Initialize a list of 26 zeros representing the count of each character (a-z)
            count = [0] * 26
            
            # Count the occurrences of each character in the current string
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # Use the character count tuple as the key to group anagrams together
            res[tuple(count)].append(s)
        
        # Return all the grouped anagrams as a list of lists
        return res.values()
