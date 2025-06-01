from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""  # Initialize result string to store the prefix
        for i in range(len(strs[0])):  # Loop over each character index in the first word
            for s in strs:  # Compare that character with every other string
                if i == len(s) or s[i] != strs[0][i]:  # If mismatch or out of bounds
                    return res  # Return result so far
            res += strs[0][i]  # If all strings have the same character at i, add it to result
        return res  # Return full prefix if loop completes