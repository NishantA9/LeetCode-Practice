class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}  # Memoization dictionary: (i, j) → count
        def dfs(i, j):
            if j == len(t): # If we matched all of t
                return 1
            if i == len(s): # If we ran out of s but t still has characters
                return 0
            if (i, j) in cache: # Use memoized result if available
                return cache[(i, j)]
            if s[i] == t[j]: # Option 1: match and move both pointers # Option 2: skip current char in s
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j) # Characters don’t match → skip s[i]
            return cache[(i, j)]
        return dfs(0, 0)