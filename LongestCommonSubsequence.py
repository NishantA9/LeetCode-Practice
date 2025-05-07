class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)] # Step 1: Initialize DP table with extra row/column for base case
        for i in range(len(text1) - 1, -1, -1): # Step 2: Fill table from bottom-right to top-left
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:  # Characters match: take diagonal value + 1
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else: # Characters don't match: take max of right or down
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0] # Step 3: Result is in dp[0][0] → full strings