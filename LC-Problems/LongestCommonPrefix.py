from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize result variable to store the longest common prefix
        res = ""
        
        # Iterate over each character position of the first string
        for i in range(len(strs[0])):
            # Check if the current character matches across all strings
            for s in strs:
                # If any string has a different character at position 'i' or ends, return result
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            
            # If all strings matched the character, add it to the result
            res += strs[0][i]
        
        # Return the longest common prefix found
        return res
