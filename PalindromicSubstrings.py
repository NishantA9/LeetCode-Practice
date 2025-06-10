class Solution:
    def countSubstrings(self, s: str) -> int: # TC: O(n^2) and SC: O(1)
        res = 0  # To store the total count of palindromic substrings
        def helper(l, r): # Helper function to expand around center and count palindromes #noqa: E741
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]: # Expand while the characters at l and r are equal and in bounds
                res += 1 # Valid palindrome found
                l -= 1  # Expand to the left #noqa: E741
                r += 1  # Expand to the right
        for i in range(len(s)): # Try every possible center (both odd and even length)
            helper(i, i) # Odd-length palindromes (center at i)
            helper(i, i + 1) # Even-length palindromes (center between i and i+1)
        return res  # Return the total number of palindromic substrings

# another sol but outward function is used
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)            # Count odd-length palindromes centered at s[i]
            res += self.countPali(s, i, i + 1)            # Count even-length palindromes centered between s[i] and s[i+1]
        return res
    def countPali(self, s, l, r):  # noqa: E741
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:         # Expand while valid and characters match
            res += 1
            l -= 1  #noqa: E741
            r += 1
        return res
'''