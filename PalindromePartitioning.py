from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []           # Final result list storing all valid palindrome partitions
        part = []          # Temporary list to hold the current partition (path)
        def dfs(i):
            if i >= len(s):  # If we've used all characters in the string
                res.append(part.copy())  # Save the current valid partition
                return
            for j in range(i, len(s)):            # Explore every possible end position from i to len(s)
                if self.isPali(s, i, j):                # Check if the current substring is a palindrome
                    part.append(s[i:j+1])  # Choose substring
                    dfs(j+1)               # Recurse on the remaining string
                    part.pop()             # Backtrack
        dfs(0)  # Start DFS from index 0
        return res
    def isPali(self, s, l, r):        # Helper to check if substring s[l...r] is a palindrome  # noqa: E741
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1  # noqa: E741
        return True