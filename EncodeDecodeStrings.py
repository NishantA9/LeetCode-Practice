from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Initialize an empty result string
        res = ""
        # For each string in the list, append its length, a delimiter, and the string itself to the result
        for s in strs:
            res += str(len(s)) + "#" + s
        # Return the encoded string
        return res

    def decode(self, s: str) -> List[str]:
        # Initialize an empty list to store the decoded strings
        res, i = [], 0
        # Iterate over the encoded string
        while i < len(s):  # Corrected 'str' to 's'
            # Find the position of the delimiter '#'
            j = i
            while s[j] != "#":  # Corrected 'str[j]' to 's[j]'
                j += 1
            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the string using the length
            res.append(s[j + 1: j + 1 + length])
            # Move the index to the start of the next encoded segment
            i = j + 1 + length
        # Return the list of decoded strings
        return res
