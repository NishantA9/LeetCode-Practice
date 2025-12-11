class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Initialize the index 'i' to the last character of the string
        i, length = len(s) - 1, 0
        
        # Skip trailing spaces at the end of the string
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # Count the length of the last word, whitespace and inbounds check
        while i >= 0 and s[i] != " ":
            length += 1  # Increase the length counter for each character in the last word
            i -= 1       # Move to the previous character
        
        # Return the length of the last word
        return length
