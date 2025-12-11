class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: #Top Down DP, TC & SC: O(m * n)
        memo = {} # Memoization dictionary to cache results for (i, j) pairs
        def dfs(i,j): # Recursive helper function with memoization
            if i == len(text1) or j == len(text2): # Base case: if we reach the end of either string, return 0
                return 0
            if (i,j) in memo: # If result already computed for this state, return it
                return memo[(i,j)]
            if text1[i] == text2[j]: # If characters match, take 1 and move both pointers forward
                memo[(i,j)] = 1 + dfs(i+1, j+1)
            else: # Else, take the max of skipping a char from either text1 or text2
                memo[(i,j)] = max(dfs(i+1,j), dfs(i,j+1))
            return memo[(i,j)]
        return dfs(0,0) # Start the recursion from the beginning of both strings

#the above code is a top-down dynamic programming solution using memoization. and here is the bottom-up dynamic programming solution below:
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)] # Step 1: Initialize DP table with extra row/column for base case
#         for i in range(len(text1) - 1, -1, -1): # Step 2: Fill table from bottom-right to top-left
#             for j in range(len(text2) - 1, -1, -1):
#                 if text1[i] == text2[j]:  # Characters match: take diagonal value + 1
#                     dp[i][j] = 1 + dp[i + 1][j + 1]
#                 else: # Characters don't match: take max of right or down
#                     dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
#         return dp[0][0] # Step 3: Result is in dp[0][0] → full strings