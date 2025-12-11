class Solution:
    def characterReplacement(self, s: str, k: int) -> int: #sliding window
        count = {} # Dictionary/ HashMap to count the frequency of characters in the current window
        res = 0 # Variable to store the result (maximum length of a valid substring)
        l = 0 # Left pointer for the sliding window # noqa: E741
        
        for r in range(len(s)):  # Iterate through the string with the right pointer
            count[s[r]] = 1 + count.get(s[r], 0) # Add the current character to the count dictionary
            while (r - l + 1) - max(count.values()) > k: # Check if the current window is valid, Invalid if the number of replacements needed > k
                count[s[l]] -= 1 # If invalid, shrink the window from the left
                l += 1 # noqa: E741 # move the left pointer to the right
            res = max(res, r - l + 1) # Update the result with the size of the valid window
        return res  # Return the maximum length of the valid substring