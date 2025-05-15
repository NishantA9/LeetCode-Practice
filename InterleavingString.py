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