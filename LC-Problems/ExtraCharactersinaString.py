from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Convert dictionary to set for O(1) lookups
        words = set(dictionary)
        # dp[i] stores min extra chars needed for substring s[i:]
        # Base case: empty string needs 0 extra chars
        dp = {len(s): 0}

        def dfs(i):
            # If we've already solved for index i, return cached result
            if i in dp:
                return dp[i]
            
            # Initially, treat current char as extra (1 + solve rest)
            res = 1 + dfs(i + 1)
            
            # Try all possible words starting at index i
            for j in range(i, len(s)):
                # If we find a dictionary word, we can skip these chars
                # and solve for the remaining string
                if s[i:j + 1] in words:
                    res = min(res, dfs(j + 1))
            
            # Cache and return the minimum extra chars needed
            dp[i] = res
            return res

        # Start from index 0 to solve for entire string
        return dfs(0)