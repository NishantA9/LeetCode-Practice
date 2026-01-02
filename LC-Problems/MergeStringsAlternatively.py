class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0  # Initialize pointers for both words
        res = []     # List to store merged characters
        while i < len(word1) and j < len(word2):  # Loop until one word ends
            res.append(word1[i])  # Add character from word1
            res.append(word2[j])  # Add character from word2
            i += 1  # Move to next character in word1
            j += 1  # Move to next character in word2
        res.append(word1[i:])  # Add remaining characters from word1 (if any)
        res.append(word2[j:])  # Add remaining characters from word2 (if any)
        return "".join(res)   # Join list into a string and return