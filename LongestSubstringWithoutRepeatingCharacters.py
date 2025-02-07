#Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # A set to store unique characters in the current substring
        l = 0 # Two pointers for the sliding window: `l` (left) and `r` (right) # Left pointer to track the start of the substring  # noqa: E741
        res = 0  # Variable to store the result (length of the longest substring)
        
        # Iterate through the string using the right pointer
        for r in range(len(s)):
            # If the current character is already in the set, it means there's a duplicate
            while s[r] in charSet:
                charSet.remove(s[l]) # Remove the character at the left pointer from the set
                l += 1 # Move the left pointer one step to the right to shrink the window # noqa: E741
            charSet.add(s[r]) # Add the current character to the set
            # Calculate the length of the current substring and update the result
            res = max(res, r - l + 1) # The length is (r - l + 1), where `r` is the right pointer, and `l` is the left pointer
        return res  # Return the length of the longest substring without repeating characters