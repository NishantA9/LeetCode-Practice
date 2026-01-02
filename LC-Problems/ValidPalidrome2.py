class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == "": # Check if the string is empty, which is considered a valid palindrome
            return True        
        l, r = 0, len(s) - 1 # Initialize two pointers: left at start, right at end  # noqa: E741
        while l < r: # Loop while left pointer is less than right pointer           
            if s[l] != s[r]:  # If characters at pointers don't match                
                skipL, skipR = s[l+1 : r + 1], s[l:r] # Create two substrings: one skipping left char, one skipping right char                
                return (skipL == skipL[::-1] or skipR == skipR[::-1]) # Check if either substring is a palindrome (reversed equals itself)           
            l, r = l + 1, r - 1  # Move pointers inward       # noqa: E741  
        return True # If no mismatches found, it's a palindrome