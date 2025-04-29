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