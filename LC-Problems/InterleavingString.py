class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool: # DFS with memoization TC & SC: O(len(s1) * len(s2))
        if len(s1) + len(s2) != len(s3): # If lengths don't match, s3 can't be formed by interleaving s1 and s2
            return False # Early exit if lengths are incompatible
        dp = {} # Memoization dictionary to store results of subproblems
        def dfs(i,j): # Recursive DFS function that checks if s3[i+j:] can be formed by interleaving s1[i:] and s2[j:]
            if i == len(s1) and j == len(s2): # Base case: if we've reached the end of both s1 and s2, return True
                return True
            if (i,j) in dp: # If this state has been computed before, return the stored result
                return dp[(i,j)]
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j): # Check if current character of s1 matches s3, and recurse by moving one step in s1
                return True
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i,j+1): # Check if current character of s2 matches s3, and recurse by moving one step in s2
                return True
            dp[(i,j)] = False # If neither condition works, store result as False for current (i, j)
            return False
        return dfs(0,0) # Start the recursion from the beginning of both strings
    
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False         # If lengths don't match, s3 can't be formed from s1 and s2
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]        # Create a 2D DP table
        dp[len(s1)][len(s2)] = True  # Base case: all strings exhausted
        for i in range(len(s1), -1, -1):        # Fill the table from bottom to top
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:  # If s1 has characters left and matches s3's current char
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:  # If s2 has characters left and matches s3's current char
                    dp[i][j] = True
        return dp[0][0]  # Is s3 interleaving from s1[0:] and s2[0:]?
'''
