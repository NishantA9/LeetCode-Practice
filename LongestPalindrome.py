class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen, res = set(), 0  # seen holds chars with odd count so far, res accumulates pairs
        for c in s:
            if c in seen:
                seen.remove(c)  # found a pair for c, remove odd mark
                res += 2  # add the pair length to result
            else:
                seen.add(c)  # mark c as seen odd number of times
        return res + 1 if seen else res  # if any odd count remains, one center char can be used