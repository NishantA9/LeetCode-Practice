class Solution:
    def longestPalindrome(self, s: str) -> str: #Brute force TC: O(n^2) and SC: o(1)
        res = "" # Resulting longest palindrome substring
        reslen = 0 # Length of longest palindrome found
        def helper(l,r): #EXPAND around center in both cases # noqa: E741
            nonlocal res, reslen
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:  # If the current palindrome is longer than previous best, update
                    res = s[l:r+1] # Update longest palindrome string
                    reslen = r-l+1 # Update its length
                l -= 1 # noqa: E741
                r += 1  
        for i in range(len(s)):
            helper(i,i) # Case 1: Odd length palindrome (center at i)
            helper(i,i+1) # Case 2: Even length palindrome (center between i and i+1)
        return res  # Return the longest palindromic substring found

# another sol without using helper function
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            l, r = i, i   # Check for odd length palindrome (center at i)  # noqa: E741
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1 # noqa: E741
                r += 1
            l, r = i, i+1  # Check for even length palindrome (center between i and i+1) # noqa: E741
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1 # noqa: E741
                r += 1
        return res
'''