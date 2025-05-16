class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}  # Memoization dictionary: (i, j) → bool
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p): # If both s and p are fully matched
                return True
            if j >= len(p): # If pattern is finished but string isn't
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".") # Check if current characters match (with '.' wildcard support)
            if (j + 1) < len(p) and p[j + 1] == "*": # If next pattern character is '*'
            # Option 1: Skip 'char*' block → dfs(i, j+2) # Option 2: Use '*' if there's a match → dfs(i+1, j)
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]
            if match:   # If characters match normally, continue
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False            # If no match
            return False
        return dfs(0, 0)