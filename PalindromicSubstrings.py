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