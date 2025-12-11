from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # Initialize an empty result string
        # For each string in the list, append its length, a delimiter, and the string itself to the result
        for s in strs:
            res += str(len(s)) + "#" + s
        return res # Return the encoded string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # Initialize an empty list to store the decoded strings
        # Iterate over the encoded string
        while i < len(s):  
            j = i # Find the position of the delimiter '#'
            while s[j] != "#":  
                j += 1
            length = int(s[i:j])  # Extract the length of the next string
            res.append(s[j + 1: j + 1 + length]) # Extract the string using the length
            i = j + 1 + length  # Move the index to the start of the next encoded segment
        
        return res # Return the list of decoded strings
