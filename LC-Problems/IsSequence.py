class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize 2 pointers for both strings
        i, j = 0, 0
        
        # Loop through characters in 't' as long as there are characters in 's' to match
        while i < len(s) and j < len(t):
            # Check if current characters match
            if s[i] == t[j]:
                i += 1  # Move to next character in 's' since there's a match
            j += 1      # Always move to the next character in 't'
        
        # Check if we've matched all characters in 's' if s goes out of bounds or j reaches the end of 't'
        return True if i == len(s) else False