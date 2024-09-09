class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths of the strings are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Initialize dictionaries to count character frequencies, this are the hashmaps
        countS, countT = {}, {}

        # Count frequencies of each character in both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare character frequencies
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
